#Prime number checker : check a number is prime or not
from tkinter import N


number = 22

is_prime = True
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
print(is_prime)