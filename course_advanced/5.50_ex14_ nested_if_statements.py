score = int(input("What is student's score? "))

if score >= 90:
    print("Student's grade is A.")
else:
    if score >= 80:
        print("Student's grade is B.")
    else:
        if score >= 70:
            print("Student's grade is C.")
        else:
            if score >=60:
                print("Student's grade is D.")
            else:
                print("Student's grade is F.")
