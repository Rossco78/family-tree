
class Family:
    def __init__(self, first, last, parent, grand, gen, male):
        self.first = first
        self.last = last
        self.parent = parent
        self.grand = grand
        self.gen = gen
        self.male = male
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

       
Sharon = Family('Sharon', 'Brett', 'Kitty', 'Unknown', 2, False)
Ross = Family('Ross', 'King', 'Sharon', 'Kitty', 3, True)
Bret = Family('Bret', 'Champ', 'Sharon', 'Kitty', 3, True)
Kelly = Family('Kelly', 'Goode', 'Sharon', 'Kitty', 3, False)
Harrison = Family('Harrison', 'Champ', 'Bret', 'Sharon', 4, True)

Phil = Family('Phil', 'Brett', 'Kitty', 'Unknown', 2, True)
Lee = Family('Lee', 'Bret', 'Phil','Kitty', 3, True )

print(Ross.fullName())  

#def checkRel(*args, **kwargs:
 #   print(args)
#    print(kwargs)

def chekFam(one, two):
    if one.parent == two.parent and two.male == True:
        print('Brother')
    elif one.parent == two.parent and two.male == False:
            print('Sister')
    elif one.gen == two.gen and one.parent != two.parent:
        print('Cousins')
    elif one.parent == two.first and one.male == True:
        print('Son')
    elif one.parent == two.first and one.male != True:
        print('Daughter')
    elif one.grand == two.parent and two.male == True:
        print('Uncle')
    elif one.grand == two.parent and two.male == False:
        print('Aunt')
    elif one.parent == two.grand and one.male == True:
         print('Nephew')
    elif one.parent == two.grand and one.male != True:
        print('Niece')
    
    
        
print(Phil.fullName())
chekFam(Ross, Phil)
chekFam(Ross, Lee)
chekFam(Ross, Kelly)
chekFam(Ross, Sharon)
chekFam(Kelly, Sharon)
chekFam(Kelly, Bret)
chekFam(Harrison, Kelly)
chekFam(Phil, Ross)



