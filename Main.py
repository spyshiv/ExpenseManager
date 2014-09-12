#This is Second Project On GitHub
print("Welcome To Expense Maneger.@Idea By-'CJAY' Programmed By-'Cipher'")
print("This is an application program to manage money after returning from any trip")
print("So let begin.")       
TripName=input("Enter The Name Of The Trip,You visited With Your Friends.:\n")

#Input Of Friends Names
TotalMember=input("How Many of friends visited the Trip:")
namelist=[]
for i in range(int(TotalMember)):
    prompt=("Enter the name of friend%d:" %(i+1))
    name=input(prompt)
    namelist.append(name)
print ("Your have visted with these friends in '%s'"%(TripName.upper()))
for i in namelist:
    print (i)
#Input Values Spent By Friends or by you.
print("\n\n@@@Attention!!@@@")
moneyList=[]
for i in namelist:
    print("Enter the Money Spent by",i)
    money=input()
    moneyList.append(int(money))
print("Total Details of spending money")
print("Name:Money")
for i in range(len(namelist)):
    print("%s:%s"%(namelist[i],moneyList[i]))

#Calculation Of money
total=0
for i in moneyList:
    total=total+int(i)
print("The total spent amount is=%d"%(total))
equal=total/len(namelist)
newMoneyList=[]
for i in moneyList:
    calculated=equal-int(i)
    newMoneyList.append(calculated)
#Display the Data
print("\n\n@@@Attention!!@@@")
print("-ve Sign means you have to receive")
print("for e.g If Cjay=-10 then he has to receive 10 rupees from someone else")
for i in range(len(namelist)):
    print("%s:%s"%(namelist[i],newMoneyList[i]))
print("The End. Thank You for Using It.")
