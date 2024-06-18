
import datetime
import re
import smtplib

def supermarket():
    print("Welcome to pk stores")

ghee = 50
butter = 100
cheese = 150
dark_choco = 40
milkybar = 100
one_5star = 10
turmeric = 10
sugar_packet = 60
maida = 50
bournvita= 400
ponds=50
comb=30
clip=30
lipstick=250
ice=30
shampoo=50
maggi=200

f=open("products.txt","r")
txt=f.read()
your_products=input("what do u want?")
x=re.search(your_products,txt)
print(x)

if x:
    print("your product is selected")
    how_many = int(input(f"How many {your_products} do you want? "))
else:
    print("ur product is unavailable")

    delivery = "" 

if your_products== "ghee": # same like add the products
    total= (ghee*how_many)    
    if total <= 1000:
        delivery=""
        gst_rate=4
        gst_price=total*4/100
        net_price=total+gst_price
        print(f"gst {gst_price} gst rate {gst_rate}%")
        print(f"after gst {net_price}")
        print(f"{your_products} {how_many} and the total bill is is {net_price}")
        f=open("bill.txt","w")
        today=datetime.datetime.now()
        f.write(f"ur total bill is  {today} {net_price}")
        print("bill generated sucessfully")
        print("you got a gift of mirror")
        delivery=input(" would you like to pay cash or card?")
             
    else:
        delivery=""
        if total >= 1000:
            gst_rate=4
            gst_price=total*4/100
            net_price=total+gst_price
            print(f"gst {gst_price} gst rate {gst_rate}%")
            print(f"after gst {net_price}")
            discount=net_price-500
            print(discount)
            print(f"{your_products} {how_many} and the total bill is with discount price is {discount}")
            f=open("bill.txt","w")
            today=datetime.datetime.now()
            f.write(f"ur total bill is  {today} {discount}")
            print("bill generated sucessfully")
            print("you got gift of tiffen box")
            delivery=input(" would you like to pay cash or card?")
  
if delivery == "cash":
                print("ok thankyou")
elif delivery == "card":
    card=int(input("enter the card no to pay:"))
    print("welcome")

mail_id=input("enter ur mail id:")
print(mail_id)
try:
        for i in mail_id:
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("hello@gmail.com"  "password")
            f=open("bill.txt","w")
            today=datetime.datetime.now()
            f.write(f"ur total bill is  {today} {discount}")
            print("bill generated sucessfully")
            message=(f" ur bill is {today} {discount}")
            s.sendmail("hello@gmail.com",i,message)
            s.quit()
            print("mail sent successfully")
except:
            print("mail not sent")

