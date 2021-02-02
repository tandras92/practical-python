# bounce.py
#
# Exercise 1.5
"""A rubber ball is dropped from a height of 100 meters and each time it hits the ground,
it bounces back up to 3/5 the height it fell.  Write a program that prints a table showing the height
of the first 10 bounces"""


def calculate_bounce_height(height, bouncing_height, num_of_bounces):
    while num_of_bounces >= 0:
        height = height * bouncing_height
        print(num_of_bounces, round(height, 4))
        num_of_bounces -= 1


print(calculate_bounce_height(100, (3/5), 10))
