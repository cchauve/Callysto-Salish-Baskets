# Function: Converts Pattern string into array
# Input: Pattern string
# Ouput: A H x W array containing the pattern where H is the height of the pattern and W is the width
def pattern_str_to_list( st ):
    # Split pattern string into appropriate rows and remove last (empty) row
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    
    # Reverse pattern string
    row_strings = row_strings[::-1]

    output_list = []

    # Convert each row into a list
    # Each character in the pattern string has a unique index in the output array
    for row in row_strings:
        char_split = list(row)
        output_list.append(char_split)

    return output_list

# Function: Converts pattern array to string
# Input: Pattern array
# Ouput: A string containing the pattern 
def list_to_pattern_str(lst):
    st_out = ''
    
    # Add each element in array to string output
    # Add new line character at new row
    for row in lst[::-1]:
        for ch in row:
            st_out += ch
            
        st_out += '\n'
            
    return st_out

# Function: Adds blank weaves around border of pattern
# Input: Pattern string and value of space/blank weaves to add
# Ouput: String containing given pattern string and added blank weaves
def add_basket_space(st, add_h, add_w):
    # Split pattern string into appropriate rows and remove last (empty) row
    row_strings = st.split("\n")
    row_strings = row_strings[:-1]
    
    pattern_width = len(row_strings[0])
    st_out = ''
    
    # Add blank weave characters to sides of pattern
    for row in row_strings:
        st_out += add_w*'-' + row + add_w*'-' + '\n'
    
    # Add blank weave characters above pattern and new added sides
    space = add_h*((pattern_width + 2*add_w)*'-'+ '\n')
    
    st_out = space + st_out + space
    return(st_out)
         
# Function: For Rectangular Basket Only - Calculates the amount of space required to match the dimensions of each face
# Input: 4 strings containing patterns
# Output: A 4x2 array containing the amount of space to add on the top/bottom and side of each face
def space_calculator(front, back, left, right):
    
    # Split each pattern string into appropriate rows and remove last (empty) row 
    f = front.split("\n")
    b = back.split("\n")
    l = left.split("\n")
    r = right.split("\n")
    
    f = f[:-1]
    b = b[:-1]
    l = l[:-1]
    r = r[:-1]
    
    # Define height, length, and width
    # Need front and back to have same dimensions and left and right to have same dimensions
    height = max(len(f), len(b), len(l), len(r))
    length = max(len(f[0]), len(b[0])) + 10
    width = max(len(l[0]), len(r[0])) + 10
      
    # Get dimensions of patterns and initialize array to hold values for spaces to add
    current_dim = [[len(f), len(f[0])], [len(b), len(b[0])], [len(l), len(l[0])], [len(r), len(r[0])]]
    spaces_to_add = [None]*4
    
    for side in range(len(current_dim)):
    
        # Side is front or back 
        if side <= 1:
            spaces_to_add[side] = [math.ceil((height - current_dim[side][0])/2), math.ceil((length - current_dim[side][1])/2)]
         
        # Side is left or right
        else:
            spaces_to_add[side] = [math.ceil((height - current_dim[side][0])/2), math.ceil((width - current_dim[side][1])/2)]

    return(spaces_to_add)

# Function: Plots motif in 2D
# Input: Pattern and palette colors
# Output: 2D plot of patten and additional spaces/blank weave for visual purposes
def plot_motif_2D(pattern_st, palette):
    
    # Create figure
    fig = plt.figure( figsize = (6,4) )
    current_axis = fig.add_subplot(111)
    
    # Get color palette
    col_dict = get_colors(palette)

    # Add space to the side of pattern (for visual purposes only)
    nonpattern_space = 10
    st = add_basket_space(pattern_st, 0, nonpattern_space)
    col_list = pattern_str_to_list(st)
    
    # Define height and width of plot
    height = len(col_list)
    width = len(col_list[0])
    
    for i in range(0, height):
        for j in  range(0, width ):
            
            # Define bottom left coordinate of weave
            bottom_left = (j, i)
            
            # Define color of weave
            color = col_dict[col_list[i][j]]

            # Create weave and add to plot
            rect = Rectangle( bottom_left, 1, 1, fill = True, facecolor = color, edgecolor = "white", linewidth = 1)
            current_axis.add_patch(rect)
    
    plt.xlim(-0.25 , width + 0.25)
    plt.ylim(-0.25 , height)
    current_axis.axis('off')
    plt.show()

