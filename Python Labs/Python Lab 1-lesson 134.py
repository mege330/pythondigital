num=int(input("Enter a number with 4 digit: "))

'''
Alafim=4
Meot=5
Asarot=6
Ahadot=7

'''
#this is alafin
#print("Alafim=" +str(num//1000))
#this is Meot
#print("Meot=" +str(num%1000//100))
#this is Asarot
#print("Asarot=" +str(num%100//10))
#this is Ahadot
#print("Ahadot=" +str(num%10))

print("Alafim=" +str(num//1000) + "\nMeot=" +str((num%1000)//100) + "\nAsarot=" +str(((num%100)//10)) + "\nAhadot=" + str((num%10)) )

