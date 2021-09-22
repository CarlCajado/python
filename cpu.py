import platform
import psutil
def os():
    return platform.uname().system
def osVersion():
    return platform.uname().version
def frequencia():
    return psutil.cpu_freq().current/1000
def frequenciaMX():
    return psutil.cpu_freq().max/1000
def frequenciaMin():
    return psutil.cpu_freq().min/1000
def cores():
    return psutil.cpu_count()
def phycores():
    return psutil.cpu_count(logical=False)
def  memory():
    return psutil.virtual_memory()
def swap():
    return psutil.swap_memory()
def ps():
    return platform.processor()
def vm ():
    return psutil.virtual_memory().total/(1024000000)
def temp ():
    return psutil.sensors_battery()
def test():
    return psutil.disk_usage('/')
