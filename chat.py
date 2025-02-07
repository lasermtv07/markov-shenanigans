#!/usr/bin/python3
import json
import random

#haha stolen
def wagner_fisher(s1,s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        s1, s2 = s2, s1
        len_s1, len_s2 = len_s2, len_s1

    current_row = range(len_s1 + 1)
    for i in range(1, len_s2 + 1):
        previous_row, current_row = current_row, [i] + [0] * len_s1
        for j in range(1, len_s1 + 1):
            add, delete, change = previous_row[j] + 1, current_row[j-1] + 1, previous_row[j-1]
            if s1[j-1] != s2[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[len_s1]
COUNT=1


ff=open("data.json","r")
f=ff.read()
ff.close()
f=json.loads(f)

while True:
    t=input(">>")
    t=t.split(" ")
    l=len(t)-COUNT
    q=t[l:]
    q=" ".join(q)
    
    best={'key':f[0]["key"],'dst':wagner_fisher(f[0]["key"],q)}
    for i in f:
        wag=wagner_fisher(i["key"],q)
        if wag<best['dst']:
            best['key']=i['key']
            best['dst']=wag
    ln=random.randint(10,25)
    o=""
    p=best['key']
    while ln>0:
        t=None
        for i in f:
            if i['key']==p:
                weights=[]
                states=[]
                for j in i['data']:
                    weights.append(j['probability'])
                    states.append(j['key'])
                r=random.choices(states,weights=weights,k=1)[0]
                o+=r
                p=r
                break
        ln-=1    
    print('<<'+o)