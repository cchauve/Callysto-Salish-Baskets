global pattern_files, new_pattern, file_name, save_button
global join_button_clicked
join_button_clicked = False

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


def save_joined_pattern(ev):
    global pattern_files
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(), IPython.notebook.get_selected_index()+1)'))

    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")
    
    # Remove checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
    
    # Check if file name is taken
    if (file_name1.value in pattern_files):
        display( Markdown("The file <b>" +  file_name1.value + '</b> already exists. If you still would like to save your pattern as <b>' + file_name1.value + '</b>, delete the file and save again.') )
    
    # Write joined pattern into text file
    elif (file_name1.value != ''):
        file = open("./patterns/" + file_name1.value, "w")
        new_pattern = join_patterns(first, second, spacing.value)

        file.write(new_pattern)
        file.close()

        display(Markdown("Your motif has been saved as <b>" + file_name1.value + "</b>."))

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
    

def refresh_list(ev):
    global pattern_files
    
    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
        
    #remove directory listing created for JS element
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
    
def joined_motif_preview(join_button_clicked, pattern_files, first_pattern, second_pattern):
    if (join_button_clicked == True and pattern_files != []):

        display(Markdown('<center> <h3> Motif Preview </h3>'))

        # Read chosen pattern text files, join the patterns and display new pattern
        first = open('./patterns/'+ first_pattern.value, 'r') 
        first = first.read()
        second = open('./patterns/'+ second_pattern.value, 'r') 
        second = second.read()

        new_pattern = join_patterns(first, second, spacing.value)
        plot_motif_2D(new_pattern, ori_p)
    
if __name__ == "__main__":
    
    
    # Create folder name patterns in pattern folder does not exist
    if not os.path.exists('patterns'):
        os.makedirs('patterns')

    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    #remove directory listing created for JS element
    if 'dirList' in pattern_files:
        pattern_files.remove('dirList')

    # Remove checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
        
    # Define layout and style of widgets
    box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
    style = {'description_width': 'initial'}
    
    # Layout for widgets
    box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='100%', justify_content = 'center')
    style = {'description_width': 'initial'}

    # Create dropdown menu for patterns
    first_pattern = widgets.Dropdown(options = pattern_files, description ='Motif 1:', style = style, disabled=False,)
    second_pattern = widgets.Dropdown(options = pattern_files, description ='Motif 2:', style = style, disabled=False,)
    spacing = widgets.IntSlider(value = 0, min = 0, max = 10, description = "Spacing Amount", style = style)

    # Create join and refresh button and define click events
    join_button = widgets.Button( button_style= 'info', description="Join Motifs")
    join_button.on_click(apply_alteration)

    refresh_button = widgets.Button( button_style= 'info', description="Refresh Files")
    refresh_button.on_click(refresh_list)
    
    # Create saving widgets
    save_button1 = widgets.Button(button_style= 'info',description="Save")
    save_button1.on_click(save_joined_pattern)

    file_name1 = widgets.Text(value = '', description='File Name:', disabled=False)
