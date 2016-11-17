import os
import subprocess

# p = subprocess.Popen('python ../hello.py 2>&1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

stream = os.popen("python ../hello.py 2>&1")

print stream.read()
# print p.stdout.read()
# print p.stdout.read()