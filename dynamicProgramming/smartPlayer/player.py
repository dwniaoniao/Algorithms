#!\usr\bin\python3
import sys

item = ['number','strength','type','worth','subitem']
baseItemNumber=int()    #基本装备数量
premiumItemNumber=int() #高级装备数量
itemNuber=int() #所有装备种类
gold = int()    #玩家拥有的金币数量
items=list()    #所有装备类型
itemsPurchased=list()   #用于记录符合最大力量值要求购买的所有装备
store = dict()  #用于记录基础装备的数量

def Subitems(i):
    #返回合成i所需的所有基础装备
    r = list()
    if IsBaseitem(i):
        r.append(i)
    else:
        for x in i['subitem']:
            r.extend(Subitems(x))
    return r
    pass

def Enough(i,store):
    #判断装备i是否存在至少一个
    if IsBaseitem(i):
        if store[i['number']] <= 0:
            return False
    else:
        l =store.copy()
        for x in Subitems(i):
            if l[x['number']] > 0:
                l[x['number']] -= 1
            else:
                return False
    return True
    pass

def IsBaseitem(i):
    #装备i是否为基础装备
    if i['type'] == 'basic':
        return True
    else:
        return False
    pass

def RemoveItem(i,store):
    #若i为基础装备，从store中简单地把它的数量减去1
    #若i为高级装备，从store中减去合成它所需的所有基础装备
    s=store.copy()
    if IsBaseitem(i):
        s[i['number']] -= 1
    else:
        for x in Subitems(i):
            s[x['number']] -= 1
    return s

def MaxStrength(gold):
    #具有数量为gold的金币，返回其所能购买到的装备力量之和的最大值
    #购买的装备记录在表ItemsPurchased中
    global store
    global itemsPurchased
    r=list()    #用于记录所需信息的表，表最后一项即有力量之和的最大值
    temp=list()
    r.append([0,{},store])
    def back(): #回溯操作求解购买的所有装备
        i = -1
        s = r[i][0]
        while s > 0:
            itemsPurchased.append(r[i][1]['number'])
            temp = r[i][1]['strength']
            temp2 = s
            s -= r[i][1]['strength']
            while r[i][0] != temp2 - temp: 
                i -= 1

    for g in range(1,gold+1):
        temp.clear()
        for i in items:
            if g>=i['worth'] and Enough(i,r[g-i['worth']][2]):
                temp.append([])
                temp[-1].append(r[g-i['worth']][0]+i['strength'])
                temp[-1].append(i)
                temp[-1].append(RemoveItem(i,r[g-i['worth']][2]))
        if not temp:    #temp为空，说明以价格g的金币无法购买任意的装备
            r.append([])
            r[-1]=r[-2]
            continue
        r.append([])    #填表
        r[-1].append(temp[0][0])
        r[-1].append(temp[0][1])
        r[-1].append(temp[0][2])
        for x in temp:
            if x[0] > r[-1][0]:
                r[-1][0] = x[0]
                r[-1][1] = x[1]
                r[-1][2] = x[2]
    back()  #回溯操作求解购买的所有装备
    return r[-1][0] #返回表最后一项记录的最大力量值

f = open('player.txt')
temp = f.readlines()
f.close()
l = list()
for x in temp:
    l.append(x.split())

itemNuber = int(l[0][0])
baseItemNumber = int(l[0][1])
premiumItemNumber = int(l[0][2])
gold = int(l[0][3])

lb = l[1:baseItemNumber+1]
for x in lb:    #基础装备
    vnumber = int(x[0])
    vstrength = int(x[1])
    vworth = int(x[2])
    amount = int(x[3])
    vitem = {'number':vnumber,'strength':vstrength,'type':'basic','worth':vworth,'subitem':[]}
    store[vnumber] = amount
    items.append(vitem)

lp = l[baseItemNumber+1:]
for x in lp:    #高级装备
    vnumber = int(x[0])
    vstrength = int(x[-1])
    vworth = 0
    vsubitem = list()
    for y in x[1:-1]:
        for z in items:
            if int(y) == z['number']:
                vstrength += z['strength']
                vworth += z['worth']
                vsubitem.append(z)
                break
    vitem = {'number':vnumber,'strength':vstrength,'type':'premium','worth':vworth,'subitem':vsubitem}
    items.append(vitem)

print(MaxStrength(gold))
print(itemsPurchased)
