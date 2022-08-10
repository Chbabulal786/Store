from __future__ import nested_scopes
from datetime import datetime
from optparse import Option

name = input("Enter Name:\n")
lists='''
Rice  Rs 50/kg
oil  Rs 1/liter
sugar  Rs 2/kg
salte  Rs 1/kg
panner  Rs 1/kg
chilli powder Rs 89/kg
choclate Rs 1pc
boost Rs 1bottle
maggi  Rs 1pc
'''
#declaration

price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]


items={
    'Rice':20,
    'oil':50,
    'sugar': 35,
    'salte':20,
    'panner':75,
    'choclate':25,
    'maggi': 10,
    'boost':56,
    'chilli powder': 35
}

option=int(input(" for list of items press 1: "))
if option==1:
    print(lists)
for i in range(len(items)):
    needs=int(input("if you want buy press 1 or 2 for exit:"))
    if needs==2:
        break
    if needs==1:
        item=input("Enter your items: ")
        quantity=int(input("Enter your Quantity: "))
        if item in items.keys():
            price= quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterd item not available")
    else:
        print("you enterd wrong number")

    int=input("can i bill items yes or no:")
    if int=='yes':
        pass
        if finalamount !=0:
            print(25*"=","Babulal Store",25*"=")
            print(25*" ","Viziyanagram")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Qunatity',3*" ", 'price')
            for i in range(len(pricelist)):
                print(i,8*' ',2*' ',ilist[i],12*' ',qlist[i],8*' ',plist[i])
            print(75*"-")
            print(50*" ",'Totalamount:', 'Rs',totalprice)
            print("gst amount",50*" ",2*' ','Rs',gst)
            print(75*"-")
            print(50*" ",'Fianlamount:', 'Rs',finalamount)
            print(75*"-")
            print(20*" ",'Thanks for visting')
            print(75*"-")
