"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".

def hello_world():
    """
    Prints 'Hello World'.

    :param: None
    :return: None
    """

    print("Hello World")


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.

def say_hi(name):
    """
    Prints 'Hi {name}'.

    :param: name as a string
    return: None
    """

    print(f"Hi {name}")


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.

def print_product(num1, num2):
    """
    Prints the product of two integers.

    :param num1: first integer
    :param num2: second integer
    :return: None
    """

    print(num1 * num2)

# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times

def repeat_string(phrase, n):
    """
    Prints duplicate of a string based on n times. 

    :param phrase: word or string of words as a string
    :param n: integer
    """

    print(f"{phrase}" * n)


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".

def print_sign(number):
    """
    Prints message 'Higher than 0', 'Lower than '0', or 'Zero' depending on met condition.

    :param number: integer
    :return: None
    """

    if number == 0:
        print("Zero")
    elif number > 0:
        print("Higher than 0")
    else:
        print("Lower than 0")


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.

def is_divisible_by_three(number):
    """
    Returns True if number is divisible by 3.

    :param number: integer
    :return: boolean
    """

    if number % 3 == 0:
        return True
    else:
        return False


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.

def num_spaces(sentence):
    """
    Returns number of spaces in a given string.

    :param sentence: string
    :return: number of spaces in given string 
    """

    num_spaces = 0

    for word in sentence:
        if word == " ":
            num_spaces += 1
    
    return num_spaces


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.

def total_meal_price(price, tip=.15):
    """
    Returns the total amount paid (price + price * tip); default tip = 15%

    :param price: price of meal as integer or float
    :param tip: tip percentage as integer or float
    :return: total amount paid
    """

    tip_amount = price * tip

    return price + tip_amount


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.

def sign_and_parity(number):
    """
    Evaluates a number and returns a list of strings indicating if the number is either positie or negative and either even or odd.

    :param number: given number as integer
    :return: list of strings
    """

    sign_and_parity = []

    if number > 0:
        sign_and_parity.append("Positive")
    elif number < 0:
        sign_and_parity.append("Negative")
    
    if number % 2 == 0:
        sign_and_parity.append("Even")
    else:
        sign_and_parity.append("Odd")
    
    return sign_and_parity

###############################################################################

# PART TWO

# 1. Write a function called full_title that takes a name and a job title as
#    parameters, making it so the job title defaults to "Engineer" if a job
#    title is not passed in. Return the person's title and name in one string.

def full_title(name, title="Engineer"):
    """
    Returns job title and name in one string.

    :param name: name as a string
    :param title: job title as a string
    :return: job title and name in a string
    """

    full_title = f"{title} {name}"

    return full_title

# 2. Write a function called write_letter that, given a recipient name & job
#    title and a sender name, prints the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.

def write_letter(name, title, sender):
    """
    Prints the following letter:

    Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
        Sincerely, SENDER_NAME.
    
    :param name: recipient name as a string
    :param title: job title as a string
    :sender: sender name as a string
    """

    print(f"Dear {full_title(name, title)}, I think you are amazing! Sincerely, {sender}")

###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print
