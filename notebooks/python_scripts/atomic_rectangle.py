# For the Broken Line Motif, let us divide the motif into 3 parts: The Top Vertical, the Middle Horizontal, 
# and Bottom Vertical.
# The Broken Line Motif is created in a rectangular form. That is, the Top Vertical and Bottom Vertical pieces 
# consists of plain blocks to the left and right of the pieces, respectively.

color_list = list(string.ascii_lowercase)

# Function: For Broken Line Motif - Creates the Top Vertical
# Input: The height of the Top Vertical and the width and number of colors used on the Broken Line motif
# Output: A string of the Top Vertical
def height_1(height, width, num_colors):

    row = ""
    st = ""
    
    # For number of colors desired, create string consisting of 2 blocks for each color
    # Ex. 'aabbccdd' when number of colors equals 4
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    # Add the plain blocks at the beginning of each row
    for i in range(height):
        
        st = st + width*"-" + row + "\n"
        
    return st

# Function: For Broken Line Motif - Creates the Bottom Vertical
# Input: The height of the Bottom Vertical and the width and number of colors used on the Broken Line motif
# Output: A string of the Top Vertical
def height_2(height, width, num_colors):

    row = ""
    st = ""
    
    # For number of colors desired, create string consisting of 2 blocks for each color
    # Ex. 'aabbccdd' when number of colors equals 4
    for i in range(num_colors):
        
        row = row + 2*color_list[i]
    
    # Add the plain blocks at the end of each row
    for i in range(height):
        
        st = st + row  + width*"-" + "\n"
        
    return st

# Function: For Broken Line Motif - Creates the Middle Horizontal
# Input: The 'width' and number of colors of the Broken Line motif 
# Output: A string containing the Middle Horizontal piece
def width(wid, num_colors):

    row = ""    
    st = ""
    
    # For number of colors desired, create string consisting of 2 blocks for each color
    # Ex. 'aabbccdd' when number of colors equals 4
    for i in range(num_colors): 
        row = row + 2*color_list[i]
    
    # Create Middle Horizontal piece row by row
    for i in range(num_colors):
        left_st = row[:2*i]
        right_st = row[2*i:]
        
        st = st + left_st + wid*color_list[i] + right_st + "\n"

    return st


# Function: Creates Broken Line Motif
# Input: Height of Top Vertical, height of Bottom Vertical, Width of Broken Line Motif and number of colors
# Output: A string containing the Broken Line pattern
def build_atomic_rect(h1, h2, wid, num_colors):
    
    # Define pattern strings for Top Vertical, Bottom Vertical and Middle Horizontal
    h1 = height_1(h1, wid, num_colors)
    h2 = height_2(h2, wid, num_colors)
    w = width(wid, num_colors)
    
    # Join strings
    st = h1 + w + h2
    
    return(st)   

