class Ip:
    
    def __init__(self, cidr):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.addr
            '192.168.53.1'
            >>> a .mask
            24
        '''  
        pass
        
    def getAddrBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getAddrBytes()
            [192, 168, 53, 1]
        '''
        pass
    
    def getMaskBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getMaskBytes()
            [255, 255, 255, 0]
            >>> b = Ip("192.168.124.13/18")
            >>> b.getMaskBytes()
            [255, 255, 192, 0]
        '''
        pass
    
    def getNetworkBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getNetworkBytes()
            [192, 168, 53, 0]
            >>> b = Ip("91.198.174.2/19")
            >>> b.getNetworkBytes()
            [91, 198, 160, 0]
        '''
        pass
        
    def getHostBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getHostBytes()
            [0, 0, 0, 1]
            >>> b = Ip("91.198.174.2/19")
            >>> b.getHostBytes()
            [0, 0, 14, 2]
        '''
        pass
    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
