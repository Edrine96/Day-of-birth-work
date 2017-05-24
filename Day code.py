#Returning the day someone was born
import datetime
Month_Of_Birth = int(input("Insert your Month Of Birth:\n "))
Date_Of_Birth = int(input("Insert your Date Of Birth:\n "))
Age = int(input("Insert Your Age:\n "))
DateNow = datetime.datetime.now()
DaysPerYear = 365
DaysLived = Age*DaysPerYear
Real_Date_Of_Birth_in_Timedelta = datetime.timedelta(days = DaysLived) 
Real_Date_Of_Birth = DateNow-Real_Date_Of_Birth_in_Timedelta
Year_Of_Birth = int(Real_Date_Of_Birth.strftime("%Y"))
Exact_Date_Of_Birth = datetime.date(Year_Of_Birth,Month_Of_Birth,Date_Of_Birth)
print("You were born on",Exact_Date_Of_Birth.strftime("%A"))
