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
        self.addr=cidr.split("/")[0]
        self.mask=int(cidr.split("/")[1])
        
    def getAddrBytes(self):
        '''
            @tests :
            >>> a = Ip("192.168.53.1/24")
            >>> a.getAddrBytes()
            [192, 168, 53, 1]
        '''
        addr = self.addr.split(".")
        int_addr=list(map(int,addr))
        return int_addr
    
    
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
        S1 = S[0:8]
        S2 = S[8:16]
        S3 = S[16:24]
        S4 = S[24:32]
        return [int(S1,2) , int(S2,2), int(S3,2), int(S4,2)]
    
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
        ip = self.getAddrBytes()
        mask = self.getMaskBytes()
        
        return [ip[i] & mask[i] for i in range (4)]
        
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
        ip = self.getAddrBytes()
        mask = self.getMaskBytes()
        
        return [ip[i] & (255-mask[i]) for i in range(4)]
    
    def __repr__(self):
        return f'{self.addr}/{self.mask}'
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = True)
