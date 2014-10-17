import sys
import subprocess
import yaml

stream = file('softwares.yaml', 'r')
softList = yaml.load(stream)

process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process.stdin.write('module load EasyBuild\n')

process.stdin.write('eb ' + ' '.join(softList['softwares']) + ' -D --robot\n')
process.stdin.write('echo $?\n')
out = ""
while True:
    out = process.stdout.readline()
    try:
        i = int(out)
    except ValueError:
        i = -1
    if i < 0:
        sys.stdout.write(out)
    else:
        if i == 0:
            sys.stdout.write('Operation successful\n')
        else:
            sys.stdout.write('Operation failed with return code ' + out)
        break
