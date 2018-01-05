
# coding: utf-8

# In[1]:


my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 6,
    'height': 3,

}


# In[9]:


def find_x_overlap(rect1, rect2):
    if rect2["left_x"]< rect1["left_x"]:
        left_rect = rect2
        right_rect = rect1
    else:
        left_rect = rect1
        right_rect = rect2
        
    left_x_one = left_rect["left_x"]
    right_x_one = left_rect["left_x"] +left_rect["width"]
    
    left_x_two = right_rect["left_x"]
    right_x_two = right_rect["left_x"] + right_rect["width"]
    
    if right_x_one > left_x_two and right_x_one < right_x_two:
        x_overlap = right_x_one - left_x_two
    
    elif left_x_one < left_x_two and right_x_one > right_x_two:
        x_overlap = left_rect["width"]
    
    elif right_x_one <= left_x_two:
        return 0
    
    return x_overlap


# In[10]:


my_rectangle_2 = {

    # coordinates of bottom-left corner
    'left_x': 4,
    'bottom_y': 2,

    # width and height
    'width': 6,
    'height': 3,

}


# In[11]:


find_x_overlap(my_rectangle, my_rectangle_2)


# In[12]:


def find_y_overlap(rect1, rect2):
    if rect2["bottom_y"]< rect1["bottom_y"]:
        bottom_rect = rect2
        top_rect = rect1
    else:
        bottom_rect = rect1
        top_rect = rect2
        
    bottom_y_one = bottom_rect["bottom_y"]
    top_y_one = bottom_rect["bottom_y"] +bottom_rect["height"]
    
    bottom_y_two = top_rect["bottom_y"]
    top_y_two = top_rect["bottom_y"] + top_rect["height"]
    
    if top_y_one > bottom_y_two and top_y_two > top_y_one:
        y_overlap = top_y_one - bottom_y_two
    
    elif bottom_y_one  < bottom_y_two and top_y_one > top_y_two:
        y_overlap = left_rect["height"]
    
    elif bottom_y_two >= top_y_one:
        return 0
    
    return y_overlap
    


# In[ ]:


## Solution

ef find_range_overlap(point1, length1, point2, length2):

    # find the highest start point and lowest end point.
    # the highest ("rightmost" or "upmost") start point is
    # the start point of the overlap.
    # the lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # return null overlap if there is no overlap
    if highest_start_point >= lowest_end_point:
        return (None, None)

    # compute the overlap length
    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)

def find_rectangular_overlap(rect1, rect2):

    # get the x and y overlap points and lengths
    x_overlap_point, overlap_width  = find_range_overlap(
        rect1['left_x'], rect1['width'],  rect2['left_x'], rect2['width'])
    y_overlap_point, overlap_height = find_range_overlap(
        rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])

    # return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    return {
        'left_x': x_overlap_point,
        'bottom_y': y_overlap_point,
        'width': overlap_width,
        'height': overlap_height,
    }

