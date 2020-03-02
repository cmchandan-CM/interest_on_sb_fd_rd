class Fd:
   def calculateinterest(amount,days,age):
       interest=0.0
       if(amount<10000000):
         if(age<60):
             if (days > 7 and days < 14):
                 interest=(amount*4.50)/100
                 print(f"Interest gained : {interest}")
             elif (days > 15 and days < 29):
                 interest = (amount * 4.75) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 30 and days < 45):
                 interest = (amount * 5.50) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 45 and days < 60):
                 interest = (amount * 7) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 61 and days < 184):
                 interest = (amount * 7.50) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 185 and days < 365):
                 interest = (amount * 8) / 100
                 print(f"Interest gained : {interest}")
         else:
             if (days > 7 and days < 14):
                 interest = (amount * 5) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 15 and days < 29):
                 interest = (amount * 5.25) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 30 and days < 45):
                 interest = (amount * 6) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 45 and days < 60):
                 interest = (amount * 7.50) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 61 and days < 184):
                 interest = (amount * 8) / 100
                 print(f"Interest gained : {interest}")
             elif (days > 185 and days < 365):
                 interest = (amount * 8.5) / 100
                 print(f"Interest gained : {interest}")
       else:
           if (days > 7 and days < 14):
               interest = (amount * 6.5) / 100
               print(f"Interest gained : {interest}")
           elif (days > 15 and days < 29):
               interest = (amount * 6.75) / 100
               print(f"Interest gained : {interest}")
           elif (days > 30 and days < 45):
               interest = (amount *7 ) / 100
               print(f"Interest gained : {interest}")
           elif (days > 45 and days < 60):
               interest = (amount * 8) / 100
               print(f"Interest gained : {interest}")
           elif (days > 61 and days < 184):
               interest = (amount * 8.5) / 100
               print(f"Interest gained : {interest}")
           elif (days > 185 and days < 365):
               interest = (amount * 10) / 100
               print(f"Interest gained : {interest}")

class sb(Fd):
    def calculateinterest(amount,year,type):
        interest=0.0
        if(year>0):
            if (type == 'NORMAL'):
                interest=(amount*4*year)/100
                print(f"Interest gained : {interest}")

            else:
                interest = (amount * 6*year) / 100
                print(f"Interest gained : {interest}")
        else:
            print("enter valid year ")

class rd(sb):
    def calculateinterest(amount,month,age):
      interest=0.0
      if(age<60):

          if (month == 6):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (7.5 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 9):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (7.75/ 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 12):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 15):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.25 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 18):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.5 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 21):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.75 / 100))
              print(f"Interest on RD ::{interest}")
      else:
          if (month == 6):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 9):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.25 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 12):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.5/ 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 15):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (8.75 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 18):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (9 / 100))
              print(f"Interest on RD ::{interest}")
          elif (month == 21):
              interest = (amount * ((month * (month + 1)) / (2 * 12)) * (9.25 / 100))
              print(f"Interest on RD ::{interest}")

class account(rd):
    def __init__(self):
        while True:
            print("MAIN MENU")
            print("---------")
            print("1. Interest Calculator - SB")
            print("2. Interest Calculator - FD")
            print("3. Interest Calculator - RD")
            print("4. Exit")
            val=int(input("Enter Your Option(1..4)"))
            if(val==1):
                 amount=float(input("Enter the Average Amount in your account :"))
                 year=int(input("Enter the year :" ))
                 type=input("Enter Type of account (NORMAL or NRI) :")
                 if(amount<0 and year<0 ):
                   raise Exception("VALID VALUE ENTER OF AMOUNT AND YEAR :")

                 sb.calculateinterest(amount,year,type.upper())
            elif (val == 2):
                amount = float(input("Enter the FD Amount  :"))
                days = int(input("Enter the number of days :"))
                if(amount<10000000):
                    age = int(input("Enter your age :"))
                else:
                    age=0

                Fd.calculateinterest(amount,days,age)
            elif (val == 3):

                amount = float(input("Enter the Monthly installment:  :"))
                month = int(input("Enter the Month :(6,9,12,15,18,21)"))
                age = int(input("Enter your age :"))
                rd.calculateinterest(amount,month,age)
            elif (val == 4):
                exit()
            else:
                print("invalid value Entered Again")
                continue

obj=account()
# p=500
# n=48
# r=9
# uj=0.0
# uj=(p*((n*(n+1))/(2*12))*(r/100))
