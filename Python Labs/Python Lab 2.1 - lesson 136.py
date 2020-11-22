print("Now we will calculte your Marketing:\nPrices:\n=============\nTomatos=3 NIS\nCucambers=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
tomatos=int(input("Enter how many tomtos?"))
cucambers=int(input("Enter how many cucambers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

print("\nSummery of your Order:\n-------------\ntomatos: "+str(tomatos) + "\ncucambers: " +str(cucambers) + "\ncolas:" +str(colas) +"\nchickens: " +str(chickens))


summery=(tomatos*3)+(cucambers*2)+(colas*5)+(chickens*20)
print("\nYou have to pay: " +str(summery) + "NIS without Tax")
print("\nYou have to pay: " +str("%.2f" % (summery*1.17)) + "NIS with Tax")


