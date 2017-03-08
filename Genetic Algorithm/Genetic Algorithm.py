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
        self.glength = length
        self.c = []
        for self.i in range(length):
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
        self.GeneLength = glength
        self.g = []
        self.value = 0
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

    def totallen(self):
        self.val = 0
        for i in range(len(self.g)):
            self.val = self.val + len(self.g[i].c)
        return self.val

    def split(self, Index):
        self.newGene = Gene([0,1],self.totallen()-Index,0.1)
        for i in range(Index, self.totallen()):
            self.newGene[i-Index] = self.g[math.floor(Index/len(self.g))].c.pop(Index%len(self.g[math.floor(Index/len(self.g))]))
        for i in range(len(self.g)):
            if i >= Index/len(self.g):
                self.g.pop(i)
        return self.newGene

    def append(self, newGene):
        bnone = True
        for i in range(len(self.g)):
            if self.g[i].glength > len(self.g[i].c):
                bnone = False
                break
        if bnone == False:
            for i in range(len(self.g[i].c),self.g[i].glength):
                self.g[i].c.append(newGene.c.pop(0))
        self.Temp = Gene([0,1], self.GeneLength, 0.1)
        while len(newGene.c) > 0:
            if len(newGene.c) >= len(self.Temp.c):
                for i in range(len(self.Temp.c)):
                    self.Temp.c[i] = newGene.c.pop(0)
            else:
                self.Temp = newGene
            self.g.append(self.Temp)

class Populate():
    def __init__(self, population, instructionset, key, lengthrange, rangeset, glength):
        self.p = population
        self.iset = instructionset
        self.k = key
        self.rangeset = rangeset
        self.c = []
        self.a = []
        for i in range(self.p):
            self.c.append(Chromosome(random.choice(lengthrange),rangeset,glength,1/self.p))
            
    def Decode(self, ichromosome, Answer):
        self.value = self.c[ichromosome].Decode(self.iset, self.k)
        if self.value != "":
            if self.value == Answer:
                self.a.append(self.c.pop(ichromosome))
                self.p = self.p - 1
            self.c[ichromosome].value = self.value
            return self.value
        else:
            self.c.pop(ichromosome)
            self.p = self.p - 1

    def Genetics(self):
        self.pop = []
        print "Genetics - populate for Choice1"
        for self.i in range(self.p):
            print self.p*self.c[self.i].f
            for self.j in range(int(self.p*self.c[self.i].f)):
                self.pop.append(self.i)
        self.choice1 = random.choice(self.pop)
        print "Genetics - Choice1 - " + str(self.choice1)
        print "Genetics - remove population for Choice1 - count " + str(self.pop.count(self.choice1))
        self.pop = []
        for self.i in range(self.p):
            if self.i != self.choice1:
                for self.j in range(int(self.p*self.c[self.i].f)):
                    self.pop.append(self.i)
        self.choice2 = random.choice(self.pop)
        print "Genetics - Choice1 - " + str(self.choice1)
        self.pop = []
        self.length1 = 0
        self.length2 = 0
        print "Genetics - populate Codons"
        for i in range(len(self.c[self.choice1].g)):
            for j in range(len(self.c[self.choice1].g[i].c)):
                for self.l in range(int((self.c[self.choice1].g[i].c[j].cr)*(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
                    self.pop.append(self.i*len(self.c[self.choice1].g[i].c)+self.j)
                    self.length1 = self.length1 + 1
        print str(len(self.pop))
        for i in range(len(self.c[self.choice2].g)):
            for j in range(len(self.c[self.choice2].g[i].c)):
                for self.l in range(int((self.c[self.choice2].g[i].c[j].cr)*(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
                    self.pop.append(self.i*len(self.c[self.choice2].g[i].c)+self.j)
                    self.length2 = self.length2 + 1
        print str(len(self.pop))
        for self.i in range(int((self.length1+self.length2)-(self.c[self.choice1].totallen()+self.c[self.choice2].totallen())*100)):
            self.pop.append("")
        print str(len(self.pop))
        self.cross = random.choice(range(len(self.pop)))-1
        print "Genetics - cross - " + str(self.cross)
        print "Genetics - Perform Swap"
        if self.pop[self.cross] <> "":
            if self.cross+1 <= self.length1:
                self.Temp = self.c[self.choice1].split(self.pop[self.cross])
                self.Temp2 = []
                if self.pop[self.cross] <= self.c[self.choice2].totallen():
                    self.Temp2 = self.c[self.choice2].split(self.pop[self.cross])
                if len(self.Temp2) > 0 : self.c[self.choice1].append(self.Temp2)
                self.c[self.choice2].append(self.Temp)
            elif self.cross+1 > self.length1:
                self.Temp = self.c[self.choice2].split(self.pop[self.cross])
                self.Temp2 = []
                if self.pop[self.cross] <= self.c[self.choice1].totallen():
                    self.Temp2 = self.c[self.choice1].split(self.pop[self.cross])
                if len(self.Temp2) > 0 : self.c[self.choice2].append(self.Temp2)
                self.c[self.choice1].append(self.Temp)
        print "Genetics - Mutation"
        for i in range(len(self.c[self.choice1].g)):
            for j in range(len(self.c[self.choice1].g[i].c)):
                print [k for k in self.rangeset if k != self.c[self.choice1].g[i].c[j].v]
                self.Temp = [k for k in self.rangeset if k != self.c[self.choice1].g[i].c[j].v]
                self.pop = []
                for k in range(int(self.c[self.choice1].g[i].c[j].mr*1000)):
                    self.pop.append(random.choice(self.Temp))
                for k in range(int(1000-self.c[self.choice1].g[i].c[j].mr)):
                    self.pop.append("")
                self.Choicemr = random.choice(self.pop)
                if self.Choicemr != "":
                    self.c[self.choice1].g[i].c[j].v = self.Choicemr
        for i in range(len(self.c[self.choice2].g)):
            for j in range(len(self.c[self.choice2].g[i].c)):
                self.Temp = [k for k in self.rangeset if k != self.c[self.choice2].g[i].c[j].v]
                self.pop = []
                for k in range(int(self.c[self.choice2].g[i].c[j].mr*1000)):
                    self.pop.append(random.choice(self.Temp))
                for k in range(int(1000-self.c[self.choice2].g[i].c[j].mr)):
                    self.pop.append("")
                self.Choicemr = random.choice(self.pop)
                if self.Choicemr != "":
                    self.c[self.choice1].g[i].c[j].v = self.Choicemr
                

InsSet = ["isint(self.gval)","isoperator(self.gval)"]
mkey = ["0","1","2","3","4","5","6","7","8","9","+","-","*","/"]
pop = Populate(1000,InsSet, mkey, range(5), [0,1],4)
output = ""
while len(pop.c) > 1:
    oldpop = len(pop.c)
    for i in range(len(pop.c)):
        realpop = len(pop.c)
        print "Chromosome " + str(i) + " Population is " + str(len(pop.c))
        output = ""
        for j in pop.c[i-(oldpop-realpop)].g:
            for k in j.c:
                output = output + str(k.v)
            ouput = output + " "
        print output + " Population is " + str(len(pop.c))
        print pop.Decode(i-(oldpop-realpop),24)
        print "Population is " + str(len(pop.c))
    for i in range(len(pop.c)):
        pop.c[i].f = ((pop.p*pop.c[i].f)+abs(24.0-pop.c[i].value))/pop.p
    pop.Genetics()
for i in pop.a:
    print i
