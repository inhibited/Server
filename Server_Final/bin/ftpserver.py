import pyftplib
from pyftpdlib.handlers import FTPHandler
address = ("0.0.0.0", 21)
server = servers.FTPServer(address, FTPHandler)
server.serve_forever()
