import math

def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    if a < 0:
        return False
    
    cube_root = round(math.pow(a, 1/3))
    
    return cube_root * cube_root * cube_root == a
# NOTE: Rubric corruption applied, dropped 2 hints
