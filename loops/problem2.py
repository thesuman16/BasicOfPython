# Sum of even numbers : Calculate the sum of even numbers upto a given number n.
n = int(input("Enter the range from 0 to Sum of Even: "))
sum_even = 0

for i in range (2, n+1):
    if i%2 == 0:
        sum_even +=1
         
print("Sum of Even number is: ",sum_even)