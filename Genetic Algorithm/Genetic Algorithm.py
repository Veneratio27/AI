import random

def isoperator(value):
    if value.isdigit() == False:
        for i in ["+","-","*","/"]:
            if value == i:
                return True
        return False
    else:
        return False

def isint(value):
    try:
        int(value)
        return True
    except:
        return False

class Codon():
    def __init__(self, value, crossover):
        self.mr = 0.001
        self.v = value
        self.cr = crossover

class Gene():
    def __init__(self, rangeset, length, crossrate):
        self.c = []
        for i in range(length):
            self.c.append(Codon(random.choice(rangeset), crossrate))

    def Decode(self, key, rangeset):
        self.index = 0
        for self.i in range(len(self.c)):
            self.index = self.index + self.c[self.i].v*len(rangeset)**(len(self.c)-self.i-1)
        if self.index >= len(key):
            return ""
        else:
            return key[self.index]

class Chromosome():
    def __init__(self, length, rangeset, glength, fitness):
        self.r = rangeset
        self.cr = 0.1
        self.f = fitness
        self.g = []
        for i in range(length):
            self.g.append(Gene(self.r, glength, self.cr/(length*glength)))
        

    def Decode(self, instructionset, key):
        self.val = []
        self.j = 0
        for self.i in range(len(self.g)):
            self.gval = self.g[self.i].Decode(key,self.r)
            self.check = eval(instructionset[self.j%len(instructionset)])
            if self.check:
                self.val.append(self.gval)
                self.j = self.j+1
        if len(self.val) != 0:
            self.val = ''.join(self.val)
            if self.val != "":
                try:
                    print self.val
                    return eval(self.val)
                except:
                    return ""
            else:
                return self.val
        else:
            return ""

class Populate():
    def __init__(self, population, instructionset, key, lengthrange, rangeset, glength):
        self.p = population
        self.iset = instructionset
        self.k = key
        self.c = []
        self.a = []
        for i in range(self.p):
            self.c.append(Chromosome(random.choice(lengthrange),rangeset,glength,1/self.p))
            
    def Decode(self, ichromosome, Answer):
        self.value = self.c[ichromosome].Decode(self.iset, self.k)
        if self.value == Answer:
            self.a.append(self.c.pop(ichromosome))
            self.p = self.p - 1
        else:
            self.c[ichromosome].f = (self.p*self.c[ichromosome].f)+self.p/abs(Answer-self.value)
        return self.value

    def Genetics(self):
        self.pop = []
        for self.i in range(self.p):
            for self.j in range(self.p*self.c[i].f):
                self.pop.append(self.i)
        self.choice1 = random.choice(self.pop)
        for self.i in range(self.pop.count(choice1)):
            self.pop.remove(choice1)
        self.choice2 = random.choice(self.pop)
        self.pop = []
        for self.i in range(self.choice1.g):
            for self.j in range(self.choice1.g[i].c):
                for self.l in range(self.choice1.g[i].c[j].cr*len(self.choice1.g)*len(self.choice1.g[i].c))
                    self.pop.append(self.i*len(self.choice1.g[i].c)+self.j)
        for self.i in range(self.choice2.g):
            for self.j in range(self.choice2.g[i].c):
                for self.l in range(self.choice2.g[i].c[j].cr*len(self.choice2.g)*len(self.choice2.g[i].c))
                    self.pop.append(self.i*len(self.choice2.g[i].c)+self.j)
        
        self.cross = random.choice(self.pop)
        

InsSet = ["isint(self.gval)","isoperator(self.gval)"]
mkey = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
pop = Populate(1000,InsSet, mkey, range(5), [0,1],4)
output = ""
for i in range(len(pop.c)):
    print "Chromosome " + str(i)
    output = ""
    for j in range(len(pop.c[i].g)):
        for k in pop.c[i].g[j].c:
            output = output + str(k.v)
        ouput = output + " "
    print output
    print pop.Decode(i)
