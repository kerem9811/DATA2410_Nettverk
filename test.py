# Task 1: sum of values
# Write a Python function, sum_of_values, to calculate the sum of
# values in a list. The function will take two arguments: 'a List' and
# 'odd/even/all’.
# sum_of_values ([1,2,3,4,5], “all”). → Output: “the sum is 15”
# sum_of_values ([1,2,3,4,5], “odd”). → Output: “the sum is 9”
# sum_of_values ([1,2,3,4,5,100], “even”). → Output: “the sum is 106”
import random
import portcheck


def sum_of_values(list, str):
    even_sum = 0
    odd_sum = 0
    if str == "all":
        print("the sum is", sum(list))
    elif str == "odd":
        for num in list:
            if num % 2 == 1:
                odd_sum += num
        print("the sum is", odd_sum)
    elif str == "even":
        for num in list:
            if num % 2 == 0:
                even_sum += num
        print("the sum is", even_sum)

sum_of_values([1,2,3,4,5], "all")
sum_of_values([1, 2, 3, 4, 5], "odd")
sum_of_values([1,2,3,4,5,100],"even")


def test7(num):
    if num % 7 == 0:
        print("True")
    else:
        print("False")


test7(21)
test7(14)
test7(5)
test7(11)
# ////////////////////////////////////////////


library = [
    {'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'readingStatus': True},
    {'title': 'Sapiens', 'author': 'Yuval Noah', 'readingStatus': False},
    {'title': 'Factfulness', 'author': 'Hans Rosling', 'readingStatus': True}
]


def checklibrary(list):
    for book in list:
        if 'readingStatus':
            print("You have read the book =",book['title'],"by",book['author'])
        if not 'readingStatus':
            print("You have not read the book =",book['title'],"by",book['author'])

checklibrary(library)

# .............................................................
# Task 4: guess a number
# Write a Python program that generates a random integer between 1 and 10. Prompt the user to guess
# the number. If the user's input matches the generated number, the program will display the message
# 'Good Work.' Otherwise, it will display the message 'Try again' and prompt the user to guess again.
# Hint: To generate a random integer between 1 to 10, import random library and use
# random.randint(1,10)
# Input: Guess a number: 7 → Output: It’s a match!
# Input: Guess a number: 6 → Output: Try again!

def numberGuess():
    randnum = random.randint(1,10)
    count = 0
    while True:
        try:
            num = int((input("Guess a number between 1 and 10: ")))
            if num == randnum:
                print("It’s a match!","Du brukte",count,"forsøk")
                return
            else:
                print("Try again!")
        except ValueError:
            print("Not a number!")
            count += 1
        count += 1

numberGuess()

################################################################################3

#Task 5: Port address check using argparse
# Write a Python program that utilises argparse to take two optional arguments (-p and -s). Check if
# the server is specified with (-s) and ensure that the given port number is within the range (1025,
# 65535).
# Example:
# Run: python3 portcheck.py –s -p 1000
# → Output: Invalid port. The port must be within the range 1025 and 65536
# Run: python3 portcheck.py -p 1075
# → Output: The server is not available
# Run: python3 portcheck.py -s -p 1075
# → Output: Valid port

#####################################################################################

# Task 6: reading from a file
# Write a Python program that reads throughput values from a file and identifies the minimum
# throughput.
# NOTE: Create a text file named throughput_values.txt with the following lines:
# 100 Mbps
# 2000 Kbps
# 1 Gbps
# 200 Mbps
# Hint: Consider the units conversion: 1Kbps = 1000bps, 1Mbps = 1000Kbps, 1Gbps = 1000Mbps
# Output: The minimum throughput value is: 2000 Kbps


