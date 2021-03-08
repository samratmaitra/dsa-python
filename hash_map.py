class HashMap:
    """
    Hash Map Implementation w/ Chaining Approach.
    """

    def __init__(self, size:int=100) -> None:
        self.size = size
        self.arr = [[] for _ in range(self.size)]

    def gen_hash(self, key: str) -> int:
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.size
    
    def __setitem__(self, key:str, val) -> None:
        hash = self.gen_hash(key)
        elements = self.arr[hash]
        for element in elements:
            if element[0] == key:
                element[1] = val
                return
        self.arr[hash].append([key, val])

    def __getitem__(self, key:str):
        hash = self.gen_hash(key)
        elements = self.arr[hash]
        for element in elements:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self, key:str) -> None:
        hash = self.gen_hash(key)
        elements = self.arr[hash]
        for element in elements:
            if element[0] == key:
                element[1] = None

if __name__ == "__main__":
    map = HashMap()
    map['FEB 3'] = 4
    map['MAR 6'] = 10
    map['APR 3'] = 20
    print(map['APR 3'])
    del map['APR 3']
    print(map['APR 3'])
