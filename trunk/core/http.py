"""
    Enema module (core): Http request handler
    Copyright (C) 2011 Valeriy Bogachuk
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import os
import sys
import time
import socket
import core.txtproc
from PyQt4 import QtCore
from threading import *
from urllib import request
from urllib.error import HTTPError
from urllib.error import URLError
from urllib.parse import urlencode
from core.e_const import QUOTED_CONTENT


class HTTP_Handler(QtCore.QObject):

    logSignal = QtCore.pyqtSignal(str)
    requestDoneSignal = QtCore.pyqtSignal(bool)
    
    def __init__(self):
        QtCore.QObject.__init__(self)

    def kwordsInHeader(self, header):
        kwFound = False
        if "[sub]" in header:
            kwFound = True
        if "[cmd]" in header:
            kwFound = True
        if "[blind]" in header:
            kwFound = True
        return kwFound
        
    #Injection in cookies?:
    def isInjectionInHeader(self, vars):
        if self.kwordsInHeader(vars['user_agent']):
            return "user_agent"
        if self.kwordsInHeader(vars['cookie']):
            return "cookie"
        if self.kwordsInHeader(vars['referer']):
            return "referer"
        if self.kwordsInHeader(vars['x_forwarded_for']):
            return "x_forwarded_for"

    #SET variables in string to valid value 
    def buildQuery(self, query, vars, args=None):
        ms =  core.txtproc.strToSqlChar(vars['ms'], vars['db_type'])
        try:
            if vars['db_type'] == "MySQL" and (vars['task'] =='tables' or vars['task'] =='columns'):
                args['cdb'] = core.txtproc.strToSqlChar(args['cdb'], vars['db_type'])
        except Exception:
            pass
        if vars is None:
            vars = {}
        if args is None:
            args = {}
        query_vars = {
        '${MS}' : ms, 
        #Args---
        '${current_db}' : args.setdefault('cdb'), 
        '${current_table}' : args.setdefault('ctbl'),
        '${symbol_num}' : args.setdefault('symbol_num'), 
        '${condition}' : args.setdefault('condition'),
        '${time}' : args.setdefault('delay'),
        '${num}' : args.setdefault('num'), 
        '${row}' : args.setdefault('row'),
        '${btable}' : args.setdefault('btable'),
        '${current_column}' : args.setdefault('ccol'),
        '${ordinal_position,}' : args.setdefault('num'), 
        '${column}' : args.setdefault('column'), 
        '${hex}' : args.setdefault('hex'), 
        #Vars---
        '${selected_table}' : vars.setdefault('selected_table'), 
        '${cmd}' : vars.setdefault('cmd'), 
        '${query_cmd}' : vars.setdefault('query_cmd'), 
        '${login}' : vars.setdefault('login'), 
        '${password}' : vars.setdefault('password'), 
        '${key}' : vars.setdefault('key'),
        '${table}' : vars.setdefault('table')} 
        for key in query_vars:
            query = query.replace(key, str(query_vars[key]))
        if vars['isRandomUpCase']:
            query = core.txtproc.rndUpCase(query)
        return query

    def buildRequest(self, strVar, query, isCmd, isHeader, header=None):
        if isHeader:
            if header == "cookie" or header == "referer":
                query = request.quote(query)
                strVar = strVar.replace("[eq]", "%3d")
        else:
            strVar = strVar.replace("[eq]", "=")
        if isCmd:
            if "[cmd]" in strVar:
                strVar = strVar.replace("[cmd]", query)
                if "[sub]" in strVar:
                    strVar = strVar.replace("[sub]", "null")
        else:
            if "[cmd]" in strVar:
                strVar = strVar.replace(";[cmd]", "")
            strVar = strVar.replace("[sub]", query)
        if "[blind]" in strVar:
            strVar = strVar.replace("[blind]", query)
        return strVar

    #checking for special keywords
    def checkForSpecKw(self, string):
        parsedStr = string
        if "urlenc^" in string:
            parsedStr = core.txtproc.extractString(string, "urlenc")
            hexStr = core.txtproc.strToHex(parsedStr['substr'], False)
            urlhex = hexStr.replace("0x", "%")
            parsedStr['substr'] = urlhex
        return parsedStr
            
    #Content parser
    def contentParse(self, content, match_pattern, match_sybol):
        patternStr = content.find(match_pattern)
        fromStr = content.find(match_sybol, patternStr, len(content))
        fromStr += 1
        toStr = content.find(match_sybol, fromStr, len(content))
        if (fromStr or toStr) <= 0:
            file = open("tmp/err_log.html", "w")
            file.write(content)
            file.close()
            time.sleep(0.01)
            self.logSignal.emit("\n==================[SERVER RESPONSE]==================\n\n"\
            + content + \
            ">>> Html saved to: " + os.path.abspath("tmp/err_log.html"))
            return "no_content"
        return content[fromStr:toStr]
        
    #Preparing POST data
    def preparePostData(self, data, query, isCmd, encoding):
        #Post data must be Var=value, otherwise function fails when trying to build dictionary.
        data = data.replace("=&",  "=[empty]&").replace("\n", "")
        if "[blind]" in data:
            query = query.replace("=", "[eq]")
            data = data.replace("[blind]", query)
        data = data.replace(":",  "[colon]")
        if len(data) < 3:
            self.logSignal.emit("No POST data specified.")
            return
        if  data[-1] == "=":
            data += "[empty]"
        data = ''.join([x.replace("=",  ":") for x in data])
        data = data.replace("[eq]", "=").replace("[eq-urlhex]",  "=")
        if isCmd:
            if "[cmd]" in data:
                data = data.replace("[cmd]", query)
                if "[sub]" in data:
                    data = data.replace("[sub]", "1")
        else:
            if "[cmd]" in data:
                data = data.replace(";[cmd]", "")
            data = data.replace("[sub]", query)
        data = data.split("&")
        try:
            data = dict([s.split(':') for s in data])
        except ValueError as err:
            self.logSignal.emit(\
            "[x] Error. Can't prepare post data (bad characters detected). Use [eq] keyword instead of '='\n\n[details]: " + str(err))
            return "fail"
        for key, value in data.items():
            if value == "[empty]":
                data[key] = ""
            if "[colon]" in value:
                data[key] = value.replace("[colon]", ":")
        urlEncoded = urlencode(data)
        postData = urlEncoded.encode(encoding)
        return postData

    #Http request main function:
    def httpRequest(self, query, isCmd, vars, blind=False):
        urlOpener = request.build_opener()
        data = vars['data']
        data = data.replace("+",  " ").replace("%3D",  "[eq-urlhex]")
        data = request.unquote(data)
        vuln_header = self.isInjectionInHeader(vars)

        if vars['method'] == "POST":
            postData = self.preparePostData(data, query, isCmd, vars['encoding'])
            if (postData is None or postData == "fail"):
                return "no_content"
            reqLog = "\n[POST] " + vars['url'] + "\n+data+\n{\n" + postData.decode(vars['encoding']) + "\n}"
        else:
            get_url = self.buildRequest(vars['url'], query, isCmd, False)
            parsed = self.checkForSpecKw(get_url)
            if type(parsed) is dict:
                get_url = request.quote(parsed['str'])
                get_url = get_url.replace("ERASEDSUBSTRING", parsed['substr'])
            else:
                get_url = request.quote(get_url)
            #Replacing important symbols
            get_url = get_url.replace("%3D", "=").replace("%26", "&").replace("%3A", ":").replace("%3F", "?")
            reqLog = "\n[GET] " + get_url

        reqLog += "\n+headers+\n{"
        
        #If injection in header
        if vuln_header is not None:
            inj_header = self.buildRequest(vars[vuln_header], query, isCmd, True, vuln_header)
            
        #Adding headers if defined
        if len(vars['user_agent']) > 0:
            if vuln_header == "user_agent":
                header = inj_header
            else:
                header = vars['user_agent']
            reqLog += "\nUser-Agent: " + header
            urlOpener.addheaders = [('User-Agent', header)]
        if len(vars['cookie']) > 0:
            if vuln_header == "cookie":
                header = inj_header
            else:
                header = vars['cookie']
            reqLog += "\nCookie: " + header
            urlOpener.addheaders = [('Cookie', header)]
        if len(vars['referer']) > 0:
            if vuln_header == "referer":
                header = inj_header
            else:
                header = vars['referer']
            reqLog += "\nReferer: " + header
            urlOpener.addheaders = [('Referer', header)]
        if len(vars['x_forwarded_for']) > 0:
            if vuln_header == "x_forwarded_for":
                header = inj_header
            else:
                header = vars['x_forwarded_for']
            reqLog += "\nX-Forwarded-For: " + header
            urlOpener.addheaders = [('X-Forwarded-For', header)]
        reqLog += "\n}"
        
        start_time = time.time()
        try:
            if not vars['method'] == "POST":
                postData = None
                url = get_url
            else:
                url = vars['url']
            self.logSignal.emit(reqLog)
            response = urlOpener.open(url, postData, vars['timeOut'])
            content = response.read()
        except HTTPError as httpErr: 
            content = httpErr.read()
        #Handling timeout. 
        except socket.error:
            errno, errstr = sys.exc_info()[:2]
            if errno == socket.timeout:
                time.sleep(0.01)
                self.logSignal.emit("\n\n[HTTP Timeout]")
                return "[---Timed out---]"
        except URLError as uerr:
            if isinstance(uerr.reason, socket.timeout):
                time.sleep(0.01)
                self.logSignal.emit("\n\n[HTTP Timeout]")
                return "[---Timed out---]"
        except ValueError as err:
            time.sleep(0.01)
            self.logSignal.emit("\n[x] Can't start task.\n\n[reason]: " + str(err))
            return "no_content"
        
        if blind:
            if vars['blind_inj_type'] == "Time":
                response_time = round((time.time() - start_time), 4)
                return response_time               
        if not isCmd:
            if QUOTED_CONTENT:
                content = request.unquote(content)
            try:
                content = content.decode(vars['encoding'])
            except:
                self.logSignal.emit("[x] Can't decode content (current encoding: " + vars['encoding'] + "). Try to change it in Tools->Pereferences.")
                return "no_content"
            if blind:
                if vars['blind_inj_type'] == "Boolean":
                    patternIndex = content.find(vars['bool_pattern'])
                    if patternIndex <= 0:
                        return False
                    else:
                        return True
            db_data = self.contentParse(content, vars['mp'], vars['ms'])
        else:
            db_data = 0
        return db_data
        
