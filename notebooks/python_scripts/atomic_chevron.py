# Function: For Chevron Pattern - Creates a single row of the Chevron Pattern
# Input: The height and number of colors used for the Chevron as well as the row number of the row to be created
# Output: A string containing a row of a Chevron Pattern
def create_row(height, num_colors, row_num):
    
    # Each row of the Chevron pattern contains a certain number of plain blocks at the start of the row
    st_out = (2*row_num)*'-'
    
    # From the first color to second last, add two colored blocks followed by three plain blocks 
    for i in range(num_colors-1):
        st_out += 2*color_list[i] + 3*'-'
        
    # For the last color, add two colored blocks followed by the number of plain blocks the row should end with
    st_out += 2*color_list[num_colors-1]+ 2*(height-row_num-1)*'-'
    return(st_out)
    
# Function: Create Chevron Pattern
# Input: The height and number of colors used for the Chevron
# Output: A string of a Chevron pattern    
def build_atomic_chevron(height, num_colors):
    row = ''
    st_out = ''
    
    # Create the Chevron row by row
    for i in range(height):
        row = create_row(height, num_colors, i)
        st_out += row + '\n'
        
    return(st_out)