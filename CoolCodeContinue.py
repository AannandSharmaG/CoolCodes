blockedDatesInMyCalender = [2,4,6,7,10,13,14,15,18,19,23,25,27]
print("I am available on these dates:")
for date in range(1,32):
     if date in blockedDatesInMyCalender:
         continue
     print(date)