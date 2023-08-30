#!/usr/bin/env python
# coding: utf-8

# In[1]:


class coffee:
    def __init__(self,water,milk,coffee,money):#400,150,80,0
        self.water=water
        self.milk=milk
        self.coffee=coffee
        self.money=money
    def report(self):
        print("*"*80)
        ti="REPORT"
        print(ti.center(80,"*"))
        print("*"*80)
        print("Water:",self.water)
        print("Milk:",self.milk)
        print("Coffee:",self.coffee)
        print("Money:",self.money)
        print("*"*80)

    def espresso(self):
        print("*"*80)
        ti="ESPRESSO"
        print(ti.center(80,"*"))
        print("*"*80)
        if self.water>150 and self.milk>50 and self.coffee>25:
            qu=int(input("Enter the number of quartes:"))
            di=int(input("Enter the number of dimes:"))
            ni=int(input("Enter the number of nickles:"))
            pe=int(input("Enter the number of pennies:"))
            coins=(0.25*qu)+(0.10*di)+(0.05*ni)+(0.01*pe)
            print("coins:",coins)
            
            if coins>5:
                new=round(coins-5)
                coins=coins-new
                print("Change:",new)
                self.water=self.water-150
                self.milk=self.milk-50
                self.coffee=self.coffee-25
                self.money=self.money+coins
            elif coins<5:
                print("Sorry! there is not enough money")
            else:
                self.water=self.water-150
                self.milk=self.milk-50
                self.coffee=self.coffee-25 
                self.money=self.money+coins

        else:
            print("Sorry! there is not enough water or milk or coffee powder")

    def latte(self):
        print("*"*80)
        ti="LATTE"
        print(ti.center(80,"*"))
        print("*"*80)
        if self.water>200 and self.milk>100 and self.coffee>50:
            qu=int(input("Enter the number of quartes:"))
            di=int(input("Enter the number of dimes:"))
            ni=int(input("Enter the number of nickles:"))
            pe=int(input("Enter the number of pennies:"))
            coins=(0.25*qu)+(0.10*di)+(0.05*ni)+(0.01*pe)
            print("coins:",coins)
            
            if coins>7:
                new=round(coins-7)
                coins=coins-new
                print("Change:",new)
                self.water=self.water-200
                self.milk=self.milk-100
                self.coffee=self.coffee-50
                self.money=self.money+coins
            elif coins<7:
                print("Sorry! there is not enough money")
            else:
                self.water=self.water-200
                self.milk=self.milk-100
                self.coffee=self.coffee-50 
                self.money=self.money+coins

        else:
            print("Sorry! there is not enough water or milk or coffee powder")

    def cappuccino(self):
        print("*"*80)
        ti="CAPPUCCINO"
        print(ti.center(80,"*"))
        print("*"*80)
        if self.water>100 and self.milk>40 and self.coffee>20:
            qu=int(input("Enter the number of quartes:"))
            di=int(input("Enter the number of dimes:"))
            ni=int(input("Enter the number of nickles:"))
            pe=int(input("Enter the number of pennies:"))
            coins=(0.25*qu)+(0.10*di)+(0.05*ni)+(0.01*pe)
            print("coins:",coins)
            
            if coins>3:
                new=round(coins-3)
                coins=coins-new
                print("Change:",new)
                self.water=self.water-100
                self.milk=self.milk-40
                self.coffee=self.coffee-20
                self.money=self.money+coins
            elif coins<3:
                print("Sorry! there is not enough money")
            else:
                self.water=self.water-100
                self.milk=self.milk-40
                self.coffee=self.coffee-20 
                self.money=self.money+coins

        else:
            print("Sorry! there is not enough water or milk or coffee powder")

            
print("*"*80)
ti="WELCOME TO COFFEE TODAY SHOP"
print(ti.center(80,"*"))
print("*"*80)
while True:
    msg="Options\t1.Report\t2.espresso\t3.Latte\t\t4.cappuccino\t5.Exist"
    print(msg)
    ch=int(input("What would you like?:"))
    if ch==1:
        cu=coffee(400,150,80,0)
        cu.report()
    elif ch==2:
        cu.espresso()
        cu.report()
    elif ch==3:
        cu.latte()
        cu.report()
    elif ch==4:
        cu.cappuccino()
        cu.report()
    elif ch==5:
        quit()
        break
        


# In[ ]:




