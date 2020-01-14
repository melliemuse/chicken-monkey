# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.
# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".
def count_to_100():
    for num in range(1, 101):
        if num % 5 == 0 and num % 7 == 0:
            print("ChickenMonkey")
        if num % 5 == 0:
            print("chicken")
        if num % 7 == 0:
            print("monkey")
        else:
            print(num)
count_to_100()
# To determine if a number can be evenly divided by 5 or 7, use the Python modulo operator. 