def show_magicians(names):
    for name in names:
        print(name.title())


def make_great(names, great_names):
    while names:
        current_name = names.pop()
        great_names.append(f"The Great {current_name.title()}")


magicians = ['hermiona', 'gendalf', 'harry potter', 'ron']
great_magicians = []

make_great(magicians[:], great_magicians)

show_magicians(magicians)
show_magicians(great_magicians)
