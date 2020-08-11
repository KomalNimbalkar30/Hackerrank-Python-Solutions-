# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

ip=input().split()
month=int(ip[0])
date=int(ip[1])
year=int(ip[2])

cal=calendar.weekday(year,month,date)

if cal == 0:
    print("MONDAY")
elif cal == 1:
    print("TUESDAY")
elif cal == 2:
    print("WEDNESDAY")
elif cal==3:
    print("THURSDAY")
elif cal==4:
    print("FRIDAY")
elif cal== 5:
    print("SATURDAY")
elif cal==6:
    print("SUNDAY")
