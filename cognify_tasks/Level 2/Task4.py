def fibonacci(n):
    a, b = 0, 1

    if n <= 0:
        print("Please enter a positive integer")
        return

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Take input from user
n = int(input("Enter number of terms: "))
fibonacci(n)

#OUTPUT
'''
Enter number of terms: 5
0 1 1 2 3 '''
