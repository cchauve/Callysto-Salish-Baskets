color_list = list(string.ascii_lowercase)

# Function: Creates a single row in the triangle motif given a row number
# Input: Height and number of colors of the triangle motif and the row number of the desired row to be created
# Output: A string containing a row in the triangle motif
def create_tri_row(height, num_colors, row_num):
    col_block = ''
    st_out = ''
    
    # For number of colors desired, create string consisting of 2 blocks for each color
    # Ex. 'aabbccdd' when number of colors equals 4
    for i in range(num_colors):
        col_block = col_block + 2*color_list[i]
     
    # Note the length of each row is 2+4*row_num
    # Define the string containing the plain blocks that exists at the beginning and end of a row
    # Define the string containing the plain blocks in between the colored blocks of each row
    plain_blocks = (2*(height - row_num - 1))*'-'
    blocks_between = (2 + 4*row_num - 2*len(col_block))*'-'    
    
    
    # When the row number is larger or equal than the number of colors, create the desired row by adding plain
    # blocks at the beginning, the color block, the plain blocks inside the triangle, the color block reversed, and plain
    # blocks again
    if (row_num >= num_colors):

        st_out += plain_blocks + col_block + blocks_between + col_block[::-1] + plain_blocks
        
    
    # When the row number is smaller than the number of colors, create the desired row by taking a part of the color block
    # previously initialized, reverse it and add plain blocks to the beginning and end of these 2 blocks
    else:
        col_block = col_block[:2*(row_num + 1) - 1]
        block_reversed = col_block[::-1]
        st_out += plain_blocks + col_block + block_reversed + plain_blocks

    
    return(st_out)


# Function: Creates Triangle Motif
# Input: Height and number of colors of the triangle
# Output: A string containing the Triangle motif
def build_atomic_tri(height, num_colors):
    row = ''
    st_out = ''
    
    # Create the triangle motif row by row
    for i in range(height):
        row = create_tri_row(height, num_colors, i) + '\n'
        st_out = row + st_out
    
    return (st_out)
