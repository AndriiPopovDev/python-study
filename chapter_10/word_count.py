from pathlib import Path

def count_words(path):
    # count the approximate number of words in the file: 
    path = Path(path)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"{path} doesn't exist")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words")


filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for file in filename:
    path = Path(file)
    count_words(path)

