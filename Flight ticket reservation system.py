#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Flight ticket reservation system:

# Each passenger details store -booking
booking=[]

#Intro:
print("*"*80)
st="WELCOME TO AIR INDIA"
print(st.center(80,'*'))
print("*"*80)

msg="""1.Ticketing booking 
2.Cancel ticket
3.Available seats
4.Exist"""
print(msg)

print("*"*80)

#Original Rate:
original={
    "Bprice":5000,
    "Eprice":3000,
    "non_veg":100,
    "veg":80
}

#Each flight original seats
flight1={ #101
    "Bseats":25,
    "Eseats":25
}
flight2={ #102
    "Bseats":25,
    "Eseats":25
}

#Seats details:
def seats():
    print("*"*80)
    se="AVAIABLE OF SEATS"
    print(se.center(80,"-"))
    print("*"*80)
    print("Flight 101 for business class:",flight1["Bseats"])
    print("Flight 101 for economy class:",flight1["Eseats"])
    print("Flight 102 for business class:",flight2["Bseats"])
    print("Flight 102 for economy class:",flight2["Eseats"])
    print("*"*80)

#Business class details:
def businessCl():
    print("*"*80)
    bu="BUSINESS CLASS"
    print(bu.center(80,"-"))
    print("*"*80)
    
    tl="Business class"
    
    msg1="""1.Flight-101 and 2.Flight-102"""
    print(msg1)
    
    num1=int(input("Enter the flight number:"))
    
    if num1==101:
            print("Business class totally",flight1["Bseats"], "seats")
    else:
            print("Business class totally",flight2["Bseats"], "seats")   
    print("Flight ticket for business class",original["Bprice"])
    
    bookID=int(input("Enter the booking id:"))
    
    name=input("Enter you name:")
    sit=int(input("Enter the number of seats:"))
    
    if num1==101:
        if sit <= flight1["Bseats"]:
            print("Food are available")
    
            msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
            print(msg3)
            v1=int(input("Enter the number of non-veg dish:"))
            v2=int(input("Enter the number of veg dish:"))
    
            p1=original["Bprice"]*sit
        
            flight1["Bseats"]=flight1["Bseats"]-sit
            #print("101",flight1["Bseats"])
            #print("FB1",flight1)
            p1f1=original["non_veg"]*v1
            p1f2=original["veg"]*v2
    
            total = p1 + p1f1 + p1f2
    
            return sit,p1,p1f1, p1f2,name, num1,v1,v2,total,tl,bookID
        else:
            return 0

    elif num1==102:
        if sit <= flight2["Bseats"]:
            print("Food are available")
    
            msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
            print(msg3)
            v1=int(input("Enter the number of non-veg dish:"))
            v2=int(input("Enter the number of veg dish:"))
    
            p1=original["Bprice"]*sit
        
            flight2["Bseats"]=flight2["Bseats"]-sit
            #print("102",flight2["Bseats"])
            #print("FB2",flight2)

            p1f1=original["non_veg"]*v1
            p1f2=original["veg"]*v2
    
            total = p1 + p1f1 + p1f2
    
            return sit,p1,p1f1, p1f2,name, num1,v1,v2,total,tl,bookID
        else:
            return 0

            
   
    print("*"*80)

#Economy class details:
def economyCl():
    print("*"*80)
    ec="ECONOMY CLASS"
    print(ec.center(80,"-"))
    print("*"*80)
    tl="Economy class"
    msg1="""1.Flight-101 and 2.Flight-102"""
    print(msg1)
    num1=int(input("Enter the flight number:"))
    
    if num1==101:
        print("Economy class totally",flight1["Eseats"], "seats")
    else:
        print("Economy class totally",flight2["Eseats"], "seats")  
        
        
    print("Flight ticket for economy class",original["Eprice"])
    
    bookID=int(input("Enter the booking id:"))

    name=input("Enter you name:")
    
    sit=int(input("Enter the number of seats:"))
    
    if num1==101:
        if sit <= flight1["Eseats"]:
            print("Food are available")
    
            msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
            print(msg3)
            v1=int(input("Enter the number of non-veg dish:"))
            v2=int(input("Enter the number of veg dish:"))
    
            p1=original["Eprice"]*sit
        
            flight1["Eseats"]=flight1["Eseats"]-sit
            #print("101",flight1["Eseats"])
            #print("FB1",flight1)
            p1f1=original["non_veg"]*v1
            p1f2=original["veg"]*v2
    
            total = p1 + p1f1 + p1f2
    
            return sit,p1,p1f1, p1f2,name, num1,v1,v2,total,tl,bookID
        else:
            return 0

    elif num1==102:
        if sit <= flight2["Eseats"]:
            print("Food are available")
    
            msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
            print(msg3)
            v1=int(input("Enter the number of non-veg dish:"))
            v2=int(input("Enter the number of veg dish:"))
    
            p1=original["Eprice"]*sit
        
            flight2["Eseats"]=flight2["Eseats"]-sit
            #print("102",flight2["Eseats"])
            #print("FB2",flight2)

            p1f1=original["non_veg"]*v1
            p1f2=original["veg"]*v2
    
            total = p1 + p1f1 + p1f2
    
            return sit,p1,p1f1, p1f2,name, num1,v1,v2,total,tl,bookID
        else:
            return 0
    
    
    print("*"*80)


