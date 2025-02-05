#!/usr/bin/python3
import math
import random

#an excerpt from collection of lovecrafitan horror
FILE='text.txt'
COUNT=2
LEN=420

#class
class state:
    def __init__(self,key):
        self.key=key
        self.states=[]
        isMarkov=False
    def addState(self,state):
        addNew=True
        for i in self.states:
            if i[1]==state:
                i[0]+=1
                addNew=False
        if addNew:
            self.states.append([1,state])
    def markovify(self):
        count=0
        for i in self.states:
            count+=i[0]
        for i in range(len(self.states)):
            t=self.states[i]
            self.states[i][0]=t[0]/count
    def randState(self):
        weights=[]
        states=[]
        for i in self.states:
            weights.append(i[0])
            states.append(i[1])
        return random.choices(states,weights=weights,k=1)[0]

#open and preprocess file
with open(FILE,'r') as i:
    f=(i.read()).replace("\n"," ")
for i in range(0,26):
    f=f.replace(chr(65+i),chr(97+i))
for i in "[]\"\'!@#$%^&*(){}?/;`~:<>+-\\":
    f=f.replace(i,"")
f=f.replace(". "," . ")
f=f.replace(", "," , ")

#generate state space
space=[]
f=f.split(" ")
i=0
while(i<len(f)-COUNT-1):
    tok=""
    for j in range(0,COUNT):
        tok+=f[i]+" "
        i+=1
    nxt=""
    for j in range(0,COUNT):
        nxt+=f[i+j]+" "
    addNew=True
    for j in space:
        if j.key==tok:
            j.addState(nxt)
            addNew=False
    if addNew:
        a=state(tok)
        a.addState(nxt)
        space.append(a)

for i in space:
    i.markovify()

#generate
r=random.choice(space)
l=1
o=""
while(l<LEN):
    t=r.randState()
    for i in space:
        if i.key==t:
            r=i
    o+=t
    l+=1

#final processing
o=o.replace(" , ",", ")
o=o.split(" . ")
for i in range(len(o)):
    t=list(o[i])
    t[0]=t[0].upper()
    o[i]="".join(t)
o=". ".join(o)
print(o)