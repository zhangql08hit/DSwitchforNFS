import socket
import time
import os

HOST = ''
PORT = 51519
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print 'Connect by', addr
	data = conn.recv(1024)
	if data == 'start':
		print 'Start to monitor disk and resume service'
		os.system('./DiskMonitor.sh')
		print 'Mount disk done'
		os.system('service nfs restart')
		print 'NFS restart done'
		conn.sendall('done')
	else:
		print 'recv error!'
	conn.close()
