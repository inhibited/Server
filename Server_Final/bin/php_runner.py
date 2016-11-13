#!/usr/bin/env python3

import os
import urllib.request

#os.system('php -S localhost:9990')
phpsyntax="<?php $out = shell_exec('python3 "

def getData(filepath):
    #print('in runner')
    #print(filepath)
    url = "http://localhost:7777/hdocs/"
    url = url + filepath
    #print(url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
        data = data.decode('utf-8')
    except:
        return "Please Start PHP server."
    #print(data)
    return data
def runPython(filename):
    phpfile = phpsyntax+filename+"');"+' echo "<pre>$out</pre>"; ?>'
    #phpfile="<?php shell_exec('python3 "+filename+" 2>&1 | tee -a /tmp/mylog 2>/dev/null >/dev/null &"+"');"
    fl = open("tmp.php","w+")
    fl.write(phpfile)
    fl.close()
    url = "http://localhost:7777/tmp.php"
    url2 = "http://localhost:8888/tmp.php"
    response = urllib.request.urlopen(url)
    data = response.read()
    data = data.decode('utf-8')
    #print(data)
    return data
