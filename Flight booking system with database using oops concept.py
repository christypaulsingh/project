#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sqlite3
#class
class flight:
    def __init__(self):
        self.bookId=None
        self.bookingName=None
        self.pin=None
        self.email=None
        self.seats=None
        self.non_veg=None
        self.veg=None
        self.bookingTicket=None
        self.non_vegPrice=None
        self.vegPrice=None
        self.flightNum=None
        self.bookingClass=None
        self.noOfPassenger=None
        self.date=None
        self.time=None
        self.totalPrice=None
        self.place=None
        self.bookingList=[]
        self.conn=sqlite3.connect('E:\sqlite\Ticket.sqlite')
        cursor=self.conn.cursor()
        cursor.execute("""Create table ticket08
                          (Id integer primary key autoincrement,
                           FlightNumber int not null,
                           Class text,
                           Booking_ID int not null,
                           Name text not null,
                           Pin int not null,
                           Email char(25),
                           No_of_Passenger int,
                           Seats int not null,
                           Place text not null,
                           Date char(10),
                           Time char(10),
                           Non_veg int,
                           Veg int,
                           Total_Price int);""")
        cursor.close()

    def booking(self):
        #Intro:
        print("*"*80)
        st="WELCOME TO AIR INDIA"
        print(st.center(80,'*'))
        print("*"*80)
        
        msg="""1.Ticketing booking\t2.Cancel ticket\t3.Available seats\t4.Exist"""
        print(msg)
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
                
                #Business class
                if cl==1:
                    print("*"*80)
                    bu='Business class'
                    print(bu.center(80,"-"))
                    print("*"*80)
                    
                    #Booking class
                    self.bookingClass="Business class"
                    
                    msg1="""1.Flight-101\tPlace:Mumbai\tDate:23/07/23\tTime:16:00PM\n 2.Flight-102\tPlace:Chennai\tDate:25/07/23\tTime:20:00PM"""
                    print(msg1)
                    
                    #Each flight original seats
                    flight1={ #101
                        "Bseats":25,
                        "Eseats":25,
                        "Date":"23/07/23",
                        "Time":"16:00PM",
                        "Place":"Mumbai"
                    }
                    flight2={ #102
                        "Bseats":25,
                        "Eseats":25,
                        "Date":"25/07/23",
                        "Time":"20:00PM",
                        "Place":"Chennai"
                    }
                    
                    #Flight number:
                    num=int(input("Enter the flight Number:"))
                    if num==101 or num==102:
                        self.flightNum=num
                    else:
                        print("Invlaid flight number")
                    
                    #Display fligth seats:
                    if self.flightNum==101:
                        print("Business class flight number 101",flight1["Bseats"],"seats" )
                    else:
                        print("Business class flight number 101",flight2["Bseats"],"seats" )
                        
                    #Original Rate:
                    original={
                        "Bprice":5000,
                        "Eprice":3000,
                        "non_veg":100,
                        "veg":80
                    }
                    
                    #fligth ticket price:
                    print("Flight ticket price for business class",original["Bprice"])
                    
                    #BookingId:
                    self.bookId=int(input("Enter the booking id:"))
                    
                    #Booking Name:
                    name=input("Enter the booking name:")
                    if name and name.isalpha():
                        self.bookingName=name
                    else:
                        print("Invalid name")
                    
                    #pin number:
                    pin=input("Enter the pin number:")
                    if pin and len(pin)==4:
                        self.pin=pin
                    else:
                        print("Invlaid pin number")
                    
                    #email address:
                    email=input("Enter the email address:")
                    if email and email.endswith("@gmail.com"):
                        self.email=email
                    else:
                        print("Invalid email address")
                    
                    #noOfPassenger:
                    noOfPassenger=int(input("Enter the number of passenger:"))
                    if noOfPassenger<=25:
                        self.noOfPassenger=noOfPassenger
                    else:
                        print("Please check available of seats")
                        
                    #Seats:
                    print("""1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25""")
                    seats=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                    length=len(seats)
                    Sseats=input("Enter the seats number:")
                    seats_list=Sseats.split(" ")
                    Scount=0
                    
                    for i in range(len(seats_list)):
                        Scount+=1
                    
                    """for i in range(len(seats_list)):
                        seats_list[i]=int(seats_list[i])
                        
                    if seats<[25]:
                        for j in range(len(seats_list)):
                            seats.remove(seats_list[j])"""
                    
                    st=(','.join(seats_list))       
                    self.seats=st
                    
                    #Date:
                    date=input("Enter the date:")
                    if date==flight1["Date"] and self.flightNum==101:
                        self.date=date
                    elif date==flight2["Date"] and self.flightNum==102:
                        self.date=date
                
                        
                    #Time:
                    time=input("Enter the time:")
                    if time==flight1["Time"] and self.flightNum==101:
                        self.time=time
                    elif time==flight2["Time"] and self.flightNum==102:
                        self.time=time
                    else:
                        print("Invalid time")
                        
                    #place:
                    place=input("Enter the place:")
                    if place==flight1["Place"] and self.flightNum==101:
                        self.place=place
                    elif place==flight2["Place"] and self.flightNum==102:
                        self.place=place
                    else:
                        print("Invalid time")
                        
                    #condition:
                    if self.flightNum==101:
                        if length<=flight1['Bseats']:
                            print("Food available")
                        #Order for food
                        msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
                        print(msg3)
                        self.non_veg=int(input("Enter the number of non-veg dish:"))
                        self.veg=int(input("Enter the number of veg dish:"))
                        
                        #booking ticket
                        self.bookingTicket=original["Bprice"]*Scount
                        
                        #flight reduce:
                        flight1["Bseats"]=flight1["Bseats"]-Scount
                        
                        #food price:
                        self.non_vegPrice=original["non_veg"]*self.non_veg
                        self.vegPrice=original["veg"]*self.veg
                        
                        #Total price:
                        self.totalPrice=self.bookingTicket+self.non_vegPrice+self.vegPrice
                        
                    elif self.flightNum==102:
                        if length<=flight1['Bseats']:
                            print("Food available")
                        #Order for food
                        msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
                        print(msg3)
                        self.non_veg=int(input("Enter the number of non-veg dish:"))
                        self.veg=int(input("Enter the number of veg dish:"))
                        
                        #booking ticket
                        self.bookingTicket=original["Bprice"]*Scount
                        
                        #flight reduce:
                        flight2["Bseats"]=flight2["Bseats"]-Scount
                        
                        #food price:
                        self.non_vegPrice=original["non_veg"]*self.non_veg
                        self.vegPrice=original["veg"]*self.veg
                        
                        #Total price:
                        self.totalPrice=self.bookingTicket+self.non_vegPrice+self.vegPrice
                        
                    print("*"*80)
                    bu="BOOKING DETAILS"
                    print(bu.center(80,"-"))
                    print("*"*80)           
                    print("Flight class:",self.bookingClass)
                    print("Booking Name:",self.bookingName)
                    print("Pin number:",self.pin)
                    print("Email address:",self.email)
                    print("Flight number:",self.flightNum)
                    print("Flight Booking Id:",self.bookId)
                    print("Number of passenger:",self.noOfPassenger)
                    print("Number of Seats:",self.seats)
                    print("Place:",self.place)
                    print("Date:",self.date)
                    print("Time:",self.time)
                    print("Ticket price:",self.bookingTicket)
                    print("Count of non_veg:",self.non_veg)
                    print("Count of veg:",self.veg)
                    print("Non_Veg amount:",self.non_vegPrice)
                    print("Veg amount:",self.vegPrice)
                    print("Total amount ticket:",self.totalPrice)                        
                    print("*"*80)
                    
                    #Database
                    self.conn=sqlite3.connect('E:\sqlite\Ticket.sqlite')
                    Pin=self.pin
                    FlightNumber=self.flightNum
                    Class=self.bookingClass
                    Name=self.bookingName
                    Booking_ID=self.bookId
                    Email=self.email
                    No_of_Passenger=self.noOfPassenger
                    Seats=self.seats
                    Place=self.place
                    Date=self.date
                    Time=self.time
                    Non_veg=self.non_veg
                    Veg=self.veg
                    Total_Price=self.totalPrice
                    cursor=self.conn.cursor()
                    params=(FlightNumber,Class,Booking_ID,Name,Pin,Email,No_of_Passenger,Seats,Place,Date,Time,Non_veg,Veg,Total_Price)
                    cursor.execute("insert into ticket08 values(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",params);
                    self.conn.commit()
                    self.conn.close()
                    
                #Economy class
                if cl==2:
                    print("*"*80)
                    bu='Economy class'
                    print(bu.center(80,"-"))
                    print("*"*80)
                    
                    #Booking class
                    self.bookingClass="Economy class"
                    
                    msg1="""1.Flight-101\tPlace:Mumbai\tDate:23/07/23\tTime:16:00PM\n 2.Flight-102\tPlace:Chennai\tDate:25/07/23\tTime:20:00PM"""
                    print(msg1)
                    
                    #Each flight original seats
                    flight1={ #101
                        "Bseats":25,
                        "Eseats":25,
                        "Date":"23/07/23",
                        "Time":"16:00PM",
                        "Place":"Mumbai"
                    }
                    flight2={ #102
                        "Bseats":25,
                        "Eseats":25,
                        "Date":"25/07/23",
                        "Time":"20:00PM",
                        "Place":"Chennai"
                    }
                    
                    #Flight number:
                    num=int(input("Enter the flight Number:"))
                    if num==101 or num==102:
                        self.flightNum=num
                    else:
                        print("Invalid flight number")
                    
                    #Display fligth seats:
                    if self.flightNum==101:
                        print("Business class flight number 101",flight1["Eseats"],"seats" )
                    else:
                        print("Business class flight number 101",flight2["Eseats"],"seats" )
                        
                    #Original Rate:
                    original={
                        "Bprice":5000,
                        "Eprice":3000,
                        "non_veg":100,
                        "veg":80
                    }
                    
                    #fligth ticket price:
                    print("Flight ticket price for business class",original["Eprice"])
                    
                    #BookingId:
                    self.bookId=int(input("Enter the booking id:"))
                    
                    #Booking Name:
                    name=input("Enter the booking name:")
                    if name and name.isalpha():
                        self.bookingName=name
                    else:
                        print("Invalid name")
                    
                    #pin number:
                    pin=input("Enter the pin number:")
                    if pin and len(pin)==4:
                        self.pin=pin
                    else:
                        print("Invlaid pin number")
                    
                    #email address:
                    email=input("Enter the email address:")
                    if email and email.endswith("@gmail.com"):
                        self.email=email
                    else:
                        print("Invalid email address")
                    
                    #noOfPassenger:
                    noOfPassenger=int(input("Enter the number of passenger:"))
                    if noOfPassenger<=25:
                        self.noOfPassenger=noOfPassenger
                    else:
                        print("Please check available of seats")
                        
                    #Seats:
                    print("""1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25""")
                    seats=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
                    length=len(seats)
                    Sseats=input("Enter the seats number:")
                    seats_list=Sseats.split(" ")
                    Scount=0
                    
                    for i in range(len(seats_list)):
                        Scount+=1
                    
                    """for i in range(len(seats_list)):
                        seats_list[i]=int(seats_list[i])
                        
                    if seats<[25]:
                        for j in range(len(seats_list)):
                            seats.remove(seats_list[j])"""
                    
                    st=(','.join(seats_list))       
                    self.seats=st
                    
                    #Date:
                    date=input("Enter the date:")
                    if date==flight1["Date"] and self.flightNum==101:
                        self.date=date
                    elif date==flight2["Date"] and self.flightNum==101:
                        self.date=date
                    else:
                        print("Invalid date")
                        
                    #Time:
                    time=input("Enter the time:")
                    if time==flight1["Time"] and self.flightNum==101:
                        self.time=time
                    elif time==flight2["Time"] and self.flightNum==102:
                        self.time=time
                    else:
                        print("Invalid time")
                        
                    #place:
                    place=input("Enter the place:")
                    if place==flight1["Place"] and self.flightNum==101:
                        self.place=place
                    elif place==flight2["Place"] and self.flightNum==102:
                        self.place=place
                    else:
                        print("Invalid time")
                        
                    #condition:
                    if self.flightNum==101:
                        if length<=flight1['Eseats']:
                            print("Food available")
                        #Order for food
                        msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
                        print(msg3)
                        self.non_veg=int(input("Enter the number of non-veg dish:"))
                        self.veg=int(input("Enter the number of veg dish:"))
                        
                        #booking ticket
                        self.bookingTicket=original["Eprice"]*Scount
                        
                        #flight reduce:
                        flight1["Eseats"]=flight1["Eseats"]-Scount
                        
                        #food price:
                        self.non_vegPrice=original["non_veg"]*self.non_veg
                        self.vegPrice=original["veg"]*self.veg
                        
                        #Total price:
                        self.totalPrice=self.bookingTicket+self.non_vegPrice+self.vegPrice
                        
                    elif self.flightNum==102:
                        if length<=flight1['Eseats']:
                            print("Food available")
                        #Order for food
                        msg3="""1.Non-veg-Rs.100 and 2.Veg-Rs.80"""
                        print(msg3)
                        self.non_veg=int(input("Enter the number of non-veg dish:"))
                        self.veg=int(input("Enter the number of veg dish:"))
                        
                        #booking ticket
                        self.bookingTicket=original["Eprice"]*Scount
                        
                        #flight reduce:
                        flight2["Eseats"]=flight2["Eseats"]-Scount
                        
                        #food price:
                        self.non_vegPrice=original["non_veg"]*self.non_veg
                        self.vegPrice=original["veg"]*self.veg
                        
                        #Total price:
                        self.totalPrice=self.bookingTicket+self.non_vegPrice+self.vegPrice
                        
                    print("*"*80)
                    bu="BOOKING DETAILS"
                    print(bu.center(80,"-"))
                    print("*"*80)           
                    print("Flight class:",self.bookingClass)
                    print("Booking Name:",self.bookingName)
                    print("Pin number:",self.pin)
                    print("Email address:",self.email)
                    print("Flight number:",self.flightNum)
                    print("Flight Booking Id:",self.bookId)
                    print("Number of passenger:",self.noOfPassenger)
                    print("Number of Seats:",self.seats)
                    print("Place:",self.place)
                    print("Date:",self.date)
                    print("Time:",self.time)
                    print("Ticket price:",self.bookingTicket)
                    print("Count of non_veg:",self.non_veg)
                    print("Count of veg:",self.veg)
                    print("Non_Veg amount:",self.non_vegPrice)
                    print("Veg amount:",self.vegPrice)
                    print("Total amount ticket:",self.totalPrice)                        
                    print("*"*80)
                    
                    #Database
                    self.conn=sqlite3.connect('E:\sqlite\Ticket.sqlite')
                    Pin=self.pin
                    FlightNumber=self.flightNum
                    Class=self.bookingClass
                    Name=self.bookingName
                    Booking_ID=self.bookId
                    Email=self.email
                    No_of_Passenger=self.noOfPassenger
                    Seats=self.seats
                    Place=self.place
                    Date=self.date
                    Time=self.time
                    Non_veg=self.non_veg
                    Veg=self.veg
                    Total_Price=self.totalPrice
                    cursor=self.conn.cursor()
                    params=(FlightNumber,Class,Booking_ID,Name,Pin,Email,No_of_Passenger,Seats,Place,Date,Time,Non_veg,Veg,Total_Price)
                    cursor.execute("insert into ticket08 values(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",params);
                    self.conn.commit()
                    self.conn.close()
                    
            elif choice==2:
                print("*"*80)
                bu='CANCEL TICKET'
                print(bu.center(80,'-'))
                print("*"*80)
                
                ID=int(input("Enter the booking id:"))
                print("Refund amount:",self.totalPrice)
                self.conn=sqlite3.connect("E:\sqlite\Ticket.sqlite")
                cursor=self.conn.cursor()
                cursor.execute("delete from ticket08 where id=ID")
                self.conn.commit()
                self.conn.close()
            else:
                break;
obj=flight()
obj.booking()

                            
                    
                        
                    

                        
                    
                    
                    
                        
                        
                    

                        
        
        
        
        
        
        
        


# In[ ]:




