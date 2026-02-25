def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album"""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict
    

album_list = []

"""
album_list.append(make_album('andrii', 'street east'))
album_list.append(make_album('ponimau', 'son', 20))
album_list.append(make_album('mots', 'food', 5))


for album in album_list:
    track_count = album.get('tracks', 'unknown')

    print(f"New hot artist, {album['artist']}, "
        f"release new album '{album['title']}',"
            f" with {track_count} tracks!")

"""

while True:
    print("Reads our news!\n\t(u can quit any time if type 'q')")

    artist = input("Insert artsit name: ")
    if artist == 'q':
        break
    
    title = input("Insert title of album: ")
    if title == 'q':
        break

    tracks = int(input("Insert how much tacks has album: "))    
    if tracks == 'q':
        break

    album_list.append(make_album(artist, title, tracks))


    for album in album_list:
        print(
            f"The new hotest artist, {album['artist']}, "
            f"released new cool album '{album['title']}', "
            f"that contains {tracks} traks!"
        )

    next = input("Do u want continue? (y/n) ")
    if next == 'n':
        break
    