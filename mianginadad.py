students = []
i = 1
while i <= 4:
    lesson1 = float(input("نمره درس ۱ را وارد کنید: "))
    lesson2 = float(input("نمره درس ۲ را وارد کنید: "))
    lesson3 = float(input("نمره درس ۳ را وارد کنید: "))
    lesson4 = float(input("نمره درس ۴ را وارد کنید: "))

    miangin = (lesson1 + lesson2 + lesson3 + lesson4) / 4
    students.append(miangin)
    i += 1

print("s1:", students[0], "s2:", students[1], "s3:", students[2], "s4:", students[3])
if students[0] > students[1] and students[0] > students[2] and students[0] > students[3]:
    if students[1] > students[2] and students[1] > students[3]:
        if students[2] > students[3]:
            print(students[0])
            print(students[1])
            print(students[2])
            print(students[3])
        else:
            print(students[0])
            print(students[1])
            print(students[3])
            print(students[2])
    elif students[2] > students[1] and students[2] > students[3]:
        if students[1] > students[3]:
            print(students[0])
            print(students[2])
            print(students[1])
            print(students[3])
        else:
            print(students[0])
            print(students[2])
            print(students[3])
            print(students[1])
    else:
        if students[1] > students[2]:
            print(students[0])
            print(students[3])
            print(students[1])
            print(students[2])
        else:
            print(students[0])
            print(students[3])
            print(students[2])
            print(students[1])
elif students[1] > students[0] and students[1] > students[2] and students[1] > students[3]:
    if students[0] > students[2] and students[0] > students[3]:
        if students[2] > students[3]:
            print(students[1])
            print(students[0])
            print(students[2])
            print(students[3])
        else:
            print(students[1])
            print(students[0])
            print(students[3])
            print(students[2])
    elif students[2] > students[0] and students[2] > students[3]:
        if students[0] > students[3]:
            print(students[1])
            print(students[2])
            print(students[0])
            print(students[3])
        else:
            print(students[1])
            print(students[2])
            print(students[3])
            print(students[0])
    else:
        if students[0] > students[2]:
            print(students[1])
            print(students[3])
            print(students[0])
            print(students[2])
        else:
            print(students[1])
            print(students[3])
            print(students[2])
            print(students[0])

elif students[2] > students[0] and students[2] > students[1] and students[2] > students[3]:
    if students[0] > students[1] and students[0] > students[3]:
        if students[1] > students[3]:
            print(students[2])
            print(students[0])
            print(students[1])
            print(students[3])
        else:
            print(students[2])
            print(students[0])
            print(students[3])
            print(students[1])
    elif students[1] > students[0] and students[1] > students[3]:
        if students[0] > students[3]:
            print(students[2])
            print(students[1])
            print(students[0])
            print(students[3])
        else:
            print(students[2])
            print(students[1])
            print(students[3])
            print(students[0])
    else:
        if students[0] > students[1]:
            print(students[2])
            print(students[3])
            print(students[0])
            print(students[1])
        else:
            print(students[2])
            print(students[3])
            print(students[1])
            print(students[0])

