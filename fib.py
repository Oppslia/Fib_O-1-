'''
Implement the function
fib(n), which returns the nth
number in the Fibonacci sequence, using only O(1) space. (you can ignore the O(1) space thing ... we'll get to that.
'''
def fib(n):
    num1 = 0
    num2 = 1
    ar = [0, 1]
    for x in range(0,n -1):
        ar.append(ar[num1] + ar[num2])
        num1 += 1
        num2 += 1
    print(ar[-1])

n = 4
fib(n)
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# print(fib(9))
