from network import *
import shutil
import psutil

def check_disc(disc):
    du=shutil.disk_usage(disc)
    free_perc=du.free/du.total*100
    return free_perc>20
def cpu_usage():
    cpu_use=psutil.cpu_percent(1)
    return cpu_use< 75
if not check_disc('/') and cpu_usage():
    print("error!!")
elif(check_connectivity() and check_localhost()):
     print("Everything is working fine!!")
else:
    print("network failed")
   
