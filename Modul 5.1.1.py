class StringVar:

    string = []

    def __init__(self, st = string):
        self.string = st
    
    def set(self, st):
        return st
    
    def get(self):
        return self.string

s = StringVar(input())
print(s.get())
print(s.set('World'))