'''
Problem Description: Return the second largest number from a list.
Tasks: 1. Implement the function or class. 2. Write a simple test in
main.py. 3. Commit the solution to GitHub.
'''
class ArrayUtils:
    #Return the second largest number from a list.
    def second_largest(self,numbers):
        numbers = [int(x) for x in numbers.split(",")]
        max1 = max2 = float('-inf')
        for n in numbers:
            if n > max1:
                max2 = max1
                max1 = n
            elif n > max2 and n!= max1:
                max2 = n

        if max2 == float('-inf'):
            return None
        return(max2)
