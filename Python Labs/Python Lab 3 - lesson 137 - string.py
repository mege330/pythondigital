#יצירת 2 משתנים : סטרינג של השם המלא, סטרינג נוסף של כתובת המייל
#יצירת משתנה של הגיל (אינטיג'ר)
#הדפסה על המסך של כל המשתנים בצורה יפה
#הדפסת שם מלא והדפסת הגיל תהיה *3
#אחר כך לבדוק האם השם שלנו מופיע בתוך הסטרינג הבא:
#"menahem eliezer ofir shlomi yuval moshe kobi aminadav"

name="menahem geller"
age=62
mail="menahem.geller@gmail.com"
print("Full Nmae: " + name + "\nage: " +str(age) + "\nmail: " + mail)
print("\n\nFull Nmae: " + name[::-1] + "\nage: " +str(age*3) )
print("menahem" in "menahem eliezer ofir shlomi yuval moshe kobi aminadav")