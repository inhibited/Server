
import sys
import datetime
import time
import threading
import traceback
import socketserver
from dnslib import *

class DomainName(str):
    def __getattribute__(self,item):
        return DomainName(item+'.'+self)
D = DomainName('backdated.com')
ip = '127.0.0.1'
ttl = 60*5
port = 5555
