""" this program is based on the greedy approach in which a 
    theif having a bag of a capacity and there are few bags
    filled and having their own different weight and profit.
    Now, the theif will steal from those filled bags in such
    a way such that he get maximum profit in minimum weight.
    In the end, program will also display the total profit taken 
    by theif."""


def greedyTheif(totBags,theifBagCap):
    bags=dict()
    kgPftDt=dict()
    kgpftLt=list()
    for i in range (totBags):
        proWtLt=[]
        profit=float(input("\nProfit of Bag %d : " %(i+1)))
        weight=float(input("Weight of Bag %d : "%(i+1)))
        perKgPft=profit/weight
        proWtLt.append(profit)
        proWtLt.append(weight)
        kgpftLt.append(perKgPft)
        bags[i+1]=proWtLt
        kgPftDt[perKgPft]=i+1
    kgpftLt.sort()
    kgpftLt.reverse()


    updTotPft=list()
    for i in kgpftLt:
        bagkey=kgPftDt[i]
        bagWt=bags.get(bagkey)[1]
        mx=max(bagWt,theifBagCap)
        mn=min(bagWt,theifBagCap)
        theifBagCap=theifBagCap-bagWt
        
        print()
        if (mx >=0 and mn>=0):
            print("Max profit bag : ",bagkey," and taken weight : ",mn)
            totWtPft=mn*i
            updTotPft.append(totWtPft)
        else:
            print("Max profit bag : ",bagkey," and taken weight : ",0)
    print("\nTotal profit stolen by theif : ",sum(updTotPft))
    print("\n\n {bag no. : [bag profit, bag weight]}\n",bags)
    print("\n {bag per kg profit : bag no.}\n",kgPftDt)
    print("\n [bag per kg profit]\n",kgpftLt)
    print("\n [total profit of weight taken by theif]\n",updTotPft)
    print()

totBags=int(input("\nEnter total bags : "))
theifBagCap=float(input("Theif bag capacity : "))
greedyTheif(totBags, theifBagCap)