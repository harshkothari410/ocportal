import os

def output(fileurl, time, inputfile=None):
	command0 = 'chmod 777 ' + fileurl

	if inputfile:
		command1 = 'timeout ' + time + ' python ' + fileurl  + ' 2>&1 < ' + inputfile
	else:
		# command1 = 'timeout ' + time + ' python ' + fileurl  + ' 2>&1'
		command1 = 'python ' + fileurl  + ' 2>&1'

	c1 = os.popen(command0)

	c2 = os.popen(command1)

	print c2
	return c2