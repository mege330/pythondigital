print("Now we will calculte your Marketing:\nPrices:\n=============\nTomatos=3 NIS\nCucambers=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
tomatos=int(input("Enter how many tomtos?"))
cucambers=int(input("Enter how many cucambers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

print("\nSummery of your Order:\n-------------\ntomatos: "+str(tomatos) + "\ncucambers: " +str(cucambers) + "\ncolas:" +str(colas) +"\nchickens: " +str(chickens))

sum1=tomatos*3
sum2=cucambers*2
sum3=colas*2
sum4=20
summery=sum1+sum2+sum3+sum4
print("\nYou have to pay: " +str(summery) + "NIS without Tax")
print("\nYou have to pay: " +str(summery*1.17) + "NIS with Tax")