# Function: Plot rectanglular basket in 3D
# Input: Patterns for 4 faces of basket and color palette
# Output: Plot of the 4 faces of basket and bottom
def plot_rect_basket(front, back, left, right, palette):
    # Create figure
    fig = plt.figure(figsize = (14, 14))
    ax = fig.add_subplot(221, projection='3d', facecolor = '#ffffff')
    ax2 = fig.add_subplot(222, projection='3d', facecolor = '#ffffff')
    ax3 = fig.add_subplot(223, projection='3d', facecolor = '#ffffff')
    ax4 = fig.add_subplot(224, projection='3d', facecolor = '#ffffff')

    # Get color palette
    col_dict = get_colors(palette)

    # Calculate the amount of space needed to make dimensions of faces match
    space_values = space_calculator(front, back, left, right)

    # Add corresponding spaces to pattern strings and convert strings to array
    f = pattern_str_to_list( add_basket_space(front, space_values[0][0], space_values[0][1]) )
    b = pattern_str_to_list( add_basket_space(back, space_values[1][0], space_values[1][1]) )
    l = pattern_str_to_list( add_basket_space(left, space_values[2][0], space_values[2][1]) )
    r = pattern_str_to_list( add_basket_space(right, space_values[3][0], space_values[3][1]) )

    # Initialize height, length and width of basket
    height = min(len(f), len(b), len(l), len(r))
    length = min(len(f[0]), len(b[0]))
    width = min(len(l[0]), len(r[0]))

    # Define number of rows and number of columns for the front/back and left/right faces
    rows = height + 1
    cols_fb = length + 1
    cols_lr = width + 1

    # Define the size the basket tapers in by
    indent = max(width, length)/5

    # Define x,y,z values to create coordinates of blocks
    x = []
    for i in range(0, rows):
        x.append(np.linspace(indent - i, length - indent + i, cols_fb))

    y = []
    for i in range(0, rows):
        y.append(np.linspace(indent - i, width - indent + i, cols_lr))

    z = np.linspace(0, height, rows)

    # Initialize size of basket rim
    basket_rim = (z[1]-z[0])/2

    for i in range(0, height):
        # Plot front and back faces of rectangular prism
        for j in range(0, length):

            # FRONT FACE

            # Define coordinates for 4 corners of block
            bottom_left = [x[i][j], indent-i, z[i]]
            top_left = [x[i+1][j], indent-(i+1), z[i+1]]
            top_right = [x[i+1][j+1], indent-(i+1), z[i+1]]
            bottom_right = [x[i][j+1], indent-i, z[i]]

            # Create block, color accordingly and add to plot
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect2 = a3.art3d.Poly3DCollection([rect_coords])
            rect3 = a3.art3d.Poly3DCollection([rect_coords])
            rect4 = a3.art3d.Poly3DCollection([rect_coords])

            color = col_dict[f[i][j]]
            rect.set_color(color)
            rect.set_edgecolor('#ad8a54')
            rect2.set_color(color)
            rect2.set_edgecolor('#ad8a54')
            rect3.set_color(color)
            rect3.set_edgecolor('#ad8a54')
            rect4.set_color(color)
            rect4.set_edgecolor('#ad8a54')

            ax.add_collection3d(rect)
            ax2.add_collection3d(rect2)
            ax3.add_collection3d(rect3)
            ax4.add_collection3d(rect4)

            # BACK FACE

            # Define coordinates for 4 corners of block
            bottom_left = [x[i][j], width - indent + i, z[i]]
            top_left = [x[i+1][j], width - indent + (i+1), z[i+1]]
            top_right = [x[i+1][j+1], width - indent + (i+1), z[i+1]]
            bottom_right = [x[i][j+1], width - indent + i, z[i]]

            # Create block, color accordingly and add to plot
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect2 = a3.art3d.Poly3DCollection([rect_coords])
            rect3 = a3.art3d.Poly3DCollection([rect_coords])
            rect4 = a3.art3d.Poly3DCollection([rect_coords])

            color = col_dict[b[i][j]]
            rect.set_color(color)
            rect.set_edgecolor('#ad8a54')

            rect2.set_color(color)
            rect2.set_edgecolor('#ad8a54')

            rect3.set_color(color)
            rect3.set_edgecolor('#ad8a54')

            rect4.set_color(color)
            rect4.set_edgecolor('#ad8a54')

            ax.add_collection3d(rect)
            ax2.add_collection3d(rect2)
            ax3.add_collection3d(rect3)
            ax4.add_collection3d(rect4)

            if i == rows - 2:

                # FRONT FACE
                bottom_left = [x[i+1][j], indent-(i+1), z[i+1]]
                bottom_right = [x[i+1][j+1], indent-(i+1), z[i+1]]
                top_left = [x[i+1][j], indent-(i+1), z[i+1] + basket_rim]
                top_right = [x[i+1][j+1], indent-(i+1), z[i+1]+ basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords]) 
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')

                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect2.set_color('#af8a52')
                rect2.set_edgecolor('#87693c')

                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect3.set_color('#af8a52')
                rect3.set_edgecolor('#87693c')

                rect4 = a3.art3d.Poly3DCollection([rect_coords])
                rect4.set_color('#af8a52')
                rect4.set_edgecolor('#87693c')

                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)

                # BACK FACE
                bottom_left = [x[i+1][j], width - indent + (i+1), z[i+1]]
                bottom_right = [x[i+1][j+1], width - indent + (i+1), z[i+1]]
                top_left = [x[i+1][j], width - indent + (i+1), z[i+1] + basket_rim]
                top_right = [x[i+1][j+1], width - indent + (i+1), z[i+1]+ basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')

                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect2.set_color('#af8a52')
                rect2.set_edgecolor('#87693c')

                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect3.set_color('#af8a52')
                rect3.set_edgecolor('#87693c')

                rect4 = a3.art3d.Poly3DCollection([rect_coords])
                rect4.set_color('#af8a52')
                rect4.set_edgecolor('#87693c')

                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)

        # Plot left and right faces of rectangular prism
        for j in range(0, width):

            # LEFT FACE

            # Define coordinates for 4 corners of weave
            bottom_left = [indent - i, y[i][j], z[i]]
            top_left = [indent - (i+1), y[i+1][j], z[i+1]]
            top_right = [indent - (i+1), y[i+1][j+1], z[i+1]]
            bottom_right = [indent - i, y[i][j+1], z[i]]

            # Create weave, color accordingly and add to plot
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect2 = a3.art3d.Poly3DCollection([rect_coords])
            rect3 = a3.art3d.Poly3DCollection([rect_coords])
            rect4 = a3.art3d.Poly3DCollection([rect_coords])
          
            color = col_dict[l[i][j]]
            rect.set_color(color)
            rect2.set_color(color)
            rect3.set_color(color)
            rect4.set_color(color)

            rect.set_edgecolor('#ad8a54')
            rect2.set_edgecolor('#ad8a54')
            rect3.set_edgecolor('#ad8a54')
            rect4.set_edgecolor('#ad8a54')

            ax.add_collection3d(rect)
            ax2.add_collection3d(rect2)
            ax3.add_collection3d(rect3)
            ax4.add_collection3d(rect4)
           
           # RIGHT FACE
            
            # Define coordinates for 4 corners of weave
            bottom_left = [length - indent + i, y[i][j], z[i]]
            top_left = [length - indent + (i+1), y[i+1][j], z[i+1]]
            top_right = [length - indent + (i+1), y[i+1][j+1], z[i+1]]
            bottom_right = [length - indent + i, y[i][j+1], z[i]]
            
            # Create weave, color accordingly and add to plot
            rect_coords = [bottom_left, top_left, top_right, bottom_right]
            rect = a3.art3d.Poly3DCollection([rect_coords])
            rect2 = a3.art3d.Poly3DCollection([rect_coords])
            rect3 = a3.art3d.Poly3DCollection([rect_coords])
            rect4 = a3.art3d.Poly3DCollection([rect_coords])

            color = col_dict[r[i][j]]
            rect.set_color(color)
            rect2.set_color(color)
            rect3.set_color(color)
            rect4.set_color(color)

            rect.set_edgecolor('#ad8a54')
            rect2.set_edgecolor('#ad8a54')
            rect3.set_edgecolor('#ad8a54')
            rect4.set_edgecolor('#ad8a54')

            ax.add_collection3d(rect)
            ax2.add_collection3d(rect2)
            ax3.add_collection3d(rect3)
            ax4.add_collection3d(rect4)
           
           # BASKET RIM
            if i == rows - 2:

                # LEFT FACE
                bottom_left = [indent - (i+1), y[i+1][j], z[i+1]]
                bottom_right = [indent - (i+1), y[i+1][j+1], z[i+1]]
                top_left = [indent - (i+1), y[i+1][j], z[i+1] + basket_rim]
                top_right = [indent - (i+1), y[i+1][j+1], z[i+1] + basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                
                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect2.set_color('#af8a52')
                rect2.set_edgecolor('#87693c')
                
                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect3.set_color('#af8a52')
                rect3.set_edgecolor('#87693c')

                rect4 = a3.art3d.Poly3DCollection([rect_coords])
                rect4.set_color('#af8a52')
                rect4.set_edgecolor('#87693c')

                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)
               
               # RIGHT FACE
                bottom_left = [length - indent + (i+1), y[i+1][j], z[i+1]]
                bottom_right = [length - indent + (i+1), y[i+1][j+1], z[i+1]]
                top_left = [length - indent + (i+1), y[i+1][j], z[i+1] + basket_rim]
                top_right = [length - indent + (i+1), y[i+1][j+1], z[i+1] + basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')
                
                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect2.set_color('#af8a52')
                rect2.set_edgecolor('#87693c')
                
                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect3.set_color('#af8a52')
                rect3.set_edgecolor('#87693c')

                rect4 = a3.art3d.Poly3DCollection([rect_coords])
                rect4.set_color('#af8a52')
                rect4.set_edgecolor('#87693c')
                
                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)

    # Plot bottom
    bottom_left = [x[0][0], y[0][0], 0]
    bottom_right = [x[0][-1], y[0][0], 0]
    top_left = [x[0][0], y[0][-1], 0]
    top_right = [x[0][-1], y[0][-1], 0]

    rect_coords = [bottom_left, top_left, top_right, bottom_right]
    
    rect = a3.art3d.Poly3DCollection([rect_coords])
    rect.set_color('#af8a52')
    rect.set_edgecolor('#87693c')
   
    rect2 = a3.art3d.Poly3DCollection([rect_coords])
    rect2.set_color('#af8a52')
    rect2.set_edgecolor('#87693c')


    rect3 = a3.art3d.Poly3DCollection([rect_coords])
    rect3.set_color('#af8a52')
    rect3.set_edgecolor('#87693c')
    
    rect4 = a3.art3d.Poly3DCollection([rect_coords])
    rect4.set_color('#af8a52')
    rect4.set_edgecolor('#87693c')
    
    ax.add_collection3d(rect)
    ax2.add_collection3d(rect2)
    ax3.add_collection3d(rect3)
    ax4.add_collection3d(rect4)

    # Settings of plot
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim(-.25, 1.1*(length - indent + rows))
    ax.set_ylim(-.25, 1.1*(width - indent + rows))
    ax.set_zlim(-.25, height)
    ax.axis('off')

    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')
    ax2.set_xlim(-.25, 1.1*(length - indent + rows))
    ax2.set_ylim(-.25, 1.1*(width - indent + rows))
    ax2.set_zlim(-.25, height)
    ax2.axis('off')

    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('z')
    ax3.set_xlim(-.25, 1.1*(length - indent + rows))
    ax3.set_ylim(-.25, 1.1*(width - indent + rows))
    ax3.set_zlim(-.25, height)
    ax3.axis('off')

    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')
    ax4.set_xlim(-.25, 1.1*(length - indent + rows))
    ax4.set_ylim(-.25, 1.1*(width - indent + rows))
    ax4.set_zlim(-.25, height)
    ax4.axis('off')

    #Rotate the plots
    camera_angle = ax.azim
    ax2.view_init(azim = camera_angle + 90)
    ax3.view_init(azim = camera_angle + 180)
    ax4.view_init(azim = camera_angle + 270)

    plt.show()

