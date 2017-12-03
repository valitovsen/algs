class Heap:
    '''
    Heap(type='min') -> new heap data structure (min or max)

    Maintains heap property when performing insert/extract/heapify operations

    Methods:
    .insert(key) - insert key into data structure
    .extract() - extract min/max value key from heap structure
    .heapify(iterable) - bulk insert into data structure
    .__bubbleup__() - bubble up to maintain heap property
    .__bubbledown__() - bubble down to maintain heap property
    '''
    def __init__(self, extracttype='min'):
        if extracttype == 'min' or extracttype == 'max':
            self.type = extracttype
        else:
            raise ValueError('heap type must be min or max')
        self.keys = []

    def insert(self,entry):
        ".insert(key) - insert key into data structure"
        self.keys.append(entry)
        self.__bubbleup__()

    def extract(self):
        ".extract() - extract min/max value key from heap structure"
        try:
            res = self.keys.pop(0)
            if self.keys:
                self.__bubbledown__()
            return res
        except IndexError:
            print("can't extract from empty heap")
            pass

    def heapify(self,data):
        ".heapify(iterable) - bulk insert into data structure"
        for entry in data:
            self.insert(entry)

    def __bubbleup__(self):
        ".__bubbleup__() - bubble up to maintain heap property"
        i = len(self.keys)
        pa = int(i/2) if int(i/2)>0 else 1
        cond = {'min':1, 'max':-1}[self.type]
        while cond*self.keys[i-1] < cond*self.keys[pa-1]:
            self.keys[i-1],self.keys[pa-1] = self.keys[pa-1],self.keys[i-1]
            i = pa
            pa = int(i/2) if int(i/2)>0 else 1

    def __bubbledown__(self):
        ".__bubbledown__() - bubble down to maintain heap property"
        self.keys.insert(0,self.keys[-1])
        del self.keys[-1]
        cond = {'min':[min,1], 'max':[max,-1]}[self.type]
        length = len(self.keys)
        i = 1
        if 2*i < length:
            ch = {self.keys[2*i-1]:2*i, self.keys[2*i]:2*i+1}[cond[0](self.keys[2*i-1],self.keys[2*i])]
        elif 2*i == length:
            ch = 2*i
        else:
            ch = i
        while cond[1]*self.keys[i-1] > cond[1]*self.keys[ch-1]:
            self.keys[i-1],self.keys[ch-1] = self.keys[ch-1],self.keys[i-1]
            i = ch
            if 2*i < length:
                ch = {self.keys[2*i-1]:2*i, self.keys[2*i]:2*i+1}[cond[0](self.keys[2*i-1],self.keys[2*i])]
            elif 2*i == length:
                ch = 2*i
            else:
                ch = i
