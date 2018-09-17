# Color pallets

pal_a = ['#edf8fb','#b2e2e2','#66c2a4','#2ca25f','#006d2c'][::-1] + ['#d5a967']
pal_b = ['#edf8fb','#b3cde3','#8c96c6','#8856a7','#810f7c'][::-1] + ['#d5a967']
pal_c = ['#f0f9e8','#bae4bc','#7bccc4','#43a2ca','#0868ac'][::-1] + ['#d5a967']
pal_d = ['#fef0d9','#fdcc8a','#fc8d59','#e34a33','#b30000'][::-1] + ['#d5a967']
pal_e = ['#f1eef6','#bdc9e1','#74a9cf','#2b8cbe','#045a8d'][::-1] + ['#d5a967']
pal_f = ['#f6eff7','#bdc9e1','#67a9cf','#1c9099','#016c59'][::-1] + ['#d5a967']
pal_g = ['#f1eef6','#d7b5d8','#df65b0','#dd1c77','#980043'][::-1] + ['#d5a967']
pal_h = ['#feebe2','#fbb4b9','#f768a1','#c51b8a','#7a0177'][::-1] + ['#d5a967']
pal_i = ['#ffffd4','#fed98e','#fe9929','#d95f0e','#993404'][::-1] + ['#d5a967']
pal_j = ['#ffffb2','#fecc5c','#fd8d3c','#f03b20','#bd0026'][::-1] + ['#d5a967']
pal_k = ['#edf8e9','#bae4b3','#74c476','#31a354','#006d2c'][::-1] + ['#d5a967']
pal_l = ['#f2f0f7','#cbc9e2','#9e9ac8','#756bb1','#54278f'][::-1] + ['#d5a967']
pal_m = ['#fee5d9','#fcae91','#fb6a4a','#de2d26','#a50f15'][::-1] + ['#d5a967']
ori_p = ['#000000'] + ['wheat','maroon','#ffe07c','goldenrod','khaki'] + ['#d5a967']

# Function: associates list of hexadecimal colour formats to characters used in our data structure to represent colours
# Input: list of character code values in hexadecimal string format
# Output: dictionary, key: character used in data structure to represent color, value: hexadecimal string format of colour

def get_colors(palette):
    # Create list of the alphabet and include '-' character which will be used as the plain basket color
    alphabet =  string.ascii_lowercase + '-'
    alphabet_arr = list(alphabet)
    
    char_col_dictionary = {}
    size = len(palette)

    char_col_dictionary[alphabet_arr[1]] = palette[-1]
    for i in range(size-1):
        char_col_dictionary[alphabet_arr[i]] = palette[i]
    char_col_dictionary[alphabet_arr[-1]] = palette[-1]
    return char_col_dictionary  

# Function: switches keys to values and values to keys of a dictionary
# Input: dictionary
# Output: dictionary
def get_character(dictionary):
    
    char_dictionary =  {val:key for key,val in dictionary.items()}
    return char_dictionary