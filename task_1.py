def caching_fibonacci():
    #Create an empty dictionary for caching
    cache = {}

    #Internal function to increment the Fibonacci number
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        #Check if the valueis in the cache
        if n in cache:
            return cache[n]
        #Calculate the value if it is not in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n -2)
        return cache[n]
    
    #Return the internal function 
    return fibonacci

#Example of use
fib_num = caching_fibonacci()

print(fib_num(10))
print(fib_num(15))