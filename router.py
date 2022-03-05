from ip import Ip

class Router:
    
    NUM = 0
    def __init__(self, L):
        Router.NUM += 1
        self.name = f'Rt{Router.NUM}'
        self.interfaces = list(L)
    
    def addInterface(self, ip):
        pass
        
    def getIpByInterface(self, name):
        pass
    
    def removeInterface(self, ip):
        pass