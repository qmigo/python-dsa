class HashMap:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(0,self.MAX) ]

    def get_hash(self,key):
        t=0
        for char in key:
            t+= ord(char)

        return t % self.MAX
    
    def __setitem__ (self, key, value):
        t = self.get_hash(key)
        self.arr[t] = value
    
    def __getitem__ (self, key):
        t = self.get_hash(key)
        return self.arr[t]

    def __delitem__(self, key):
        t = self.get_hash(key)
        self.arr[t] = None
if __name__ == '__main__':
    hm = HashMap()

    hm['Ankur'] = 23
    hm['Madhav'] = 98
    hm['PP'] = 46

    print(hm['Ankur'], hm['Madhav'], hm['PP'])

    del hm['PP']

    print(hm['Ankur'], hm['Madhav'], hm['PP'])
    

