# Name: Rainier Javillo
# Date: 11/19/2021
# File: random313.py - This program does different things depending on its command-line arguments.

import sys  # to get the commandline arguments
import random  # to generate pseudo-random numbers

# declare variables
n = 0
m = 0
o = 0
letters = 'abcdefghijklmnopqrstuvwxyz'

# total arguments
arg_count = len(sys.argv)

try:
    # if 0 arguments are passed
    if arg_count == 1:
        print(random.randrange(101))  # print random integer from 0 to 100 inclusive
        
    # if -p argument is passed
    elif sys.argv[1] == '-p':
        arg_list = sys.argv[2:]
        random.shuffle(arg_list)  # shuffle the arg_list
        for i in range(len(arg_list)):  # from beginning to end of list...
            print(arg_list[i])  # print each element of the list
        
    # if 1 argument is passed
    elif arg_count == 2:
        n = int(sys.argv[1])  # get the number in the first arg, convert string to int
        if n > 0:  # if n is positive
            print(random.randrange(n+1))  # print random integer from 0 to n inclusive
        else:
            sys.exit("ERROR: Must be called with one numeric argument >0.")  # error if n is not positive
        
    # if 2 arguments are passed
    elif arg_count == 3:
        if sys.argv[1] == '-s':  # if called with argument -s
            n = int(sys.argv[2])  # get the number in the second arg
            if n > 0:  # if n is positive
                for i in range(n):  # string is of length n
                    print(random.choice(letters), end='')  # print a random lowercase string
                print('\n')  # print new line
            else:
                sys.exit("ERROR: Argument -s should be followed by a numeric argument >0.")
            
        elif sys.argv[1] == '-c':  # if called with argument -c
            n = int(sys.argv[2])  # get the number in the second arg
            if n > 0:  # if n is positive
                for i in range(n):  # string is of length n
                    print(random.randrange(101))  # print random integer from 0 to 100 inclusive
            else:
                sys.exit("ERROR: Argument -c should be followed by a numeric argument >0.")
        else:  # else just print a number between n and m 
            n = int(sys.argv[1])  # get the number in the first arg
            m = int(sys.argv[2])  # get the number in the second arg
            if m > n:
                print(random.randrange(n, m+1))  # print random integer from n to m inclusive
            else:
                sys.exit("ERROR: The right numeric argument should be greater than the left numeric argument, n < m.")

    # if 3 arguments are passed
    elif arg_count == 4:
        if sys.argv[1] == '-c':  # if called with argument -c
            n = int(sys.argv[2])  # get the number in the second arg
            if n > 0:  # if n is positive
                m = int(sys.argv[3])  # get the number in the third arg
                if m > 0:  # if m is positive
                    for i in range(n):  # print the random integer n times
                        print(random.randrange(m+1))  # print random integer from 0 to m inclusive
                else:
                    sys.exit("ERROR: Must be called with one numeric argument >0.") # error if m is not positive
            else:
                sys.exit("ERROR: Argument -c should be followed by a numeric argument >0.")  # error if n is not positive
            
    # if 4 arguments are passed
    elif arg_count == 5:
        if sys.argv[1] == '-c':  # if called with argument -c
            n = int(sys.argv[2])  # get the number in the second arg
            if n > 0:  # if n is positive
                if sys.argv[3] == '-s': 
                    m = int(sys.argv[4])  # get the number in the fourth arg 
                    if m > 0:  # if m is positive
                        for i in range(n):  # outer-loop: print the random string n times
                            for j in range(m):  # inner-loop: for string
                                print(random.choice(letters), end='')  # print a random lowercase string
                            print('\n')  # print new line
                    else:
                        sys.exit("ERROR: Argument -s should be followed by a numeric argument >0.")
                else: 
                    m = int(sys.argv[3])  # get the number in the third arg  
                    o = int(sys.argv[4])  # get the number in the fourth arg
                    if o > m:
                        for i in range(n):  # print the random integer n times
                            print(random.randrange(m, o+1))  # print random integer from m to o inclusive
                    else:
                        sys.exit("ERROR: The right numeric argument should be greater than the left numeric argument, n < m.")
            else:
                sys.exit("ERROR: Argument -c should be followed by a numeric argument >0.")  # error if n is not positive
except:
    sys.exit("ERROR: That is not one of the matching patterns.")