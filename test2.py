#!/usr/bin/python
# -*- coding: UTF-8 -*-

"this is a test module"

__author__ = 'DYJ'

import sys
import pdb
from collections import namedtuple

def test():
	args = sys.argv
	if len(args) == 1:
		print 'hello word,hello %s' %args[0]
	elif len(args) == 2:
		print "hello %s" %args[1]
	else:
		print "too many"

if __name__ == "__main__":
	test()


class Test_Students(object):
	"""docstring for Test_Stunents"""
	def __init__(self, score, name):
		super(Test_Students, self).__init__()
		self.__score = score
		self.__name = name

	def printlf(self):
		print 'score %i ' %self.score
		print 'name %i ' %self.name

	def getScore(self):
		return self.__score

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def setScore(self, score):
		self.__score = score


students = Test_Students(90,'name')
students.getName
#pdb.set_trace()
#print students.getName

"""
class ClassName(object):
	__solts__ = {'name','score'}
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
"""



		

def division(number):
	try:
		pass
	except Exception, e:
		raise
	else:
		pass
	finally:
		pass
	pass



Point = namedtuple("Point",["x","y"])
p = Point(1,2)
print p.x
print p.y