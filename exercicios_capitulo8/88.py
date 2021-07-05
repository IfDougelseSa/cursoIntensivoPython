# album function

def make_album(artist, title, number_banding=""):
    """Fuction about an album"""
    album = {'name': artist, 'album name': title}
    if number_banding:
        album['Number_bandig'] = number_banding
    return album


x = ''

active = True
while active:
    album2 = {'name': input("Digite o nome do artista: "), 'album name': input("Digite o nome do album: ")}
    x = input(f'Do you wanna leave?')

    if x == 'q':
        active = False

print(album2)
