#!/usr/bin/env python
from socket import * 

if __name__ == '__main__':
	target = raw_input('IP: ')
	targetIP = gethostbyname(target)

	#scan reserved ports
	for i in range(20, 1025):
		s = socket(AF_INET, SOCK_STREAM)

		result = s.connect_ex((targetIP, i))

		if(result == 0) :
			print 'Port %d:' % (i,)
s.close()
