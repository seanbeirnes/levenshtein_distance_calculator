# The Levenshtein Distance algorhythm calculates the number of different charachters between two strings.

# ###############################################
# Matrix Version
# This version is preferred over the recurssive version due to its efficiency.
# ###############################################

def calc_cost(char_s, char_t):

    if char_s == char_t:
        return 0
    else:
        return 1
    

def set_first_row(s):

    row = [0]

    for i in range( len(s) ):
        row.append( i + 1 )

    return row


def add_row(s, t, last_row, int_t):

    row = [ int_t + 1 ]

    for i in range( len(last_row[1:]) ):
        cell_above = last_row[ i + 1 ] + 1
        cell_left = row[i] + 1
        cell_diag = last_row[i] + calc_cost(s[i], t[int_t])

        if cell_above < cell_left and cell_above < cell_diag:
            row.append( cell_above )
        elif cell_left < cell_above and cell_left < cell_diag:
            row.append( cell_left )
        else:
            row.append( cell_diag )

    return row


def calc_lev(s, t):

    matrix = []

    first_row = set_first_row(s)
    matrix.append( first_row )
    last_row = first_row

    for i in range( len(t) ):
        new_row = add_row(s, t, last_row, i )
        matrix.append(new_row)
        last_row = new_row

    return matrix[-1][-1]


# ###############################################
# Recurssive Version
# This is computationaly inefficient and should be for demonstration only.
# ###############################################

def lev(string_a, string_b):

    if len(string_a) == 0:
        return len(string_b)
    if len(string_b) == 0:
        return len(string_a)
    if string_a[0] == string_b[0]:
        return lev(string_a[1:], string_b[1:])

    return 1 + min(
            lev( string_a[1:], string_b ),
            lev( string_a, string_b[1:] ),
            lev( string_a[1:], string_b[1:])
        )
    

