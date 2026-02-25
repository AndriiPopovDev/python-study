def make_shirt(size='large', text='I love Python'):
    print(f"{size.title()} size T-Shirt, with print '{text}'")

make_shirt(size='medium', text='Hello, world!')
make_shirt('medium', 'Hello World!')
make_shirt()
make_shirt('small')  
make_shirt(text='C#')