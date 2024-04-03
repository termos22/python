name = input("What is the job applicant's name? ")
degree = input("What did they major in at college? ")
job = input("What is their current occupation? ")
experience = input("How many years have they been working in their field? ")

print(name + " majored in " + degree + ", works as a " + job + ", add has " + experience + " years of experience.")

print("{} majored in {}, works as a {}, add has {} years of experience.".format(name, degree, job, experience))
