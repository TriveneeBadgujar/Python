class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True
#other way
n = int(input())

if n <= 1:
    print("false")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    print("true" if prime else "false")

#other way
class Solution:
    def isPrime(self, n):
        # code here
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
            
