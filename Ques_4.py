# Write a program to check a prime number?
Num = int(input("Enter the Number: "))
# define a flag variable
flag = False
# prime number is greater then 1
if Num > 1:
    # check the factor
    for i in range(2, Num):
        if (Num % i) == 0:
            flag = True
            break
# Check if flag is true
if flag:
    print(Num,"is not a prime number: ")
else:
    print(Num,"is the prime number: ")