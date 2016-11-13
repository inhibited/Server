import os
import re

host =""

def portfind():
    cwd = os.getcwd()
    cwd = os.path.join(cwd,'..')
    cwd = os.path.abspath(cwd)
    cwd = os.path.join(cwd,'conf')

    if(os.path.exists(cwd)):
        cwd = os.path.join(cwd,'httpd.conf')
        if(os.path.exists(cwd)):
            with open(cwd,'r') as rfile:
                lines = rfile.readlines()
            for line in lines:
                pattern = r'Hostname'
                if re.match(pattern,line):
                    host = line[10:-2]
                    break
            for line in lines:
                pattern = r'port'
                if re.match(pattern,line):
                    data = line.split()
                    port = int(data[2])
                    return port
                    rfile.close()
                    break
