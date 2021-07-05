magicians_list = ['Issao Imamura', 'David Coperfield', 'Fu-Manchu']



def show_magicians(magicians):
    """Show the magicians name"""
    for magician in magicians:
        print(magician)


def make_great():
    magicians_list = ["The great Issao Imamura", "The great Dabid Coperfield", "The great Fu-Manchu"]


    return magicians_list[:]


print(make_great())
show_magicians(magicians_list)

