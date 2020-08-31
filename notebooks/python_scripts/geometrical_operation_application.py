if __name__ == "__main__":


    #print(atomic)

    # Define Layout
    box_layout = Layout(display='flex', flex_flow='row', align_items='center', width='50%', justify_content = 'center')

    # Restart Button
    restart_button = widgets.Button( button_style= 'info', description="Restart")

    # Create Saving Tools
    save_button = widgets.Button(button_style= 'info',description="Save")
    save_button.on_click(save_pattern)

    save_as_button = widgets.Button(button_style= 'info',description="Save As")
    save_as_button.on_click(save_as)

    file_name = widgets.Text(placeholder = '', description='File Name:', disabled=False)

    # Create Buttons for Flipping
    flip_choices = widgets.RadioButtons(options=['Flip Horizontally', 'Flip Vertically'], layout = box_layout, disabled=False)
    apply_flip_button = widgets.Button( button_style= 'info',description="Apply")
    flip_box = HBox(children= [flip_choices, apply_flip_button], layout = box_layout)

    # Create Buttons and Sliders for Reflecting
    spacing_reflect = widgets.IntSlider(value = -1, min = -1, max = 10, description = "Spacing Amount", style = style)
    spacing_reflect.style.handle_color = '#47b0cb'

    apply_spacing_h_button = widgets.Button( button_style= 'info',description="Apply")
    apply_spacing_v_button = widgets.Button( button_style= 'info',description="Apply")

    choices_h = widgets.RadioButtons(options=['Reflect Above', 'Reflect Below'], layout = box_layout, disabled=False)
    choices_v = widgets.RadioButtons(options=['Reflect Left', 'Reflect Right'], layout = box_layout,disabled=False)

    spacing_h_box = HBox(children = [spacing_reflect, apply_spacing_h_button], layout=box_layout)
    spacing_v_box = HBox(children = [spacing_reflect, apply_spacing_v_button], layout=box_layout)

    # Create Buttons and Sliders for Stacking
    apply_stacking_h_button = widgets.Button( button_style= 'info',description="Apply")
    apply_stacking_v_button = widgets.Button( button_style= 'info',description="Apply")
    apply_stacking_d_button = widgets.Button( button_style= 'info',description="Apply")

    choices_d = widgets.RadioButtons(options=['Stack Left', 'Stack Right'], layout = box_layout,disabled=False)
    spacing_stack = widgets.IntSlider(value = 0, min = 0, max = 10, description = "Spacing Amount", style = style)

    stacking_h_box = HBox(children = [spacing_stack, apply_stacking_h_button], layout=box_layout)
    stacking_v_box = HBox(children = [spacing_stack, apply_stacking_v_button], layout=box_layout)
    stacking_d_box = HBox(children = [spacing_stack, apply_stacking_d_button], layout=box_layout)

    # Create Accordian for Operations
    reflection_options = widgets.Accordion(children = [flip_box, VBox([choices_h, spacing_h_box]), VBox([choices_v, spacing_v_box]), 
                                           VBox([stacking_h_box]), VBox([stacking_v_box]), VBox([choices_d, stacking_d_box])],  style = style)
    reflection_options.selected_index = None # Collaspe accordian
    reflection_options.set_title(0, 'Flip')
    reflection_options.set_title(1, 'Reflect Horizontally')
    reflection_options.set_title(2, 'Reflect Vertically')
    reflection_options.set_title(3, 'Stack Horizontally')
    reflection_options.set_title(4, 'Stack Vertically')
    reflection_options.set_title(5, 'Stack Diagonally')

    # Define on_click events
    apply_flip_button.on_click(apply_flip)
    apply_spacing_h_button.on_click(apply_reflect_h)
    apply_spacing_v_button.on_click(apply_reflect_v)
    apply_stacking_h_button.on_click(apply_stack_h)
    apply_stacking_v_button.on_click(apply_stack_v)
    apply_stacking_d_button.on_click(apply_stack_d)
    restart_button.on_click(restart)

    # Create Buttons for Editing
    undo_button = widgets.Button( button_style= 'warning',description="Undo")
    redo_button = widgets.Button( button_style= 'warning',description="Redo")

    undo_button.on_click(undo_pattern)
    redo_button.on_click(redo_pattern)
    edit_buttons = [undo_button, redo_button]

    edit_box = Box(children= edit_buttons, layout=box_layout)

    # Check if new atomic was created
    if atomic_built == True and op_bool == False:
        if main.isEmpty():
            main.push(atomic)
            motif_button.close()

        # User had clicked undo
        if backup.size() >= 1:

            # Main stack only has original atomic but reflections have been applied -- undo option has been exhausted
            if main.size() == 1:
                display(Box(children = [redo_button], layout=box_layout))

            # Undo and redo option available
            elif main.size() >= 2:
                display(edit_box)

        # User has applied operations to original motif
        elif main.size() >= 2:
            display(Box(children = [undo_button], layout=box_layout))

        display(reflection_options)
        display(VBox([save_as_button, restart_button]))

    # Check if operation has been applied
    # If so, add the current pattern onto main stack
    if op_bool == True:
        atomic = new_pattern
        main.push(atomic)
        op_bool = False

        # User has not clicked undo
        if backup.isEmpty():
            display(Box(children = [undo_button], layout=box_layout))

        display(reflection_options)
        display(VBox([save_as_button, restart_button]))


