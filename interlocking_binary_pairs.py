#Task
#Write a function that checks if two non-negative integers make an "interlocking binary pair".

#Interlock ?
#numbers can be interlocked if their binary representations have no 1's in the same place
#comparisons are made by bit position, starting from right to left (see the examples below)
#when representations are of different lengths, the unmatched left-most bits are ignored
#Examples
#a = 9, b = 4
#Stacking representations shows how they can interlock. Here, no 1's share any position, so the function returns true.

# 9    1001
# 4     100
#a = 3, b = 6
#These representations do not interlock. Finding they both have a 1 in the same position, the function returns false.

# 3      11
# 6     110
#Input
#Two non-negative integers.

#Output
#Boolean true or false whether or not these integers are interlockable.

#Enjoy!

def interlockable(a, b):
    a=bin(a)[2:]
    b=bin(b)[2:]
    n=0

    for val in a:
        try:
            n-=1
            if a[n]== '1'and b[n]==a[n]: 
                return False
        except IndexError:
            return True
    return True