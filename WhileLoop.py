#Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
class Solution:
    def utility(self, x):
        # code here
        while x >= 0:
            print(x, end=" ")
            x -=1
#other way

x = int(input())
for i in range(x, -1, -1):
    print(i, end=" ")
