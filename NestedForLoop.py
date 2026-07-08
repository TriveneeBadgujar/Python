#Given two integers n and m, print a solid rectangle pattern of n rows and m columns using the "*" character.

Note: There is a space between two adjacent stars (*) in the pattern.
n = int(input())
m = int(input())

# code here
for i in range(n):
    for j in range(m):
        print("* "*m)
        break
