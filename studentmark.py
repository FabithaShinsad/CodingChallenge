print("  Mark List")
english=95
malayalam=85
maths=75
chemistry=62
physics=81
total=english+malayalam+maths+chemistry+physics
percentage=(total/500)*100
print("English  ",english)
print("Malayalam  ",malayalam)
print("Maths  ",maths)
print("Chemistry  ",chemistry)
print("Physics  ",physics)
print("Total        ",total)
print("Percentage   ",percentage)

if(percentage>=90):
    print("Grade         A+")
elif(percentage>=80 and percentage<90):
    print("Grade            A ")
elif(percentage>=70 and percentage<80):
    print("Grade             B")
elif(percentage>=60 and percentage<70):
    print("Grade         C")
elif(percentage>=50 and percentage<60):
    print("Grade         D")
else:
    print("Grade             E")         



