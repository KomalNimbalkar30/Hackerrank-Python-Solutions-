# Enter your code here. Read input from STDIN. Print output to STDOUT
def doormatPattern(rows, columns): 
    width = columns 
      
    # Print the pattern having a top triangle 
    for i in range (0, int (rows / 2)): 
        pattern = ".|." * ((2 * i) + 1) 
        print (pattern.center (width, '-')) 
    print ("WELCOME".center (width, '-')) 

    i = int (rows / 2) 
    while i > 0: 
        pattern = ".|." * ((2 * i) - 1) 
        print (pattern.center (width, '-')) 
        i = i-1
    return


rows,columns=map(int,input().split())

doormatPattern(rows,columns)

"""
ip= 9 27
op
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

columns should be 3 times greater than rows
Mat size must be N*M. (N(rows) is an odd natural number, and M(column) is 3 times N.)
"""
