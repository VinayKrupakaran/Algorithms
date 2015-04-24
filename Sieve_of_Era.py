#!/usr/bin/env python

#Implementation of the Sieve of Eratosthenes method to generate prime numbers upto and including 'n'
#Current implementation efficient only up to n = 10000
import sys

def sieve(n):
	flag = 0
	l = []
	p = 2
	#populate the list
	for i in xrange(2, n+1):
		l.append(i)
	#Sieve	
	while True:
		sys.stderr.write('{}\r' .format(p))
		for i in xrange(2, (n/p)+2):
			m = i * p
			if m > n:
				break
			if m in l:
				l[l.index(m)] = 0
		#Find the next prime
		for i in xrange(l.index(p)+1, len(l)):
			if l[i] != 0:
				p = l[i]
				flag = 0
				break
			else:
				flag = 1
		if flag == 1:
			break

	#print non-zero elements	
	for i in l:
		if i != 0:
			print i
