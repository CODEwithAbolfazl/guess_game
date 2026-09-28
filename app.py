number = 5
guess = 0
count_fail = 0
while guess != number and count_fail < 3 :
  guess = int(input("enter a number"))

  if guess < number :
      print("number is higher")
      count_fail +=1
  else:
    print("number is less ")
    count_fail += 1

print("good job")
print(count_fail)