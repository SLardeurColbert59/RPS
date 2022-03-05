from ip import Ip

class Router:

    NUM = 0

    def __init__(self, L):
        self.L = L
        Router.NUM += 1
        self.name = 'Rt' + str(self.NUM)
        self.interface = list(L)
        self.neighbors = {}
        for n in range(len(self.interface)):
            self.neighbors['int-'+str(n)] = {'state':False, 'name':None, 'cost':0}

    def addInterface(self, ip):
        self.interface.append(ip)
        self.neighbors['int-'+str(len(self.interface)-1)] = {'state':False,'name':None,'cost':0}
        pass

    def getIpByInterface(self, name):
        return self.interface[int(name.split('int-')[-1])]
        pass

    def removeInterface(self, ip):
        self.interface.remove(ip)
        self.neighbors = {}
        for n in range(len(self.interface)):
            self.neighbors['int-'+str(n)] = {'state':False,'name':None,'cost':0}
        
    def __repr__(self):
        return f'{self.name}{self.interface}'
    
R1 = Router([Ip("10.53.1.2:8"), Ip("132.154.40.1/16")])
a = Router([])