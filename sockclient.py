import socket
import time
import os

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print 'Connected by', addr
	data = conn.recv(1024)
	if data == 'toarm':
		print 'Server switches to ARM'
		os.system('echo 5 > /proc/sys/fs/nfs/nfs_zql_control')
		print 'NFS client is blocked ...'
		conn.sendall('block')
		sNotify = conn.recv(1024)
		if sNotify == 'success':
			print 'Start to switch NFS client'
			os.system('echo 168 > /proc/sys/fs/nfs/nfs_zql_control')
		else:
			print 'Server fails to switch disk'
	elif data = 'topc':
		print 'Server switches to PC'
		os.system('echo 5 > /proc/sys/fs/nfs/nfs_zql_control')
		print 'NFS client is blocked ...'
		conn.sendall('block')
		sNotify = conn.recv(1024)
		if sNotify == 'success':
			print 'Start to switch NFS client'
			os.system('echo 169 > /proc/sys/fs/nfs/nfs_zql_control')
		else:
			print 'Server fails to switch disk'
	else:
		print 'Command Error!'
	conn.close()
