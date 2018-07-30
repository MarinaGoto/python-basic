#Write a Python function named modCount that is given a positive integer, n, 
#and a second positive integer, m <= n, 
#and returns how many numbers between 1 and n are evenly divisible by m. 



def modCount(int1,int2,sum = 0):
    for i in (range(1,int1 + 1)):
         if (i % int2 == 0):
            sum = sum + 1 
    print(sum)

###############################

n = 10
# pre requirements  m <= n
m = 2

modCount(n,m)  