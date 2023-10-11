with open("text.txt", 'wb') as f:
    f.write(b'abba')

with open("new", 'w') as f:
    f.write("text text\ntext")

with open('append_text', 'a') as f:
    f.write("text text\ntext")

with open('write_only_once', 'x') as f:
    f.write("text text\ntext\n")