#Program to find out the fibonacci series.


n = int(input('How many terms:'))

n1 = 0
n2 = 1
count = 0

#using decision making and looping 
if n <= 0:
    print("Please enter the number:")
elif n == 1:
    print("Fibonacci Sequence upto", n, ":")
    print(n1)
else:
    print("Fibo series:")
    while count < n:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1
