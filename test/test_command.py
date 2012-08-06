#!/usr/bin/python

from pylatex import command
import sys


optl = ['opt1', 'opt2', 'opt3', 'opt4']
opts = dict(opt1 = 'true', opt2 = 'false', opt3 = 'string', opt4 = 5)
marg = 3
args = ['arg1', 'arg2', 'arg3']

n = '\\test{o}{a}'
o = '['+','.join([str(i[0])+'='+str(i[1]) for i in opts.items()])+']'
a = '{arg1}{arg2}{arg3}'

print 'testing command'

count = 0
def fail():
    sys.exit('\ttest {0} failed'.format(count))

def succeed():
    print '\ttest successful'

tc = command('test')
count += 1
if not (tc.get_str() == n.format(o='',a='')):
    fail()

tc = command('test', options = opts)
count += 1
if not (tc.get_str() == n.format(o=o,a='')):
    fail()

tc = command('test', arguments = args)
count += 1
if not (tc.get_str() == n.format(o='',a=a)):
    fail()

tc = command('test', options = opts, arguments = args)
count += 1
if not (tc.get_str() == n.format(o=o,a=a)):
    fail()

tc = command('test', options = dict(bla = 3, bli = 1), option_list = optl)
count += 1
if not (tc.get_str() == n.format(o='',a='')):
    fail()

tc = command('test', options = opts, option_list = optl)
count += 1
if not (tc.get_str() == n.format(o=o,a='')):
    fail()

tc = command('test', options = dict(bla = 3, bli = 1), arguments = args, option_list = optl)
count += 1
if not (tc.get_str() == n.format(o='',a=a)):
    fail()

tc = command('test', options = opts, arguments = args, option_list = optl)
count += 1
if not (tc.get_str() == n.format(o=o,a=a)):
    fail()

tc = command('test', options = dict(bla = 3, bli = 1), option_list = optl, max_args = marg)
count += 1
if not (tc.get_str() == n.format(o='',a='')):
    fail()

tc = command('test', options = opts, option_list = optl, max_args = marg)
count += 1
if not (tc.get_str() == n.format(o=o,a='')):
    fail()

tc = command('test', options = dict(bla = 3, bli = 1), arguments = args, option_list = optl, max_args = marg)
count += 1
if not (tc.get_str() == n.format(o='',a=a)):
    fail()

tc = command('test', options = opts, arguments = args, option_list = optl, max_args = marg)
count += 1
if not (tc.get_str() == n.format(o=o,a=a)):
    fail()

try:
    tc = command('test', arguments = args, max_args = 2)
    fail()
except IndexError:
    pass
except:
    fail()

succeed()
