#Programm to determine the student's grade.
grade = 0

while grade != -1:
  grade = float(input("Please enter the student's grade or enter -1 to exit the program: "))

  #Check a valid value.
  if grade < -1:
    grade = float(input("Please enter the student's grade or enter -1 to exit the program: "))

  else:
    if grade >= 90:
      print("The student got an A")

    elif grade >= 80:
      print("The student got an B")

    elif grade >= 70:
      print("The student got an C")

    elif grade >= 60:
      print("The student got an D")

    elif grade >= 0:
      print("The student got an F")

    else:
      print("You have left the program")

  