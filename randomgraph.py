# Name: Rainier Javillo
# Date: 11/19/2021
# File: randomgraph.py - This program gets from random313.py 1,000 random numbers, each between 0 and 100, and tracks each of the occurrences of the 101 possible values. It then plots the numbers in a bar graph.
# Help from: https://youtu.be/XDv6T4a0RNc - Used this video to figure out how to graph the occurrences of each number. 
# Instructions: Type: python3 ./random313.py -c 1000 | python3 randomgraph.py 

import sys  # to get the commandline arguments
import pandas as pd  # import pandas for data structures
from matplotlib import pyplot as plt  # pyplot provides MATLAB-like interface

#plt.style.use('fivethirtyeight')  # for styling

# initialize lists
lst_input = []  # this list will be used to store numbers from stdin
lst_occur = [0]*101  # creates a list [0, 0, ... times 101] 

# for each line 
for line in sys.stdin:  # loop through stdin
    lst_input.append(line)  # append each line from stdn to lst_input

lst = [i[:-1] for i in lst_input]  # slice to remove trailing new line in list 

lst_int = [int(i) for i in lst]  # use list comprehension to convert string list to int list

lst_sort = sorted(lst_int)  # sort the int list in order

for i in range(0,len(lst_sort)):  # loops from 0 to length of sorted list (1000)
    lst_occur[lst_sort[i]]+=1  # for each occurrence, increment index in lst_occur

for i in range(0, 101):  # loop from 0 to 101 
    print('# of ' + str(i) + '\'s: ' + str(lst_occur[i]))  # print the occurrence of each number

# plot the items in lst_sort into their corresponding 101 bins (0-100)
plt.hist(lst_sort, bins=101, edgecolor='black')  

plt.title('Occurrence of each number 0-100')  # label for title
plt.xlabel('Number')  # label for x-axis
plt.ylabel('# of occurrences')  # label for y-axis

plt.tight_layout()  # adds padding to plot

plt.show()  # shows the plot