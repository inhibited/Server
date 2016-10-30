import os
import re

def dir():
    cwd = os.getcwd()
    #cwd = os.path.join(cwd,'..')
    cwd = os.path.abspath(cwd)
    cwd = os.path.join(cwd,'conf')
    if(os.path.exists(cwd)):
        cwd = os.path.join(cwd,'httpd.conf')
        if(os.path.exists(cwd)):
            with open(cwd,'r') as rfile:
                lines = rfile.readlines()
            for line in lines:
                pattern = r'ServerRoot'
                if re.match(pattern,line):
                    rdir = line[12:-3]
                    #print(rdir)
                    return rdir
