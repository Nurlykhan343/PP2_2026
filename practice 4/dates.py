#1
import datetime

x = datetime.datetime.now()
print(x)

#2
import datetime

x = datetime.datetime.now()

print(x.month)
print(x.strftime("%B"))

#3
import datetime

x = datetime.datetime(2022, 8, 25)

print(x)
#4
import datetime

x = datetime.datetime(2019, 9, 15)

print(x.strftime("%A"))