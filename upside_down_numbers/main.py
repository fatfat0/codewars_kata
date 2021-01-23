"""Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. 
To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. 
Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, 
because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

More examples in the test cases.
"""


def solve(a, b):
    counter = 0
    for i in range(a, b):
        if upsidedown_number(i):
            counter += 1
    return counter


def upsidedown_number(i):
    result = ""
    str_num = str(i)
    for j in str_num[::-1]:
        try:
            result += number(j)
        except TypeError:
            return False
    return str_num == result


def number(i):
    # Completed in 234.03ms
    if i in ["0", "1", "8"]:
        return i
    elif i == "6":
        return "9"
    elif i == "9":
        return "6"
    else:
        return None


def number_dict(i):
    # Completed in 913.99ms
    dict_number = {
        0: 0,
        1: 1,
        2: None,
        3: None,
        4: None,
        5: None,
        6: 9,
        7: None,
        8: 8,
        9: 6,
    }
    return dict_number[i]
