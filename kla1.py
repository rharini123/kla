import yaml
import time
import threading
import datetime
from yaml.loader import SafeLoader
global f1 
f1 = open("logfile.txt", "a")
class flow:
    def __init__(self,str):
        if str=="Sequential":
            #next child
            x=20
        else:
            #many children
            x=20

class tasks:
    def __init__(self,str,t):
        if str=="TimeFunction":
            time.sleep(t)
        else:
            #dataload
            x=20

class Engine(flow,tasks):
    def __init__(self):
        self.children = []
        flow.__init__(self)
        tasks.__init__(self)

with open('Milestone1A.yaml') as f:
    data = list(yaml.load(f, Loader=SafeLoader))
    print(data)
k=data.keys()

