def fibonacci():

    #Initialization of variable x and y to represent the current and next Fibonacci numbers.
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

nums = int(input("Number of fibonacci numbers you want to generate: "))

fib = fibonacci()
for _ in range(nums):
    print(next(fib), end=" ")

print("\n")