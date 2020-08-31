import colours
import atomic_rectangle
import atomic_triangle
import atomic_chevron
import operations 
import plotting

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
def toggle_button_run_cell(change):
    # Run next 6 cells once new toggle button is clicked to display appropriate pictures and widgets
    value = change['new']
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()+1,\
    IPython.notebook.get_selected_index()+7)'))
    
    
def save_as(ev):
    save_as_button.close()
    display(file_name, save_button)

def save_pattern(ev):
    save_button.close()

    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    # Remove checkpoints from folder if exists
    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')
    
    if atomic_built == True:

        # Check if file name is taken    
        if (file_name.value in pattern_files):
            display( Markdown("The file <b>" +  file_name.value + '</b> already exists. If you still would like to save your pattern as <b>' + file_name.value + '</b>, delete the file and save again.') )

        # Write editted pattern into text file
        elif (file_name.value != ''):
            file = open("./patterns/" + file_name.value, "w")

            file.write(atomic)
            file.close()

            display(Markdown("Your pattern has been saved as <b>" + file_name.value + "</b>."))
            
def new_motif(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(),IPython.notebook.get_selected_index()+2)'))
    
    global atomic, atomic_built
    
    # Check if restart button was clicked
    if (restart_bool == True):
        atomic_built == False
        
    else:
        atomic_built = True 
        
    # Set atomic and close appropriate widgets 
    if (current_motif == 'Broken Line'):
        atomic = build_atomic_rect(rect_h1.value, rect_h2.value, rect_width.value, num_colors.value)
        rect_h1.close()
        rect_h2.close()
        rect_width.close()
          
    elif (current_motif == 'Triangle'):
        atomic = build_atomic_tri(tri_height.value, num_colors.value)
        tri_height.close()
        
    elif (current_motif == 'Diagonal Lines'):
        atomic = build_atomic_chevron(chevron_height.value, num_colors.value)
        chevron_height.close()
        
    num_colors.close()    
    plot_motif_2D(atomic, ori_p)
    
def upload_motif(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(),IPython.notebook.get_selected_index()+2)'))
    
    global atomic, atomic_built  
    
    # Check if restart button was clicked
    if (restart_bool == True):
        atomic_built == False
        
    else:
        atomic_built = True 
    
    loaded_pattern = open('./patterns/'+ pattern_choices.value, 'r') 
    atomic = loaded_pattern.read()
        
       
    plot_motif_2D(atomic, ori_p)
    
def apply_flip(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record flipped pattern and display operation
    atomic_f = flip(atomic, flip_choices.value)
    plot_motif_2D(atomic_f, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_f 
    
    # Empty backout stack since redo's are no longer possible
    while not backup.isEmpty():
        backup.pop()
       
    
def apply_reflect_h(ev):

    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record reflected pattern and display operation
    atomic_h = reflect_h(atomic, spacing_reflect.value, choices_h.value)
    plot_motif_2D(atomic_h, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_h 
    
    # Empty backout stack since redo's are no longer possible    
    while not backup.isEmpty():
        backup.pop()

def apply_reflect_v(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record reflected pattern and display operation
    atomic_v = reflect_v(atomic, spacing_reflect.value, choices_v.value)
    plot_motif_2D(atomic_v, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_v
    
    # Empty backout stack since redo's are no longer possible   
    while not backup.isEmpty():
        backup.pop()
        
def apply_stack_h(ev):

    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record stacked pattern and display operation
    atomic_h = stack_h(atomic, spacing_stack.value)
    plot_motif_2D(atomic_h, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_h 
    
    # Empty backout stack since redo's are no longer possible 
    while not backup.isEmpty():
        backup.pop()

def apply_stack_v(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record stacked pattern and display operation
    atomic_v = stack_v(atomic, spacing_stack.value)
    plot_motif_2D(atomic_v, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_v
    
    # Empty backout stack since redo's are no longer possible
    while not backup.isEmpty():
        backup.pop()
        
def apply_stack_d(ev):
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-1,IPython.notebook.get_selected_index()+2)'))
    
    # Record stacked pattern and display operation
    atomic_d = stack_d(atomic, spacing_stack.value, choices_d.value)
    plot_motif_2D(atomic_d, ori_p)
    
    global op_bool, new_pattern
    op_bool = True
    new_pattern = atomic_d
    
    # Empty backout stack since redo's are no longer possible    
    while not backup.isEmpty():
        backup.pop()
        
def restart(ev):
    global atomic_built, restart_bool, op_bool
    atomic_built = False
    op_bool = False
    restart_bool = True
    restart_button.close()
    undo_button.close()
    redo_button.close()
    
    # Empty main and backout stack since undos and redos are no longer possible
    while not main.isEmpty():
        main.pop()
        
    while not backup.isEmpty():
        backup.pop()
    
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index()-3,\
    IPython.notebook.get_selected_index()+1)'))

def undo_pattern(ev):
    global atomic
    top = main.peek()
    main.pop()
    backup.push(top)
    atomic = main.peek()
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(),\
    IPython.notebook.get_selected_index()+2)'))
    plot_motif_2D(atomic, ori_p)
    
def redo_pattern(ev):
    global atomic
    top = backup.peek()
    backup.pop()
    main.push(top)
    atomic = main.peek()
    display(Javascript('IPython.notebook.execute_cell_range(IPython.notebook.get_selected_index(),\
    IPython.notebook.get_selected_index()+2)'))
    plot_motif_2D(atomic, ori_p)
    
    
def display_motif_using_option(current_motif):

    # Display appropriate heading and image
    if (current_motif == 'Broken Line'):
        display(Markdown('<center> <img src="./images/atomic-rect.png" alt="Atomic Rectangle">'))
        display(Markdown("<h2> Broken Line Motif </h2>"))

    elif (current_motif == 'Triangle'):
        display(Markdown('<center> <img src="./images/atomic-tri.png" alt="Atomic Triangle">'))
        display(Markdown("<h2> Triangular Motif </h2>"))

    elif (current_motif == 'Diagonal Lines'):
        display(Markdown('<center> <img src="./images/atomic-chevron.png" alt="Atomic Chevron">'))
        display(Markdown("<h2> Diagonal Lines Motif </h2>"))

if __name__ == "__main__":
    
    motif_options = widgets.ToggleButtons(
    button_style = 'info',
    options=['Broken Line', 'Triangle', 'Diagonal Lines', 'Upload Pattern'],
    description='',
    disabled=False,
    layout = Layout(display='flex',
                    align_items='stretch',
                    justify_content = 'center'))