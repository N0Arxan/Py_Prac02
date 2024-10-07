from datetime import *
time1 = input("enter your start time (hh:mm) :\n").split(":")
entryH , entryM = map(int,time1)
time2 = input("enter your end time (hh:mm) :\n").split(":")
salidaH , salidaM = map(int,time2)

start = timedelta( hours = entryH , minutes= entryM)
end = timedelta( hours = salidaH , minutes= salidaM)
duration = end - start 
