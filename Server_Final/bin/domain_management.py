#Domain managing

import sys
import os
import threading

#from distutils.core import setup
#import py2exe

#setup(console=['domain_management.py'])

domains = []
path = os.getcwd()
#print(path)
if(os.path.exists(path+"\conf") and os.path.isdir(path+"\conf")):
    path = path + "\conf"
    path = path + "\domain_names.conf"

    with open(path,"r") as f:
        sitename = f.readline()
        for sitename in f:
            #print(sitename)
            if sitename[0]!='#':
                lngth = len(sitename)
                sitename = sitename[1:lngth-2]
                domains.append(sitename)
    f.close()

def eCheck(path):
    if path.endswith('/'):
        path = path[:len(path)-1]
    print(path)
    flush,extention=os.path.splitext(path)
    print(flush)
    print(extention)
    extention = extention.lower()
    print(extention)
    content_type = {
        '.png':'image/png',
        '.jpg':'image/jpeg',
        '.jpeg':'image/jpeg',
        '.gif':'image/gif'
    }
    typ = []
    if extention in content_type:
        self.send_response(200)
        self.send_header('Content-type',content_type[extention])
        self.end_headers()
        #typ.append("rb")
        #typ.append(path)
        return "rb"
        #with open(path,'rb') as ofile:
        #    self.wfile.write(ofile.read())
    else:
        self.send_response(200)
        self.send_header("Content-type",'text/plain')
        self.end_headers()
        typ.append("r")
        typ.append(path)
        return "r"
        #with open(path) as ofile:
        #    self.wfile.write(bytes(ofile.read(),'utf-8'))
def err():
    htcode = '<html>'
    htcode += '<head>'
    htcode += '<meta charset="utf-8">'
    htcode += '<title>Error</title>'
    htcode += '</head>'
    htcode += '<body style="background-color:black"><br><br>'
    htcode += '<i><p style="font-family:serif;font-size:34px;text-align:center;color:white;">404 , Not Found</p></i>'
    htcode += '<br></body></html>'
    return htcode
    #wfile.write(bytes(htcode,"utf-8"))



def loadSite(str):
    path = os.getcwd()
    path = path + "\Domains"
    print(path)
    if os.path.exists(path) and os.path.isdir(path):
        path = path + "\\" + str
        if(os.path.exists(path) and os.path.isdir(path)):
            #path += "\index.html"
            indexof = path.find('\\')

            if(os.path.exists(path)and os.path.isfile(path)):
                with open(path) as ofile:
                    htcode = ofile.read()
                ofile.close()
        else:
            err()
    return htcode
    #wfile.write(bytes(htcode,"utf-8"))
