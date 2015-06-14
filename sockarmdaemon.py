import socket
import time
import os

HOST = ''
PORT = 51518
PCHOST = '162.105.146.169'
PCPORT = 51519

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
	conn, addr = s.accept()
	print 'Connect by', addr
	data = conn.recv(1024)
	if data == 'pcswitch':
		print 'Switch disk to pc'
		pcs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		pcs.connect((PCHOST, PCPORT))
		pcs.sendall('start')
		os.system('echo 0 > /sys/class/gpio/gpio1_pc21/value')
		res = pcs.recv(1024)
		if res == 'done':
			print 'PC mounted disk and restarted service'
			conn.sendall('pcdone')
		else:
			print 'PC mount and restart error!'
			conn.sendall('error')
		pcs.close()

	elif data == 'armswitch':
		print 'Switch disk to arm'
		os.system('echo 1 > /sys/class/gpio/gpio1_pc21/value')
		os.system('./DiskMonitor.sh')
		os.system('service nfs-kernel-server restart')
		conn.sendall('armdone')
	else:
		print 'Switch command error!'
	conn.close()
