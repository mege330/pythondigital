print("Input your Height:")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft *12
h_cm = round(h_inch * 2.54, 1)

print("Your Height is : %d cm." % h_cm)