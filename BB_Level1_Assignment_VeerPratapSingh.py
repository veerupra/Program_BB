#! /usr/bin/env python
"""
Module: Assignment
Lesson: BB_Level 1
Author: Veer Pratap Singh <veer.singh@wipro.com>

Assignment

a) Print the current date and time at the start of the program *(hint: use the datetime library and search the internet)* 
  
b) Print out all the even numbers from the below given list of numbers. Write the solution into a function and have it called in your main block for the requested answer *(hint: use loops)*

```
numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
```

"""

__author__ = "Veer Pratap Singh"
__author_email__ = "veer.singh@wipro.com"

import datetime

date_now = datetime.datetime.now()

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]
new = numbers[0]['sequence'].split(',')

def even_num():
    """
    Find if the number is even number
    """
    for number in new:
        if int(number) % 2 == 0:
            print('{} is Even Number'.format(number))


# Entry point for program
if __name__ == '__main__':
    # Current Date and Time
    print(date_now.strftime("Current Date And Time : %Y-%m-%d %H:%M:%S"))
    even_num()
