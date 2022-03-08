import yaml
import time
import threading
import datetime
from yaml.loader import SafeLoader
nodes=[]
global f1 
f1 = open("logfile.txt", "a")

class type():
   def __init__(self) -> None:
       pass  

class task(type):
    def __init__(self,funcn,ips):
        self.funcn=funcn
        self.ips=ips
        exetime=int(ips['ExecutionTime'])
    def run(self):
        f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]),end="")
        f1.write("."," Entry")
        time.sleep(self.exetime)
        f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]),end="")
        f1.write("."," Exit")

class timefunc(task):
    def __init__(self,str,t):
        time.sleep(t)
        exe()
class dataload(task):
    def __init__(self):
        ##
        super().__init__()
        exe()

class flow(task):
    children=[]
    def __init__(self,act):
        for i in act:
            if i["type"]=="task":
                obj=task(i['Function'],i['Inputs'])
                self.children.append(obj)
            elif i["type"]=="flow":
                flowobj=flow(act)
                self.children.append(flowobj)

    def run(self):
        for i in self.children:
            i.run()


class exe():
    #seq or conc
    def __init__(self,str):
        pass
class seq(exe,flow):
    def __init__(self,a_dict):
        for i in a_dict.keys():
            if i["Type"]=="Task":
                obj=task(i['Function'],i['Inputs'])
                root.children.append(obj)
                exe()
            elif i["type"]=="flow":
                flowobj=flow(i['Activities'])
                exe()
                if i['Execution']=="Sequential":
                    seqobj=seq(i['Activities'])
                else:
                    concobj=conc(i['Activities'])

class conc(exe):
    def __init__(self, str):
        super().__init__(str)

class Engine(exe):
    def __init__(self,exe1,act):
        self.children = []
        if exe1=="Sequential":
            seq.__init__(self,act)
        else:
            conc.__init__(self,act)
        #type.__init__(self,type1)

with open('Milestone1A.yaml') as f:
    data = dict(yaml.load(f, Loader=SafeLoader))
    print(data)

k=data.keys()
print(data['M1A_Workflow'])
root=Engine(data['M1A_Workflow']['Execution'],data['M1A_Workflow']['Activities'])
print(data['M1A_Workflow']['Activities'])
f1.write("{0} {1};".format(datetime.now().strftime("%Y-%m-%d %H:%M"),k[0]))
act=data["Activities"].keys()

#root.children=act

'''for i in act:
    if i["type"]=="task":
        obj=task(i['Function'],i['Inputs'])
        root.children.append(obj)
    elif i["type"]=="flow":
        if i['Execution']=="Sequential":
            seqobj=seq(i['Activities'])
        else:
            concobj=conc(i['Activities'])
'''