# Each passenger details store in dictionary format:
def booking_1(sit,p1,p1f1,p1f2,name,num1,v1,v2,total,tl,bookID):
    booking1={
            "Booking person Name":name,
            "Flight number":num1,
            "Number of Seats":sit,
            "Ticket price":p1,
            "Total amount ticket":total,
            "Non_Veg amount":p1f1,
            "Veg amount":p1f2,
            "Count of non_veg":v1,
            "Count of veg":v2,
            "Class":tl,
            "Booking Id":bookID
        }
    # Each details append the main storage in  booking list
    booking.append(booking1)
    #print(booking)
    
#Cancel details:
def cancel():
    print("*"*80)
    cl="CANCEL DETAILS"
    print(cl.center(80,'*'))
    print("*"*80)
    
    name=input("Enter your booking name:")
    tl=input("Enter the class:")
    num=int(input("Enter the flight number:"))
    bookID=int(input("Enter the booking id:"))

    l=len(booking)
    
    for i in range(0,l):
        if "Business class"==tl:
            if booking[i]["Booking person Name"]==name and booking[i]["Booking Id"]==bookID:
                print("Refund amount for booking:",booking[i]["Total amount ticket"])
                if num==101:
                    flight1["Bseats"]=flight1["Bseats"]+booking[i]["Number of Seats"]
                    #print("101-b",flight1["Bseats"])
                    #print("cFB1",flight1)
                else:
                    flight2["Bseats"]=flight2["Bseats"]+booking[i]["Number of Seats"] 
                    #print("102-b",flight2["Bseats"])
                    #print("cFB2",flight2)


        elif "Economy class"==tl:
            if booking[i]["Booking person Name"]==name and booking[i]["Booking Id"]==bookID:
                print("Refund amount for booking:",booking[i]["Total amount ticket"])
                if num==101:
                    flight1["Eseats"]=flight1["Eseats"]+booking[i]["Number of Seats"]
                    #print("101=e",flight1["Bseats"])
                    #print("cEB1",flight1)


                else:
                    flight2["Eseats"]=flight2["Eseats"]+booking[i]["Number of Seats"]  
                    #print("102-e",flight1["Eseats"])
                    #print("cEB2",flight2)
    print("*"*80)

# Printall details:
def printBook(name,bookID):
    print("*"*80)
    dt="DETAILS"
    print(dt.center(80,'*'))
    print("*"*80)
    
    l=len(booking)
    for i in range(0,l):
        if booking[i]["Booking person Name"]==name and booking[i]["Booking Id"]==bookID:
            print("Flight class:",booking[i]["Class"])
            print("Booking person Name:",booking[i]["Booking person Name"])
            print("Flight number:",booking[i]["Flight number"])
            print("Flight Booking Id:",booking[i]["Booking Id"])
            print("Number of Seats:",booking[i]["Number of Seats"])
            print("Ticket price:",booking[i]["Ticket price"])
            print("Count of non_veg:",booking[i]["Count of non_veg"])
            print("Count of veg:",booking[i]["Count of veg"])
            print("Non_Veg amount:",booking[i]["Non_Veg amount"])
            print("Veg amount:",booking[i]["Veg amount"])
            print("Total amount ticket:",booking[i]["Total amount ticket"])  
    print("*"*80)

while True:
    choice=int(input("Enter the number:"))
    if choice==1:
        print("Two flight ticket booking are open")
        print("Each flight having 50 seats")
        print("Total two class are available")
        msg2="""1.Business class and 2.Economy class"""
        print(msg2)
        cl=int(input("choice the class:"))
        if cl==1:
            #bus store all return value in tuple form
            bus=businessCl()#-------------(tuple)
            if bus==0:
                 print("Check seats avaiables in flight1")
            else:
                sit=bus[0]# tuple index
                p1=bus[1]
                p1f1=bus[2]
                p1f2=bus[3]
                name=bus[4]
                num1=bus[5]
                v1=bus[6]
                v2=bus[7]
                total=bus[8]
                tl=bus[9]
                bookID=bus[10]
                booking_1(sit,p1,p1f1,p1f2,name,num1,v1,v2,total,tl,bookID)
                printBook(name,bookID)
        else:
            eco=economyCl()
            if eco==0:
                    print("Check seats avaiables in flight1")

            else:   
                sit=eco[0]
                p1=eco[1]
                p1f1=eco[2]
                p1f2=eco[3]
                name=eco[4]
                num1=eco[5]
                v1=eco[6]
                v2=eco[7]
                total=eco[8]
                tl=eco[9]
                bookID=eco[10]
                booking_1(sit,p1,p1f1,p1f2,name,num1,v1,v2,total,tl,bookID)
                printBook(name,bookID)
        print("*"*80)
    elif choice==2:
        cancel()
    elif choice==3:
        seats()
    else:
        print("Thank you and come again")
        break
        



# In[ ]:





# In[ ]:




