import subprocess

subprocess.call("inconfig eth0 down", shell=True)
subprocess.call("inconfig eth0 hw ether 00:11:22:33:44:55", shell=True)
subprocess.call("inconfig eth0 up", shell=True)