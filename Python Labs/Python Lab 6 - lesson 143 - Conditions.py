#CONDITIONS - תנאים

#דוגמה ל-IF מקוון
#name=input("Enter your name: \n")
#if(name=="menahem"):
   # print("Hello Menahem Geller\n")
#elif(name=="shlomi"):
   # print("Hello Shlomi Geller\n")
#elif(name=="aminadav"):
   # print("Hello Aminadav Geller")
#else:
   # print("Where is my suns?...\n")
#print("It was a nice game , Bye Bye\n"
#Menu:
#כתיבת קוד שיראה תפריט
#1. הכנסת מספר שהתוצאה תהיה בחזקת 3
#2. הכנסת 4 כתובות IP לרשימה ולהדפיס
#3. הכנסת 4 ערכים למילון ולהדפיס
#4. בדיקה האם הסטרינג הוא פולינדרום
# אם המשתמש לא יבחר מ1-4 , תאמר לו שעליו לבחור 1-4 בלבד


#for time import sleep

choice=input("Menu:\n---------\n1.Insert a number and ** it by 3\n2.Insert 4 IPs to a list and print it\n3.insert 4 Entries to DNS-Dictionary and print it\n4.Check if a string is Polndrom\n")
if(choice=="1"):
    print("The new Number is: " + str((int(input("Enter a Number: ")))**3))
elif(choice=="2"):
    list_ip=[]
    list_ip.append(input("Enter new IP:"))
    list_ip.append(input("Enter new IP:"))
    list_ip.append(input("Enter new IP:"))
    list_ip.append(input("Enter new IP:"))
    print("\nThe new List:\n---------------\n" + str(list_ip))
elif(choice=="3"):
    dns_dict={}
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    dns_dict.update({input("Enter a URL: "): input("Enter IP: ")})
    print("\nThe new DNS_DICt:\n---------------\n" + str(dns_dict))
elif(choice=="4"):
    word=input("Enter a new Word: ")
    if (word == word[::-1]):
        print("This is a Polindrum!")

else:
    print("Enter 1-4 only!!...")
