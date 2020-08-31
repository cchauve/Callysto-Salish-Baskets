if __name__ == "__main__":


    if (current_motif == 'Broken Line'):
        atomic = build_atomic_rect(rect_h1.value, rect_h2.value, rect_width.value, num_colors.value)

        # Create Motif Button
        motif_button = widgets.Button( button_style= 'info', description="Display Motif" );
        motif_button.on_click(new_motif)

        # Check if atomic piece has been built. If not, display button to plot atomic piece
        if atomic_built == False:
            display(motif_button)

    elif (current_motif == 'Triangle'):
        atomic = build_atomic_tri(tri_height.value, num_colors.value)

        # Create Motif Button
        motif_button = widgets.Button( button_style= 'info', description="Display Motif" );
        motif_button.on_click(new_motif)

        # Check if atomic piece has been built. If not, display button to plot atomic piece
        if atomic_built == False:
            display(motif_button)

    elif (current_motif == 'Diagonal Lines'):
        atomic = build_atomic_chevron(chevron_height.value, num_colors.value)

        # Create Motif Button
        motif_button = widgets.Button( button_style= 'info', description="Display Motif" );
        motif_button.on_click(new_motif)

        # Check if atomic piece has been built. If not, display button to plot atomic piece
        if atomic_built == False:
            display(motif_button)

    elif (current_motif == 'Upload Pattern'):
        loaded_pattern = open('./patterns/'+ pattern_choices.value, 'r') 
        atomic = loaded_pattern.read()

        # Create Motif Button
        motif_button = widgets.Button( button_style= 'info', description="Display Motif" );
        motif_button.on_click(upload_motif)

        # Check if atomic piece has been built. If not, display button to plot atomic piece
        if atomic_built == False:
            display(motif_button)