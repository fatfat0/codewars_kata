"""In this Kata your task will be to return the count of pairs that have consecutive numbers as follows:
pairs([1,2,5,8,-4,-3,7,6,5]) = 3
The pairs are selected as follows [(1,2),(5,8),(-4,-3),(7,6),5]
--the first pair is (1,2) and the numbers in the pair are consecutive; Count = 1
--the second pair is (5,8) and are not consecutive
--the third pair is (-4,-3), consecutive. Count = 2
--the fourth pair is (7,6), also consecutive. Count = 3. 
--the last digit has no pair, so we ignore.
"""


def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):  # looping through the index by 2. (etc. 0,2,4,...)
        try:  # try block for last number if it is not a pair.
            if (
                abs(ar[i] - ar[i + 1]) == 1
            ):  # abs() is absolute function and checking if they are consecutive.
                count += 1
        except IndexError:
            pass
    return count