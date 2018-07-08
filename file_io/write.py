with open('haiku.txt', 'w') as file:
    file.write('Writing files is great\n')
    file.write('Here\'s another line of text\n')
    file.write('Closing now, goodbye!')

with open('haiku.txt', 'a') as file:
    file.write('\n\nWriting files is great\n')
    file.write('Here\'s another line of text\n')
    file.write('Closing now, goodbye!')

with open('haiku.txt', 'r+') as file:
    # Cursor starts at position 0
    # will only work with an existing file
    file.write('Added using r+ ......')