def plot_circ_basket(pattern_st, palette):
    # Create figure
    fig = plt.figure(figsize = (14, 14))
    ax = fig.add_subplot(221, projection='3d', facecolor = '#ffffff')
    ax2 = fig.add_subplot(222, projection='3d', facecolor = '#ffffff')
    ax3 = fig.add_subplot(223, projection='3d', facecolor = '#ffffff')
    ax4 = fig.add_subplot(224, projection='3d', facecolor = '#ffffff')

    # Get colors and convert string to array
    col_dict = get_colors(palette)
    col_list = pattern_str_to_list(pattern_st)

    # Initialize number of rows and columns and radius of bottom and top of basket
    rows = len(col_list)
    cols = len(col_list[0])
    min_radius = 2
    max_radius = 5

    # Define points for coordinates of weaves
    theta = np.linspace(0, 2*np.pi, cols+1)
    z = np.linspace(min_radius, max_radius, rows+1)
    theta, R = np.meshgrid(theta, z)

    X = R * np.cos(theta)
    Y = R * np.sin(theta)
    Z = np.sqrt(X**2 + Y**2) - 1

    # Initialize size of basket rim
    basket_rim = (z[1] - z[0])/2

    for i in range(0, rows+1):
        for j in range(0, cols):

            # BASKET RIM
            if i == rows:
                bottom_left = [X[i][j], Y[i][j], Z[i][j]]
                bottom_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]]
                top_left = [X[i][j], Y[i][j], Z[i][j] + basket_rim]
                top_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]+ basket_rim]

                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect4 = a3.art3d.Poly3DCollection([rect_coords])

                rect.set_color('#af8a52')
                rect.set_edgecolor('#87693c')

                rect2.set_color('#af8a52')
                rect2.set_edgecolor('#87693c')

                rect3.set_color('#af8a52')
                rect3.set_edgecolor('#87693c')

                rect4.set_color('#af8a52')
                rect4.set_edgecolor('#87693c')

                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)

            # PATTERN
            else:

                # Define coordinates for 4 corners of weave
                bottom_left = [X[i][j], Y[i][j], Z[i][j]]
                top_left = [X[i+1][j], Y[i+1][j], Z[i+1][j]]
                top_right = [X[i+1][j+1], Y[i+1][j+1], Z[i+1][j+1]]
                bottom_right = [X[i][j+1], Y[i][j+1], Z[i][j+1]]

                # Create weave, color accordingly and add to plot
                rect_coords = [bottom_left, top_left, top_right, bottom_right]
                rect = a3.art3d.Poly3DCollection([rect_coords])
                rect2 = a3.art3d.Poly3DCollection([rect_coords])
                rect3 = a3.art3d.Poly3DCollection([rect_coords])
                rect4 = a3.art3d.Poly3DCollection([rect_coords])

                color = col_dict[col_list[i][j]]
                rect.set_color(color)
                rect.set_edgecolor('#6d5634')

                rect2.set_color(color)
                rect2.set_edgecolor('#6d5634')

                rect3.set_color(color)
                rect3.set_edgecolor('#6d5634')

                rect4.set_color(color)
                rect4.set_edgecolor('#6d5634')

                ax.add_collection3d(rect)
                ax2.add_collection3d(rect2)
                ax3.add_collection3d(rect3)
                ax4.add_collection3d(rect4)

    # Plot bottom
    bottom_verts = [list(zip(X[0], Y[0], [1]*len(X[0])))]
    bottom = a3.art3d.Poly3DCollection(bottom_verts)
    bottom.set_color('#af8a52')
    bottom.set_edgecolor('#87693c')

    bottom2 = a3.art3d.Poly3DCollection(bottom_verts)
    bottom2.set_color('#af8a52')
    bottom2.set_edgecolor('#87693c')

    bottom3 = a3.art3d.Poly3DCollection(bottom_verts)
    bottom3.set_color('#af8a52')
    bottom3.set_edgecolor('#87693c')

    bottom4 = a3.art3d.Poly3DCollection(bottom_verts)
    bottom4.set_color('#af8a52')
    bottom4.set_edgecolor('#87693c')

    ax.add_collection3d(bottom)
    ax2.add_collection3d(bottom2)
    ax3.add_collection3d(bottom3)
    ax4.add_collection3d(bottom4)

    # Plot settings
    ax.set_xlim(-max_radius, max_radius)
    ax.set_ylim(-max_radius, max_radius)
    ax.set_zlim(0, max_radius-1)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.axis('off')

    ax2.set_xlim(-max_radius, max_radius)
    ax2.set_ylim(-max_radius, max_radius)
    ax2.set_zlim(0, max_radius-1)
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('z')
    ax2.axis('off')

    ax3.set_xlim(-max_radius, max_radius)
    ax3.set_ylim(-max_radius, max_radius)
    ax3.set_zlim(0, max_radius-1)
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('z')
    ax3.axis('off')

    ax4.set_xlim(-max_radius, max_radius)
    ax4.set_ylim(-max_radius, max_radius)
    ax4.set_zlim(0, max_radius-1)
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('z')
    ax4.axis('off')

    #Rotate the plots
    camera_angle = ax.azim
    ax2.view_init(azim = camera_angle + 90)
    ax3.view_init(azim = camera_angle + 180)
    ax4.view_init(azim = camera_angle + 270)

    plt.show()
