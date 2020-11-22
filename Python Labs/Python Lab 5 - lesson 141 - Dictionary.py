#Dictionary - מילון
'''
יצירת מילון עם 5 שמות וכסף
סיכום הכסף של השם הראשון והאחרון ולהדפיס למסך
אח"כ להוסיף שם חדש עם סכום כסף שחושב לפני כן
ולבסוף , הדפסת מספר הכניסות ובדיקת השם מנחם האם קיים
'''

dict_names={"menahem":10000,"shloni":30000,"aminadav":50000,"ofir":25000,"meirav":45000}
print(dict_names)
#עדכון סכום לאחד השמות
dict_names["menahem"]=60000
print(dict_names)

#הדפסה למסך סיכום של השם הראשון והאחרון
print("The Summery is: " + str(dict_names["menahem"]+dict_names["meirav"]))
#עדכון במקום הוספה
summery=dict_names["menahem"]+dict_names["meirav"]
dict_names.update({"hava":summery})
print(dict_names)
#הדפסת מספר הכניסות ובדיקה האם חוה בפנים
print("Number of entrise: " + str(len(dict_names)))
print("hava" in dict_names)




