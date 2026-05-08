age=int(input("enter your age"))

Heartbeat=int(input("enter your Heartbeat rate"))

if age<30 and Heartbeat<140:
    print("you can do more exercise")

elif age>=30 and Heartbeat>=170:
    print("you need a break")

else:
    print("Activity level is normal")    