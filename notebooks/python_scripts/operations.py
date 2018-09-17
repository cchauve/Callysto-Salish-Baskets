# Function: flips a pattern by mirror image
# Input: 
    # string - string pattern
    # direction - flip horizontally or vertically
# Ouput: modified string pattern

def flip(st, direction):
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    
    st_out = ''
    
    if (direction == 'Flip Horizontally'):
        row_strings = row_strings[::-1]
        for row in row_strings:
            st_out += row + '\n' 

        
    else:
        for row in row_strings:
            st_out += row[::-1] + '\n'
        
    return(st_out)

# Function: reflects pattern vertically 
# Input: 
    # st - string pattern
    # space - positive integer value, gap between original pattern and reflected pattern
    # direction - 'Reflect Left' or 'Reflect Right', direction to perform vertical reflection
# Output:
    # modified string pattern
    
def reflect_v(st, space, direction):
    
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    space_st = ""
    
    if (direction == "Reflect Left"): 
       
        # Add spaces on the left of pattern
        for row in row_strings:
            row = space*"-" + row 
            space_st = space_st + row + "\n"
            
        new_row_strings = space_st.split("\n")
        reflected_row_strings = new_row_strings[:len(row_strings)]
        st_out = ""
        
        for row in reflected_row_strings:
            
            if space >= 0:

                row = row[::-1] + row
            
            # Overlap
            else:
                row = row[:0:-1] + row
                
            st_out = st_out + row + "\n"
    
    else:
        # Add spaces on the right of pattern
        for row in row_strings:
            row = row + space*"-"
            space_st = space_st + row + "\n"
            
        new_row_strings = space_st.split("\n")
        reflected_row_strings = new_row_strings[:len(row_strings)]
        st_out = ""
         
        for row in reflected_row_strings:
            
            if space >= 0:

                row = row + row[::-1]
            
            # Overlap
            else: 
                row = row + row[len(row_strings[0])-2::-1]
                
            st_out = st_out + row + "\n"

    return st_out

# Function: reflect pattern horizontally
# Input:
    # st - pattern string
    # spacing - positive integer value, gap between original and reflected pattern
    # direction - 'Reflect above' or 'Reflect below', direction to reflect horizontally
# Output: modified string pattern

def reflect_h(st, spacing, direction):
    row_strings = st.split("\n")
    reflect_st = ""
    
    if spacing >= 0 :
        row_strings = row_strings[:-1]
        reflected_row_strings = list(reversed(row_strings))
        row_length = len(row_strings[0])

        # Create string for spacing area
        spacing_st = 2*spacing*(row_length*'-' + '\n')

        for row in reflected_row_strings:
            reflect_st = reflect_st + row + "\n"

        if (direction == 'Reflect Above'):
            st_out = reflect_st + spacing_st + st
        else:
            st_out = st + spacing_st + reflect_st
    
    # Overlap
    else:
        row_strings = row_strings[:-1]        
        reflected_row_strings = list(reversed(row_strings[1:]))
        
        for row in reflected_row_strings:
            reflect_st = reflect_st + row + "\n"

        if (direction == 'Reflect Above'):
            st_out = reflect_st + st
        else:
            st_out = st + reflect_st
       
    return(st_out)

# Function: stack string pattern horizontally (by copying original string pattern and placing it above original string pattern)
# Input: 
    # st - string pattern
    # space - positive integer, space between original pattern and copied pattern
# Output: modified string pattern

def stack_h(st, space):
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    
    st_out = ''
    
    for row in row_strings:
        st_out += row + space*'-' + row + '\n'

     
    return(st_out)

# Function: stack string pattern horizontally (by copying original string pattern and placing it to the right of original string pattern)
# Input: 
    # st - string pattern
    # space - positive integer, space between original pattern and copied pattern
# Output: modified string pattern

def stack_v(st, space):
    row_strings = st.split("\n")
    row_length = len(row_strings[0])
    
    spacing_st = space*(row_length*'-' + '\n')
    
    st_out = st + spacing_st + st
    
    return(st_out)

# Function: copies original string pattern top left or bottom right direction
# Input:
    # st - string pattern
    # space - positive integer, space between original pattern and copied pattern 
# Output: modified string pattern

def stack_d(st, space, direction):    
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    row_height = len(row_strings)
    row_length = len(row_strings[0])
    
    left_pattern = ''
    right_pattern = ''
    
    st_out = ''
    
    spacing_st = (row_length + space)*'-' 
    
    for row in row_strings:
        left_pattern += row + spacing_st + '\n'
        right_pattern += spacing_st + row + '\n'

    if (direction == 'Stack Left'):
        st_out += left_pattern + right_pattern
    else:
        st_out += right_pattern + left_pattern
        
    return(st_out)

# Function: joins two string pattern horizontally
# Input:
    # st1, st2 - string patterns
    # space - positive integer, gap between two joined patterns
# Output: modified string pattern

def join_patterns(st1, st2, space):
    pattern_1 = st1.split("\n")
    pattern_1 = pattern_1[:-1]
    pattern_2 = st2.split("\n")
    pattern_2 = pattern_2[:-1]
    
    height = max(len(pattern_1), len(pattern_2))
    space_to_add_p1 = math.ceil( (height - len(pattern_1))/2 ) 
    space_to_add_p2 = math.ceil( (height - len(pattern_2))/2 )
    
    p1 = add_basket_space(st1, space_to_add_p1, 0)
    p2 = add_basket_space(st2, space_to_add_p2, 0)
    
    pattern_1 = p1.split("\n")
    pattern_1 = pattern_1[:-1]
    pattern_2 = p2.split("\n")
    pattern_2 = pattern_2[:-1]

    st_out = ''
    
    for a,b in zip(pattern_1, pattern_2):
        st_out += a + space*'-' + b + '\n'
    
    return(st_out)
    