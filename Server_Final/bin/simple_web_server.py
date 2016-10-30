#!/usr/bin/python3
#Backdated server
#This is not for production use

import cgi
import sys
import os
import io
import logging
#import url_parser
import socketserver
import subprocess
import domain_management
import posixpath
import urllib.parse
import html
import mimetypes
import time
import http.server
import HTTPStatus
import shutil
import re
import getRoot
import getHostPort
import php_runner

_version_ = 1.0

close = False
host = getHostPort.host
#port = getHostPort.portfind()
port = int(input('Enter Port : '))
rootdir = getRoot.dir()
#home = host+str(port)
eext=""
Code = HTTPStatus.code

class HTTPRecquestHandler(http.server.BaseHTTPRequestHandler):
    sys_version = "Python/"+sys.version.split()[0]
    server_version = "BaseHTTP/"+ str(_version_)
    default_request_version = "HTTP/1.1"

    #system mimetypes
    if not mimetypes.inited:
        mimetypes.init()
    extensions = mimetypes.types_map.copy()
    #': 'application/octet-stream',
    extensions.update({
        ''   :'application/octet-stream',
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
        '.mp4':'video/mp4',
        '.mkv':'video/x-matroska',
        '.mp3':'audio/mp3'
        })
    def copyfile(self,source,dest):
        shutil.copyfileobj(source,dest)

    def do_HEAD(self):
        logging.debug('HEADER %s'%(self.path))
        path = self.translate_path(self.path)
        ofile = None
        ctype = None
        flush,ext = posixpath.splitext(path)
        if ext in self.extensions:
            ctype=self.extensions[ext]
        ext = ext.lower()
        if ext in self.extensions:
            ctype=self.extensions[ext]
        try:
            ofile = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
        try:
            self.send_response(200)
            self.send_header("Content-type", ctype)
            file_state = os.fstat(ofile.fileno())
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
            self.end_headers()
            ofile.close()
        except:
            ofile.close()

    def do_GET(self):
        logging.debug('GET %s'%(self.path))
        #print(self.command+" "+self.path+" "+self.default_request_version)
        #print("Request path : ")
        #print(self.path)
        self.path = self.path.rstrip()
        #if self.path.endswith('/'):
            #self.path = self.path[:-1]
        #print(self.path)
        path = self.translate_path(self.path)
        #print("translate_path : ")
        homepage = os.path.join(rootdir,"index.html")
        #print(homepage)
        self.path = self.path.rstrip()

        if self.path=='/info' or self.path=='/info/':
            #with open(homepage) as f:
            #    self.send_response(200)
            #    self.send_header('Content-type','text/html')
            #    self.end_headers()
            #    self.wfile.write(bytes(f.read(),'utf-8'))
            #if not os.path.exists(homepage):
            htc = "<html><head><title>Backdated Server</title></head>"
            htc += "<body>Welcome<br></body></html>"
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(htc,'utf-8'))
        elif(self.path =='/about' or self.path=='/about/'):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.about()
        else:
            #print("else")
            #print(path)

            if os.path.exists(path):
                if os.path.isdir(path):
                    for index in "index.html", "index.htm":
                        index = os.path.join(path, index)
                        if os.path.exists(index):
                            path = index
                            break
                    else:
                        #htc = "<html><head><title>Under Maintanance</title></head>"
                        #htc += "<body>Nothing Here.<br></body></html>"
                        #self.send_response(200)
                        #self.send_header('Content-type','text/html')
                        #self.end_headers()
                        #self.wfile.write(bytes(htc,'utf-8'))

                        fl = self.show_dir(path)
                        shutil.copyfileobj(fl,self.wfile)
                        return
            ctype = None
            flush,ext = posixpath.splitext(path)
            if ext in self.extensions:
                ctype=self.extensions[ext]
            ext = ext.lower()
            if ext in self.extensions:
                ctype=self.extensions[ext]
            #print(ext)


            #print(path)
            try:
                ofile = open(path,'rb')
            except OSError:
                self.send_error(404,"File not found")
                return None

            if(ext=='.php'):
                #print('here')
                filePath = self.path
                filePath = filePath.lstrip('/')
                dataD = php_runner.getData(filePath)
                #print("data received")
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(bytes(dataD,'utf-8'))
                return
            if(ext=='.py'):
                #print('here')
                filePath = self.path
                fname = filePath.split('/')
                filePath = filePath.lstrip('/')
                #print(fname)
                #dataD = php_runner.runPython(fname[len(fname)-1])
                #print("data received")
                output=""
                #output="<!DOCTYPE html><html><head><title>Python Output</title></head><body>"
                try:
                    output += subprocess.getoutput('python3 '+path)
                except subprocess.CalledProcessError as err:
                    output += err
                #print(output)
                #output+="</body></html>"
                self.send_response(200)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                self.wfile.write(bytes(output,'utf-8'))
                return
            self.send_response(200)
            self.send_header("Content-type",ctype)
            file_state = os.fstat(ofile.fileno())
            self.send_header("content-length",str(file_state[6]))
            self.send_header("Last-Modified",self.date_time_string)
            self.end_headers()
            try:
                self.wfile.write(ofile.read())
                #print("lastly here")
                #self.copyfile(ofile,self.wfile)
            finally:
                ofile.close()

    def translate_path(self,path):
        path = path.split('?',1)[0]
        path = path.split('#',1)[0]

        path = path.rstrip()
        t_slash = path.endswith('/')

        try:
            path = urllib.parse.unquote(path,errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
            print(path)
        path = posixpath.normpath(path)
        words = path.split('/')
        words = filter(None,words)
        path = rootdir
        path = os.path.join(path,"hdocs")
        for word in words:
            #print(word)
            if os.path.dirname(word) or word in (os.curdir,os.pardir):
                continue
            path = os.path.join(path,word)
        #print(path)
        return path

    def do_POST(self):
        #idata = web.input()
        #print(idata)
        logging.debug('POST %s' % (self.path))

        ctype, pdict = cgi.parse_header(self.headers['content-type'])


        if ctype == 'multipart/form-data':
            pdict['boundary']=bytes(pdict['boundary'],'utf-8')
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers['content-length'])
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        if self.path.find('?') < 0:
            back = self.path
        else:
            self.path[:self.path.find('?')]
        logging.debug('TYPE %s' % (ctype))
        logging.debug('PATH %s' % (self.path))
        logging.debug('ARGS %d' % (len(postvars)))
        if len(postvars):
            i = 0
            for key in sorted(postvars):
                logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
                i += 1
        #postvars = postvars.decode('utf-8')
        print(postvars)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        flush,ext = posixpath.splitext(self.path)
        if self.path.endswith('.php') or self.path.endswith('.php/'):
            #print('here')
            filePath = self.path
            filePath = filePath.lstrip('/')
            dataD = php_runner.getData(filePath)
            #print("data received")
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(dataD,'utf-8'))
            return
        if self.path.endswith('.py') or self.path.endswith('.py/'):
            #print('here')
            filePath = self.path
            fname = filePath.split('/')
            filePath = filePath.lstrip('/')
            #print(fname)
            #dataD = php_runner.runPython(fname[len(fname)-1])
            #print("data received")
            output=""
            #output="<!DOCTYPE html><html><head><title>Python Output</title></head><body>"
            try:
                path = self.translate_path(self.path)
                output += subprocess.getoutput('python3 '+path)
            except subprocess.CalledProcessError as err:
                output += err
            #print(output)
            #output+="</body></html>"
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(bytes(output,'utf-8'))
            return
    def about(self):
        htcode = '<html>'
        htcode += '<head>'
        htcode += '<meta charset="utf-8">'
        htcode += '<title>Backdated Server</title>'
        htcode += '</head>'
        htcode += '<body style="background-color:black"><br><br>'
        htcode += '<i><p style="font-family:serif;font-size:34px;text-align:center;color:white;">This is a Software Development Project of 2-2 term of CSE,KU.</p></i>'
        htcode += '<br></body></html>'
        self.wfile.write(bytes(htcode,"utf-8"))

    def show_dir(self,path):
        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(code['NOT_FOUND'],"Access Denied")
            return None
        list.sort(key=lambda a: a.lower())
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path,errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath)
        enc = sys.getfilesystemencoding()
        title = 'Directory : %s' % (displaypath)
        r.append('<!DOCTYPE HTML>')
        r.append('<html>\n<head>')
        r.append('<meta http-equiv="Content-Type"content="text/html; charset=%s">' % enc)
        r.append('<title>%s</title>\n</head>' % title)
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
            r.append('<li><a href="%s">%s</a></li>'% (urllib.parse.quote(linkname,errors='surrogatepass'),html.escape(displayname)))
        r.append('</ul>\n<hr>\n</body>\n</html>\n')
        encoded ='\n'.join(r).encode(enc,'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f

def main():
    global server
    #server = http.server.HTTPServer((host,port),HTTPRecquestHandler)
    server = socketserver.
    print('Server started on port',port)
    print('....')
    print('ctrl-c to quit server.')
    try:
        server.serve_forever()
        if(close==True):
            raise
            #server.server_close()
    except KeyboardInterrupt:
        server.server_close()
        print("Server Stopped")
    except:
        server.server_close()
        print("Server Stopped")
if __name__ == '__main__':
    main()
