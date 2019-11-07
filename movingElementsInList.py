"""
  This is for moving up and down (or left and right) elements in a Python list. 
  TODO: 
  * Error checking for input
  * enable moving several positions at once
"""

def moveListItem(lis, pos, direction="left"):
    if pos < 1 or pos >= len(lis)-1:
        return
    
    add = 1
    
    if direction.lower() == "left":
        add = -1
    
    element = lis.pop(pos)
    lis.insert(pos+add, element)
    

if __name__ == "__main__":
    # initializing list 
    test_list = ['3', '5', '7', '9', '11'] 
  
    # printing original list  
    print ("The original list is : " + str(test_list)) 
    
    moveListItem(test_list, 2, "right")
  
    # printing result 
    print ("The modified element moved list is : " + str(test_list)) 
