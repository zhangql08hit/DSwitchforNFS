import socket
import time
import os
import sys

HOST = '162.105.146.166'
PORT = 51517
ARMHOST = '162.105.146.168'
ARMPORT = 51518

if __name__ == '__main__':
	if sys.argc != 2:
		print 'Executing command error!'
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	
	print 'Sync cached data ...'
	os.system('sync')
	os.system('sync')
	print 'Sync cached data done'

	if sys.argv[1] == 'pc':
		print 'Start to switch to PC'
		s.sendall('topc')
		data = s.recv(1024)
		if data == 'block':
			print 'Client blocked IO'
			checkonflyio()
			os.system('sync')
			os.system('echo 0 > /sys/class/gpio/gpio1_pc21/value')
			print 'Send switch signal done'
		else:
			print 'Receive data error!'
	elif sys.argv[1] == 'arm':
		print 'Start to switch to ARM'
		s.sendall('toarm')
		data = s.recv(1024)
		if data == 'block':
			print 'Client blocked IO'
			checkonflyio()
			os.system('sync')
			#os.system('echo 0 > /sys/class/gpio/gpio1_pc21/value')
			print 'Build conn and send switch command to ARM'
			arms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			arms.connect((ARMHOST, ARMPORT))
			arms.send('switch')
			res = arms.recv(1024)
			if res == 'done':
				print 'ARM has switched disk'
			else:
				print 'ARM switch signal error'
			arms.close()
			print 'Send switch signal done'
		else:
			print 'Receive data error!'
	else:
		print 'Parameter error!'
	s.close()
