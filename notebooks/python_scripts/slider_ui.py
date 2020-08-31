global counter_0, atomic_built, current_pattern, op_bool, restart_bool
atomic_built = False
h_bool = False
v_bool = False
op_bool = False
restart_bool = False
counter_0 = 0


global atomic

   
def display_sliders(current_motif):
    if (current_motif == 'Broken Line'):
        display(rect_h1, rect_h2, rect_width, num_colors)

    elif (current_motif == 'Triangle'):
        display(tri_height, num_colors)

    elif (current_motif == 'Diagonal Lines'):
        display(chevron_height, num_colors)

    elif (current_motif == 'Upload Pattern'):
        display(pattern_choices)

if __name__ == "__main__":


    # Create General Sliders

    style = {'description_width': 'initial'}
    num_colors = widgets.IntSlider(value = 3, min = 1, max = 5, description = "Number of Colors", style = style)
    num_colors.style.handle_color = '#47b0cb'
    # palette = widgets.Dropdown(options={'Original':ori_p,'Seafoam Green' : pal_a, 'Magenta to blue' : pal_b, 'Ocean Breeze' : pal_c,
    #              'Fiery Red' : pal_d, 'Fiery Red 2' : pal_j, 'Blue' : pal_e, 'Turquoise' : pal_f,
    #             'Red to Purple': pal_g, 'Purple to Pink' : pal_h, 'Burnt Orange' : pal_i, 
    #              'Forest Green' : pal_k, 'Bold Lavender' : pal_l, 'Valentine Red' : pal_m}, value = ori_p,
    #     description='Palette:',
    #     disabled = False,)

    # Create Sliders for Parameters for Rectangle

    rect_h1 = widgets.IntSlider(value = 2, min = 1, max = 10, description = "Height 1", style = style, )
    rect_h1.style.handle_color = '#47b0cb'
    rect_h2 = widgets.IntSlider(value = 2, min = 1, max = 10, description = "Height 2", style = style)
    rect_h2.style.handle_color = '#47b0cb'
    rect_width = widgets.IntSlider(value = 5, min = 0, max = 20, description = "Width", style = style)
    rect_width.style.handle_color = '#47b0cb'

    # Create Sliders for Parameters for Triangle

    tri_height = widgets.IntSlider(value = 5, min = 3, max = 10, description = "Height", style = style)
    tri_height.style.handle_color = '#47b0cb'

    # Create Sliders for Parameters for Chevron
    chevron_height = widgets.IntSlider(value = 5, min = 3, max = 10, description = "Height", style = style)
    chevron_height.style.handle_color = '#47b0cb'

    # Create folder name patterns in pattern folder does not exist
    if not os.path.exists('patterns'):
        os.makedirs('patterns')

    # List Pattern Text Files
    pattern_files = os.listdir("./patterns/")

    if '.ipynb_checkpoints' in pattern_files:
        pattern_files.remove('.ipynb_checkpoints')

    pattern_choices = widgets.Dropdown(options = pattern_files, description ='Pattern:', style = style, disabled=False,)