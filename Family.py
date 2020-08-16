
class Family:
    def __init__(self, first, last, parent, grand, great, gen, male):
        self.first = first
        self.last = last
        self.parent = parent
        self.grand = grand
        self.great = great
        self.gen = gen
        self.male = male
    
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

Kitty = Family('Kitty', 'Blank', 'A.Foster', 'Unknown', 'Unknown3', 1, False)    
Sharon = Family('Sharon', 'Blank', 'Kitty', 'A_Foster', 'Unknown', 2, False)
Ross = Family('Ross', 'King', 'Sharon', 'Kitty', 'Unknown', 3, True)
Bret = Family('Bret', 'Blank', 'Sharon', 'Kitty', 'Unknown', 3, True)
Kelly = Family('Kelly', 'Blank', 'Sharon', 'Kitty', 'Unknown',3, False)
Harrison = Family('Harrison', 'Blank', 'Bret', 'Sharon', 'Kitty', 4, True)
Remy = Family('Remy', 'Blank', 'Kelly', 'Sharon', 'Kitty', 4, False)
Poppy = Family('Poppy', 'Blank', 'Kelly', 'Sharon', 'Kitty', 4, False)
Ellis = Family('Ellis', 'Blank', 'Kelly', 'Sharon','Kitty', 4, False)
Willow = Family('Willow', 'Blank', 'Remy', 'Kelly', 'Sharon', 5, False)
Taj = Family('Taj', 'Blank', 'Remy', 'Kelly', 'Sharon', 5, True)

Phil = Family('Phil', 'Blank', 'Kitty', 'A_Foster', 'Unknown2', 2, True)
Lee = Family('Lee', 'Blank', 'Phil','Kitty',  'Unknown', 3, True )
James = Family('James', 'Blank', 'Phil', 'Kitty',  'Unknown', 3, True)
Robbie = Family('Robbie', 'Blank', 'Phil', 'Kitty',  'Unknown', 3, True)
Jess = Family('Jess', 'Blank', 'Phil', 'Kitty',  'Unknown', 3, False)

Mick = Family('Mick', 'Blank', 'Kitty', 'A.Foster', 'Unknown2', 2, True)
Lou = Family('Louise', 'Blank', 'Mick', 'Kitty', 'A.Foster', 3, False)
Kev = Family('Kevin', 'Blank', 'Kitty', 'A.Foster', 'Unkown2', 2, True)
Dan = Family('Daniel', 'Blank', 'Kev', 'Kitty', 'A.Foster', 3, True)
Sian = Family('Sian', 'Blank', 'Kev', 'Kitty', 'A.Foster', 3, False)


def chekFam(one, two):
    if one.parent == two.parent and two.male == True:
        print('Brother')
    elif one.parent == two.parent and two.male == False:
            print('Sister')
    elif one.gen == two.gen and one.parent != two.parent:
        print('Cousin')
    elif one.first == two.parent and one.male == True:
        print('Son')
    elif one.parent == two.first and one.male != True:
        print('Daughter')
    elif one.grand == two.parent and two.first != one.parent and two.male == True:
        print('Uncle')
    elif one.grand == two.parent and two.male == False and  two.first != one.parent and two.male != True:
        print('Aunt')
    elif one.parent == two.grand and two.male == True:
         print('Nephew')
    elif one.parent == two.grand and two.male != True:
        print('Niece')
    elif one.grand == two.great:
        print('Second cousin')
    elif one.parent == two.first and two.male != True:
        print('Mum')
    elif one.first == two.parent and one.male == True:
        print('Dad')
    elif one.grand == two.first and two.male == False:
        print('Nan')
    elif one.grand == two.first and two.male == True:
        print('Grand Dad')
    elif one.first == two.grand and two.male == True:
        print('Grandson')
    elif one.first == two.grand and two.male == False:
        print('Grand Daughter')
    elif one.parent == two.great and two.male == False:
        print('Great Neice')
    elif one.parent == two.great and two.male == True:
        print('Great Nephew')
    elif one.great == two.first and two.first != True:
        print('Great Grand Mother')
    elif one.first == two.great and two.great != True:
        print('Great Grand Daughter')


chekFam(Kitty, Remy)   
  





