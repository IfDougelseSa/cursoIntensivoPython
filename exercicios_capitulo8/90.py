# magicians list in fuction
def show_magicians(magicians):
    """Show the name of magicians"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modified the magicians name"""
    for magician in magicians:
        print(f'The big {magician}!')


magicians = ['David Blaine', 'Dai Vernon', 'David Copperfield']


show_magicians(magicians)
make_great(magicians[:])

