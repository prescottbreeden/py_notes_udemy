def copy(file_name, new_file_name):
    '''
    Accepts a file name and produces a copy of that file with new_file name
    '''
    with open(file_name) as file:
        text = file.read()

    with open(new_file_name, 'w') as new_file:
        new_file.write(text)


def copy_and_reverse(file_name, reversed_file):
    '''
    Accepts a file name and returns a new file with the contents reversed
    '''
    with open(file_name) as file:
        text = file.read()
        text = text[::-1]

    with open(reversed_file, 'w') as reverse_file:
        reverse_file.write(text)


def statistics(file_name):
    '''
    Accepts a file and returns number of lines, words, and characters
    '''
    with open(file_name) as file:
        all_lines = file.readlines()
        lines = len(all_lines)
        words = sum(len(line.split(' ')) for line in all_lines)
        characters = sum(len(line) for line in all_lines)

    stats = {'lines': lines, 'words': words, 'characters': characters}
    print(stats)
    return stats


def find_and_replace(file_name, old_word, new_word):
    '''
    Accepts a file name, a search term, and a replacement for the search term
    '''
    with open(file_name, 'r+') as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
