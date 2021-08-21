
# Python program to display the Fibonacci sequence

def Fib(number):
    
    if number < 0:
        print("Negative Number not allowed")
    elif number == 0:
        return 0
    elif number == 1:
        return 1

    else:
        return Fib(number - 1) + Fib(number - 2)

val = Fib(6)

print(val)