from collections import Counter, deque

"""
Storing user's most recent food orders 
Only store maximum 5 food orders
"""


def main():
    foods = deque(maxlen=5)
    # add code here
    foods.append("STA001")
    foods_ordered = ["DES001", "ENT012", "ENT001", "DES011"]
    foods.extend(foods_ordered)  # multiple object
    foods.append("DES002")
    # ^will automatically remove the left most element since the max lengt is 5
    # when using appendleft, will pop the item from the opposite side if max length is reached
    print(foods)
    return


if __name__ == "__main__":
    main()
