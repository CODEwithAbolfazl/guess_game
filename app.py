number = 5
guess = 0
count_fail = 0
flag = False

while  count_fail < 3 :
  guess = int(input("enter a number"))

  if guess == number :
      print("correct")
      flag = True
      break
  elif guess < number :
      print("number is higher")

  else:
    print("number is less ")
  count_fail += 1

if flag :
 print("good job")
else:
    print("you lost")
    print(f"fails :{count_fail}")