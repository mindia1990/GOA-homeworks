age=int(input("enter your age:"))
card=input("Do you have a student card?")

if age<18 or card=="yes":
    print("danazogi gaqvs")

elif age>60 and card=="no":
    print("pensioneris fasdakleba gaqvs!")

else:
    print("fasdakleba ar gekutvnis")    


