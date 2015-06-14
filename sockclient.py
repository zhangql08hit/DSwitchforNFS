import socket
import time
import os
from multiprocessing import Process

HOST = ''
PORT = 51517

def try_ls_comm():
	print 'try ls command'
	os.system('ls /root/mountpoint/')
	print 'ls command done'

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))
	s.listen(1)
	while True:
		print 'Waiting for connection'
		conn, addr = s.accept()
		print 'Connected by', addr
		data = conn.recv(1024)
		if data == 'toarm':
			print 'Server switches to ARM'
			os.system('echo 5 > /proc/sys/fs/nfs/nfs_zql_control')
			p = Process(target=try_ls_comm)
			p.start()
			print 'NFS client is blocked ...'
			conn.sendall('block')
			sNotify = conn.recv(1024)
			if sNotify == 'success':
				print 'Start to switch NFS client'
				os.system('echo 168 > /proc/sys/fs/nfs/nfs_zql_control')
			else:
				print 'Server fails to switch disk'
			p.join()
		elif data = 'topc':
			print 'Server switches to PC'
			os.system('echo 5 > /proc/sys/fs/nfs/nfs_zql_control')
			p = Process(target=try_ls_comm)
			p.start()
			print 'NFS client is blocked ...'
			conn.sendall('block')
			sNotify = conn.recv(1024)
			if sNotify == 'success':
				print 'Start to switch NFS client'
				os.system('echo 169 > /proc/sys/fs/nfs/nfs_zql_control')
			else:
				print 'Server fails to switch disk'
			p.join()
		else:
			print 'Command Error!'
		conn.close()
