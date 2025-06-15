class Fibonacci:
    def __init__(self, n):
        self.n = n
    
    def fib(self, num):
        if num <= 0:
            return 0
        elif num == 1:
            return 1
        else:
            return self.fib(num - 1) + self.fib(num - 2)
    
    def print_series(self):
        for i in range(self.n):
            print(self.fib(i), end=" ")

n = int(input("Enter the number of terms: "))
fib_series = Fibonacci(n)
fib_series.print_series()