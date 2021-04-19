'''

Hey, I Already Did That!
========================

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their toes. But you've noticed a 
flaw in the algorithm -- it eventually loops back on itself, so that instead of assigning new minions as it iterates, it gets stuck in a cycle of 
values so that the same minions end up doing the same tasks over and over again. You think proving this to Commander Lambda will help you make a 
case for your next promotion. 

You have worked out that the algorithm has the following process: 

1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 
and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For 
example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values [210111, 122221, 102212] and it will stay in this 
cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 
6174, it will stay as that value no matter how many times it iterates.
Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution('210022', 3)
Output:
    3

Input:
Solution.solution('1211', 10)
Output:
    1

-- Python cases -- 
Input:
solution.solution('1211', 10)
Output:
    1

Input:
solution.solution('210022', 3)
Output:
    3

'''

def decToBase(n,b):
    r = ''
    while n:
        n,rem = divmod(n,b)
        r = str(rem) + r
    return r

def gen_xy(n):
    n = sorted(list(n))
    n = ''.join(n)
    return n[::-1],n

def solution(n,b):
    k = len(n)    
    results=[]
    gen_z = lambda x,y: decToBase((int(x,b)-int(y,b)),b).zfill(k)
    while True:
        x,y = gen_xy(n)
        n = gen_z(x,y)
        if n in results:
            return len(results[results.index(n):])
        results.append(n)
    
        