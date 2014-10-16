import yaml
import subprocess

stream = file('modules.yaml', 'r')
mouduleList = yaml.load(stream)

for module in moduleList:
    subprocess.call("eb" + module, shell=True)
