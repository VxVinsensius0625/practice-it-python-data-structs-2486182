from collections import deque
import math

"""
checking palindrome 
"""


def check_palindrome(word):
    d = deque(word)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


def main():
    word = "12345"
    print(check_palindrome(word))


if __name__ == "__main__":
    main()
