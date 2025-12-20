# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
import datetime as dt
current_date=dt.date.today()  #here date class i used to work with date 
current_time=dt.datetime.now()            #similerls time class is used to work with time
                                #and dateTime class to work with both date and time
print(current_date)  #print the date
#date can also can be print seperately like year month and day
print(f"year {current_date.year}")
print(f"current time is {current_time}")