global pattern_files, new_pattern, file_name, save_button
global files_selected
files_selected = False

def rerun_cell(ev):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,\
    IPython.notebook.get_selected_index()+2)'))
    
def generate_pattern_dir_listing():
    global pattern_files
    
    pattern_files = os.listdir('./patterns/')
    
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
        
    if 'dirList' in pattern_files:
        pattern_files.remove('dirList')
        
    pattern_files_string = ", ".join(pattern_files)
    
    file = open("./patterns/dirList", "w")    
    file.write(pattern_files_string)
    file.close()

## called by JS element
def save_edited_pattern(file_name2, new_pattern):
    global pattern_files
    
    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    # Remove checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
    
    # Write edited pattern into text file
    if (file_name2 != ''):
        file = open("./patterns/" + file_name2, "w")
        
        file.write(new_pattern)
        file.close()
        
    generate_pattern_dir_listing()

def save(pattern_string):
    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")
    
    # Removed checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
        
    #Remove directory listing created for JS element
    if 'dirList' in pattern_files:
        pattern_files.remove('dirList')
    
    #Check if file name is taken
    if file_name3.value in pattern_files:
        display( Markdown("The file <b>" +  file_name3.value + '</b> already exists. If you still would like to save your pattern as <b>' + file_name3.value + '</b>, delete the file and save again.') )
    
    file_path = os.path.join()
    text_file = open("sample.txt", "w")
    n = text_file.write(txt)
    text_file.close   

def refresh_list(ev):
    global pattern_files
    
    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
    
    #remove directory listing created for JS elemen    
    if 'dirList' in pattern_files:
        pattern_files.remove('dirList')
    
    # Rerun cell to refresh list of files in pattern folder
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(),\
    IPython.notebook.get_selected_index()+1)'))

def apply_alteration(ev):
    global create_button_clicked, join_button_clicked, edit_button_clicked
    create_button_clicked = True
    join_button_clicked = True
    edit_button_clicked = True
    
    # Run cell below
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,\
    IPython.notebook.get_selected_index()+3)'))

def toggle_button_run_cell(change):
    # Run next 4 cells once toggle is changed to display appropriate widgets
    value = change['new']
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,\
    IPython.notebook.get_selected_index()+5)'))

def refresh_list(ev):
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,\
    IPython.notebook.get_selected_index()+1)'))
    
def plot_basket(ev):
    global files_selected
    files_selected = True
    
    # Run next cell to plot basket
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,\
    IPython.notebook.get_selected_index()+2)'))

def display_basket_model(basket_chose):
    # Display example of basket image
    if (basket_chose == 'Rectangular Basket'):
        display(Markdown('<center><h2> Rectangular Basket </h2>'))
        display(Markdown('<center> <img src="./images/rect-basket.png" alt="Rectangular Basket">'))

    elif (basket_chose == 'Circular Basket'):
        display(Markdown('<center><h2> Circular Basket </h2>'))
        display(Markdown('<center> <img src="./images/circ-basket.png" alt="Circular Basket">'))

def dropdown_choose_basket(basket_chose):
    if (basket_chose == 'Rectangular Basket'):

        display(Box(children = [box1, box2], layout = box_layout))
        display(Box(children = [plot_button, refresh_button], layout = box_layout))

    elif (basket_chose == 'Circular Basket'):

        display(Box(children = [circ_pattern, refresh_button], layout = box_layout))
        display(Box(children = [plot_button], layout = box_layout))

def plot_3d_model(files_selected):

    if files_selected == True:  
        print("Plotting basket...please wait a few seconds to create 3D model")
        if (basket_chose == 'Rectangular Basket'):

            front = open('./patterns/'+ front_pattern.value, 'r') 
            front = front.read()

            back = open('./patterns/'+ back_pattern.value, 'r') 
            back = back.read()

            left = open('./patterns/'+ left_pattern.value, 'r') 
            left = left.read()

            right = open('./patterns/'+ right_pattern.value, 'r') 
            right = right.read()

            plot_rect_basket(front, back, left, right, ori_p)

        elif (basket_chose == 'Circular Basket'):
            pattern = open('./patterns/'+ circ_pattern.value, 'r')
            pattern = pattern.read()
            plot_circ_basket(pattern, ori_p)


        files_selected = False

if __name__ == "__main__":

    # Create folder name patterns in pattern folder does not exist
    if not os.path.exists('patterns'):
        os.makedirs('patterns')

    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    # Remove checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')

    #remove directory listing created for JS element
    if 'dirList' in pattern_files:
        pattern_files.remove('dirList')
             
    # Define layout and style of widgets
    box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
    style = {'description_width': 'initial'}
    
    
    # Create Toggle Buttons for basket shape selection
    basket_options = widgets.ToggleButtons(
        button_style = 'info',
        options=['Rectangular Basket', 'Circular Basket'],
        description='',
        disabled=False,
        layout = Layout(display='flex',
                        align_items='stretch',
                        justify_content = 'center'))
    
    # Create Refresh Button
    refresh_button = widgets.Button( button_style= 'info', description="Refresh Files")
    refresh_button.on_click(refresh_list)

    # Create Plot Button
    plot_button = widgets.Button( button_style= 'info', description="Plot Basket")
    plot_button.on_click(plot_basket)

    # Create Dropdown Menus for Faces of the Rectangular Basket
    front_pattern = widgets.Dropdown(options = pattern_files, description ='Front Motif:', style = style, disabled=False,)
    back_pattern = widgets.Dropdown(options = pattern_files, description ='Back Motif:', style = style, disabled=False,)
    left_pattern = widgets.Dropdown(options = pattern_files, description ='Left Side Motif:', style = style, disabled=False,)
    right_pattern = widgets.Dropdown(options = pattern_files, description ='Right Side Motif:', style = style, disabled=False,)

    box1 = VBox([front_pattern, back_pattern], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='50%', justify_content = 'center'))
    box2 = VBox([left_pattern, right_pattern], layout = Layout(display= 'flex', flex_flow= 'column', align_items= 'center', width='50%', justify_content = 'center'))

    # Create Dropdown Menu for Face of the Circular Basket
    circ_pattern = widgets.Dropdown(options = pattern_files, description ='Motif:', style = style, disabled=False,)