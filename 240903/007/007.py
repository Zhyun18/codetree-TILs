class temp:
    def __init__(self, sc, mp,t):
        self.sc = 'secret code : ' + sc 
        self.mp = 'meeting point : ' + mp 
        self.t = 'time : ' + t 

element = temp(*tuple(input().split(' ')))
print(element.sc)
print(element.mp)
print(element.t)