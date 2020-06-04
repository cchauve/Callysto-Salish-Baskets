# Function: Retrieves dictionary where keys are blocks and values are corresponding colors
# Input: String containing pattern and string of palette name
# Output: A dictionary containing color of each block
def pattern_dict(pattern_st, palette):

    col_dict = get_colors(palette)
    
    # Convert pattern string to list
    col_list = pattern_str_to_list(pattern_st)
    
    pattern_dictionary = {}
    
    # Define height and width of plot
    # Height is number of elements in pattern array (number of rows)
    # Width is number of elements of an element in pattern array (number of columns)
    height = len(col_list)
    width = len(col_list[0])
    
    for i in range(0, height):
        for j in  range(0, width ):
            
            # Define bottom left coordinate of block
            bottom_left = (j, i)
            
            # Define color of block
            color = col_dict[col_list[i][j]]

            # Create block and add to block's color to dictionary
            rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
            pattern_dictionary[rect] = [i, col_list[i][j]]
    
    return pattern_dictionary


# Function: Edit a given pattern by clicking
# Input: A string containing the pattern and string of palette name
# Output: Has no return; edits for pattern are stored in global character matrix called mod_pattern (modify pattern)
def edit(st, palette):
    
    # Get dictionary containing color of each block in pattern
    global blocks
    blocks = pattern_dict(st, palette)
    
    # Convert pattern string to array
    pattern = pattern_str_to_list(st)
    
    # Define height and width of pattern
    # Height is number of elements in pattern array (number of rows)
    # Width is number of elements of an element in pattern array (number of columns)
    height = len(pattern)
    width = len(pattern[0])
    
    # Set mod_pattern to original pattern array
    # Changes made to the pattern will be store in mod_pattern
    global mod_pattern
    mod_pattern = pattern

    
    # Function: Displays chosen palette 
    # Input: A string of palette name
    # Output: Has no return
    def plot_palette(palette):
        
        # Create figure for Palette
        fig = plt.figure(figsize=(8, 1), frameon=False)
        ax = fig.add_subplot(111, facecolor = '#ffffff')
        col_pos_dictionary = {}
        text_pal = fig.text(0,0, "", va="bottom", ha="left")
        
        # Create dictionary where the key is the position, size and color of a patch of color and value is position and color
        # Add the patch to the figure
        for x, color in enumerate(palette):
            col_pos_dictionary[(Rectangle((x, 0), 1, 1, facecolor = color))] = (x,color)
            ax.add_patch(Rectangle(((1.5*x), 0), 1, 1, facecolor = color, edgecolor = color, linewidth = 2))
        
        # Function: Selects color by clicking
        # Programmer Notes: This function has not gone through many edits since the time it was created and thus
        # improvements can be made. E.g. The for loop, which is used to locate which color the mouse is on, continues to run 
        # after it has found the color choice the user has selected.
        def color_picker(event):
            
            # Replots palette such that the square of the color chosen is larger than the other colors
            for x, color in enumerate(palette):
                col_pos_dictionary[(Rectangle((x, 0), 1, 1, facecolor = color))] = (x,color)
                ax.add_patch(Rectangle((1.5*x, 0), 1, 1, facecolor = color, edgecolor = 'white', linewidth = 10))

            
            # Run through the positions of the colors in palette and locate which color the mouse is on
            # Once color is found, set new_color to the color mouse was on
            for key in col_pos_dictionary:
                w,h = key.get_width(),key.get_height()
                x0,y0 = key.xy
                if 1.5*x0 <= event.xdata <= 1.5*x0 + w and y0 <= event.ydata <= y0 + h:
                    value = col_pos_dictionary[key]
                    position = value[0]
                    global new_color
                    new_color = value[1]
                    rect = Rectangle( (1.5*x0,y0), w,h, fill = False, facecolor = new_color, edgecolor = new_color, linewidth = 10)
                    ax.add_patch(rect)
                    
            plt.draw()
        
        # Connect the palette figure and color picking function through a clicking event 
        cid = fig.canvas.mpl_connect('button_press_event', color_picker)
        
        # Pattern plot settings
        ax.set_xlim((-0.1, 1.5*len(ori_p)+0.1))
        ax.set_ylim((-0.1, 1.1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")
        plt.show()
    
    plot_palette(palette)
    
    # Create figure for pattern plot
    fig = plt.figure( figsize = (6,4) )
    current_axis = plt.gca()

    # Function: Plot block with new color chosen
    def color_block(event):
        # The bottom left coordinate of each rectangular block is an ordered pair of positive integers
        # We floor the x any y positions of the mouse to figure out which block the mouse lies on
        x = math.floor(event.xdata)
        y = math.floor(event.ydata)
        
        # Create block with new color and add to figure
        rect = Rectangle( (x, y), 1,1 , fill = True, facecolor = new_color, edgecolor = "white", linewidth = 1)
        current_axis.add_patch(rect)
        
        # Get character to corresponding color chosen
        new_char = col_char_dict[new_color]
        
        # Replace character in mod_pattern array which new character -- update mod_pattern array
        mod_pattern[y][x] = new_char
   
    # Connect the pattern figure and color block function through a clicking event 
    cid = fig.canvas.mpl_connect('button_press_event', color_block)

    # Given string of palette name, get the colors in the palette and get characters corresponding to each color
    col_dict = get_colors(palette)
    col_char_dict = get_character(col_dict)
    
    # Add each block of the the original pattern to figure
    for key in blocks:
        current_axis.add_patch(key)
   
    # Pattern plot settings
    plt.xlim(0, width)
    plt.ylim(0, height)
    current_axis.axis('off')
    plt.show()

    
# Function: Edit a given pattern (string containing plain block characters '-') by clicking
# Input: A string containing the pattern and string of palette name
# Output: Has no return; edits for pattern are stored in global character matrix called create_pattern    
def create(st, palette):
    
    # Get dictionary containing color of each block in pattern
    global blocks
    blocks = pattern_dict(st, palette) 
    
    # Convert pattern string to array
    pattern = pattern_str_to_list(st)
    
    # Define height and width of pattern
    # Height is number of elements in pattern array (number of rows)
    # Width is number of elements in an element of pattern array (number of columns)
    height = len(pattern)
    width = len(pattern[0])
    
    # Set global create_pattern to original pattern array
    # Changes made to the pattern will be store in create_pattern 
    global create_pattern
    create_pattern = pattern

    # Function: Displays chosen palette 
    # Input: A string of palette name
    # Output: Has no return
    def plot_palette(palette):
        plt.ion()
        
        # Create figure for Palette
        fig = plt.figure(figsize=(8, 1), frameon=False)
        ax = fig.add_subplot(111, facecolor = '#ffffff')
        col_pos_dictionary = {}
        text_pal = fig.text(0,0, "", va="bottom", ha="left")
        
        # Create dictionary where the key is the position, size and color of a patch of color and value is position and color
        # Add the patch to the figure
        for x, color in enumerate(palette):
            col_pos_dictionary[(Rectangle((x, 0), 1, 1, facecolor = color))] = (x,color)
            ax.add_patch(Rectangle(((1.5*x), 0), 1, 1, facecolor = color, edgecolor = color, linewidth = 2))
        
        # Function: Selects color by clicking
        # Programmer Notes: This function has not gone through many edits since the time it was created and thus
        # improvements can be made. E.g. The for loop, which is used to locate which color the mouse is on, continues to run 
        # after it has found the color choice the user has selected.
        def color_picker(event):
            
            # Replots palette such that the square of the color chosen is larger than the other colors
            for x, color in enumerate(palette):
                col_pos_dictionary[(Rectangle((x, 0), 1, 1, facecolor = color))] = (x,color)
                ax.add_patch(Rectangle((1.5*x, 0), 1, 1, facecolor = color, edgecolor = 'white', linewidth = 10))

            tx = 'x=%f, y=%f' % (event.xdata, event.ydata) 
            
            # Run through the positions of the colors in palette and locate which color the mouse is on
            # Once color is found, set new_color to the color mouse was on
            for key in col_pos_dictionary:
                w,h = key.get_width(),key.get_height()
                x0,y0 = key.xy
                if 1.5*x0 <= event.xdata <= 1.5*x0 + w and y0 <= event.ydata <= y0 + h:
                    value = col_pos_dictionary[key]
                    position = value[0]
                    global new_color
                    new_color = value[1]
                    rect = Rectangle( (1.5*x0,y0), w,h, fill = False, facecolor = new_color, edgecolor = new_color, linewidth = 10)
                    ax.add_patch(rect)
                    
            plt.draw()
        
        # Connect the palette figure and color picking function through a clicking event 
        cid = fig.canvas.mpl_connect('button_press_event', color_picker)
        
        # Pattern plot settings
        ax.set_xlim((-0.1, 1.5*len(ori_p)+0.1))
        ax.set_ylim((-0.1, 1.1))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal")
        plt.show()
    
    plot_palette(palette)
    
    # Create figure for pattern plot
    fig = plt.figure( figsize = (6,4) )
    current_axis = plt.gca()

    # Function: Plot block with new color chosen
    def color_block(event):
        # The bottom left coordinate of each rectangular block is an ordered pair of positive integers
        # We floor the x any y positions of the mouse to figure out which block the mouse lies on
        x = math.floor(event.xdata)
        y = math.floor(event.ydata)
        
        # Create block with new color and add to figure
        rect = Rectangle( (x, y), 1,1 , fill = True, facecolor = new_color, edgecolor = "white", linewidth = 1)
        current_axis.add_patch(rect)
        
        # Get character to corresponding color chosen
        new_char = col_char_dict[new_color]
        
        # Replace character in create_pattern array which new character -- update create_pattern array
        create_pattern[y][x] = new_char
   
    # Connect the pattern figure and color block function through a clicking event 
    cid = fig.canvas.mpl_connect('button_press_event', color_block)

    # Given string of palette name, get the colors in the palette and get characters corresponding to each color
    col_dict = get_colors(palette)
    col_char_dict = get_character(col_dict)
    
    # Add each block of the the original pattern to figure
    for key in blocks:
        current_axis.add_patch(key)
   
    # Pattern plot settings
    plt.xlim(0, width)
    plt.ylim(0, height)
    current_axis.axis('off')
    plt.show()

    
# Programmer Note: The two functions below are used to edit an existing pattern or create a new pattern. They are almost identical in code. Originally, only one function was necessary however when called in the Notebook that edits/create patterns, changes made to the mod_pattern matrix also affected the create_matrix and vice versa.
    
