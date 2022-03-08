import yaml
import time
import threading
import datetime
from yaml.loader import SafeLoader
global f1 
f1 = open("logfile.txt", "a")
def flow():
    ##
    x=20
def timefunc(t):
    time.sleep(t)
def dataload(str):
    ##
    x=20

with open('Milestone1A.yaml') as f:
    data = list(yaml.load(f, Loader=SafeLoader))
    print(data)
k=data.keys()
if data[k[0]]["execution"]=="Sequential":
    f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]))
    act=data["Activities"].keys()
    for i in act:
        if i["type"]=="task":
            #list of dictionaries
            if i["Function"]=="TimeFunction":
                f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]),end="")
                f1.write(".",i," Entry")
                timefunc(int(i["Inputs"]["ExecutionTime"]))
                f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]),end="")
                f1.write(".",i," Exit")
            elif i["Function"]=="DataLoad":
                dataload()
        elif i["type"]=="flow":
            #
            flow(i)



    
