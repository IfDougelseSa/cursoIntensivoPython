# album function

def make_album(artist, title, number_banding=""):
    """Fuction about an album"""
    album = {'name': artist, 'album name': title}
    if number_banding:
        album['Number_bandig'] = number_banding
    return album

print(make_album('Ramones', 'Ramones', '4'))
print(make_album('Guns n Roses', 'Chinese Democracy'))
print(make_album('David Bowie', 'Starman'))
