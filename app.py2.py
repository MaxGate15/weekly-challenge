#challenge 1
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

        #challenge 2


    def reverse_string(s):
        return s[::-1]
    print(reverse_string("hello"))
    print(reverse_string("world"))

    #challenge 3
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    print(is_prime(5))
    print(is_prime(10))