"""
  This is a function for moving elements left and right in a Python list.
  TODO:
  * more testing
"""

def moveListItem(lis, pos, count=1, direction="left"):
    """
    move items in a list up or down.
    the original list will be modified, so you might not need the return value.

    This should be O(1)
   :param list lis: The list to be manipulated
   :param int pos: The index of the item to be moved, from 0 -> len(lis)-1
   :param int count: The number of positions it gets moved, -1 for maximal
   :param str direction: if 'left', moving left, if 'right' or anything else, to the right
   :return: True if moved, false if nothing has been moved
   :rtype: bool
   :raises TypeError: if the lis is not a valid list
   :raises LookupError: if the pos is out of list lis bounds
    """

    if type(lis) != list:
        raise TypeError("Given argument lis is not a list!")

    if pos < 0 or pos >=len(lis):
        raise LookupError("List position out of bounds!")

    if direction.lower() == "left":
        add = -1
        if pos < 1: # only move if not on the left side
            return False
    else: # right
        add = 1
        if pos >= len(lis)-1: # only move if not on the right side
            return False


    if count == 0:
        return False
    elif count == -1:
        count = len(lis)

    # calculate insert position
    newpos = pos + add * count

    # cap if requested pos is too big
    if newpos >= len(lis):
        newpos = len(lis)-1
    elif newpos < 0:
        newpos = 0

    element = lis.pop(pos)
    lis.insert(newpos, element)
    return True


if __name__ == "__main__":
    # initializing list
    test_list = ['3', '5', '7', '9', '11']

    # printing original list
    print ("The original list is : " + str(test_list))

    moveListItem(test_list, 2, direction="right")

    # printing result
    print ("The modified element moved list is : " + str(test_list))
