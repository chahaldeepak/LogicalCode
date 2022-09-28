import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
data=pd.read_csv('ProProduction.csv')
# data=pd.DataFrame(pd.read_csv('ProProduction.csv'))
OnlyCols=data.columns.values

cmd=-1
years=list((data['Years']))
mobs=list((data['Mobiles']))
tabs=list((data['Tablets']))
laps=list((data['Laptops']))
tv=list((data['Android TV']))
proDt=dict()
for i in range(len(years)):
    proDt[years[i]]=list((mobs[i],tabs[i],laps[i],tv[i]))


def menu():
    print("\n..... Press 1 : To determine each product Production in all the years(2015-21).....")
    print("\n..... Press 2 : To determine the Production in a specific year.....")
    print("\n..... Press 3 : To determine the Production of two specified products.....")
    print("\n..... Press 4 : To determine the Production of all products within the given interval of years.....")
    print("\n..... Press 5 : To determine the total items produced per year.....")
    print("\n\t**** Press 0 : To terminate **** \n")

def eachItemTotalProduction():
    
    totMobs=sum(mobs)
    totTabs=sum(tabs)
    totLaps=sum(laps)
    totTvs=sum(tv)

    print("\n Total Mobiles : ",totMobs)
    print("\n Total Tablets : ",totTabs)
    print("\n Total Laptops : ",totLaps)
    print("\n Total Tv : ",totTvs)

def productionInSpecifyYear(yr): 
    m,t,l,T=proDt[yr]
    print(f"\n In {yr} Production of :\n")
    print("\t\tMobiles : ",m,"\n\t\tTabs : ",t,"\n\t\tLaptops : ",l,"\n\t\tTv : ",t)
    
    products=['Mobiles','Tablets','Laptops','Tv']
    plt.bar(products,proDt[yr],width=0.3,color='purple')
    plt.xlabel('Products')
    plt.ylabel('Production Quantity')
    plt.title(f'A2Z company {yr} production')
    plt.legend([proDt[yr]])
    plt.show()

def comparing2product(pd1,pd2):
    pd1list=list((data[pd1]))
    pd2list=list((data[pd2]))

    print(f"\n Total production of {pd1} and {pd2} ...\n")
    totpds=dict()

    for i in range(len(pd1list)):
        totpds[years[i]]=list((pd1list[i],pd2list[i]))

    print(f"\nYear\t\t{pd1}\t\t{pd2}\n")

    j=0
    for i in totpds.keys():
        print(i,totpds[i][j],totpds[i][j+1],sep='\t\t')
    
    plt.plot(years,pd1list,marker='P',markerfacecolor='w',markeredgecolor='black')
    plt.plot(years,pd2list,marker='*',markerfacecolor='w',markeredgecolor='black')
    plt.title(f'{pd1} and {pd2} Production')
    plt.xlabel('Years')
    plt.ylabel('Quantity')
    plt.legend([pd1,pd2])
    plt.grid(True)
    plt.show()

def yearRangeProduction(strtYear,endYear):
    x=years.index(strtYear)
    y=years.index(endYear)+1
    rYears=list()

    for i in range(strtYear, endYear+1):
        rYears.append(i)

    m1=list((mobs[x:y]))
    tb1=list((tabs[x:y]))
    lp=list((laps[x:y]))
    tv1=list((tv[x:y]))

    print("\nYear \t\t Products Production\n")

    j=0
    for i in rYears:
        print(i,"",m1[j],tb1[j],lp[j],tv1[j],sep="\t")
        j+=1

    plt.plot(rYears,m1,marker='o',markerfacecolor='w',markeredgecolor='black')
    plt.plot(rYears,tb1,marker='v',markerfacecolor='w',markeredgecolor='black')
    plt.plot(rYears,lp,marker='1',markeredgecolor='black')
    plt.plot(rYears,tv1,marker='x',markeredgecolor='black')

    plt.grid(True)
    cols=OnlyCols[1:]
    plt.legend(cols)
    plt.xlabel('Years')
    plt.ylabel('Items Quantity')
    plt.title('A2Z Company (Product Production Report)')
    plt.show()

def totalProductionPerYear():
    perYearprdc=list()
    for i in proDt.keys():
        add=sum(proDt[i])
        perYearprdc.append(add)
        
    print("\nYear\tTotal production of all products\n")

    for i in range(len(years)):
        print(years[i],perYearprdc[i],sep="\t\t")

    plt.bar(years,perYearprdc,color='orange',width=0.5)
    plt.xlabel('Years')
    plt.ylabel('Item Production')
    plt.title('Total Products per Year')
    plt.show()


menu()
while cmd!=0:
    cmd=int(input("\n***** Enter command : "))
    if cmd==0:
        exit()  

    elif cmd==1:
        print("\n Total production of each product....\n")
        eachItemTotalProduction()

    elif cmd==2:
        print("\n Which year production you want to see.\n")
        yr=int(input("\n Enter year : "))
        productionInSpecifyYear(yr)

    elif cmd==3:
        for i in range(1,len(OnlyCols)):
            print("\n\t Product %d : "%i,OnlyCols[i])
        print("\n Enter two Product names to compare their Production.\n")
        p1=input("\n Enter product 1 : ")
        p2=input("\n Enter product 2 : ")
        comparing2product(p1, p2)

    elif cmd==4:
        print("\n Enter a range of year to see the production data of all products.\n")
        strtYear=int(input("Enter starting year : "))
        endYear=int(input(" Enter end year : "))
        yearRangeProduction(strtYear,endYear)
        
    elif cmd==5:
        print("\n Total no. of products which are produced per year in company....\n")
        totalProductionPerYear()

    else:
        print("\n\t.....Enter the Valid Choice......\n")
        