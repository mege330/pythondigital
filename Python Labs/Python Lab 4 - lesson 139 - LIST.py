'''
יצירת רשימה עם 4 פרטים אישיים: שם מלא,טלפון,כתובת,גיל
רשימה שניה עם 2 כתובות רשת
להוסיף לרשימה השניה: עוד 3 כתובות רשת, הוצאת הכתובת ה-3 מהרשימה ,
הדפסה כמה כתובות רשת יש לנו ולהדפיסם
'''
#הכנת רשימה סתמית והדפסתה
details_list=["Menahem Geller" , 62 , "menahem.geller@gmail.com" , "035888251"]
print(details_list)
#הדפסת שורה בצורה יפה
details_list=["Menahem Geller" , 62 , "menahem.geller@gmail.com" , "035888251"]
print("Full Name: " +details_list[0] + "\nAge: " + str(details_list[1]) + "\nMail: " + details_list[2] + "\nPhone:" + details_list[3] )
#רשימת כתובות רשת
ip_list=["1.1.1.1","2.2.2.2"]
print(ip_list)
#הוספת כתובות לרשימה קיימת
ip_list.append("5.5.5.5")
ip_list.append("7.7.7.7")
ip_list.append("10.10.10.10")
print(ip_list)
#הוצאת הכתובת השלישית
ip_list.pop(2)
print(ip_list)
#הדפסת הרשימה החסרה וספירה של הכתובות
ip_list.pop(2)
print("IP List length is: " + str(len(ip_list)) + "\nAnd the IP List is: " + str(ip_list))

