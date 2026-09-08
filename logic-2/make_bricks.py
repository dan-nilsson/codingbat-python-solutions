'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks


make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''

def make_bricks(small, big, goal):
    small_total = small * 1
    big_total = big * 5
    total = small_total + big_total
    ismod5 = goal % 5 == 0
    even5 = round(goal/5)
  
    if total < goal:
        return False
    if goal % 5 > small_total:
        return False
    return True