
class Family:
    def __init__(self, first, last, parent, gen, male):
        self.first = first
        self.last = last
        self.parent = parent
        self.gen = 0
        self.male = True
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

       

Ross = Family('Ross', 'King', 'Sharon', 3, True)
Bret = Family('Bret', 'Champ', 'Sharon', 3, True)
Kelly = Family('Kelly', 'Goode', 'Sharon', 3, False)

Lee = Family('Lee', 'Bret', 'Phil', 3, True )

print(Ross.fullName())  

#def checkRel(*args, **kwargs:
 #   print(args)
#    print(kwargs)

def chekFam(one, two):
    if one.parent == two.parent:
        print('Siblings')
    elif one.gen == two.gen and one.parent != two.parent:
        print('Cousins')
        
    

chekFam(Ross, Lee)



