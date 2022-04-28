def open_poem():
    text = open('/var/www/flaga/dane/wiersz1.txt').read()
    text_lines = open('/var/www/flaga/dane/wiersz1.txt').readlines()

    poem_lines = []
    for line in text_lines:
        line = line.strip()
        poem_lines.append(line)


    return poem_lines

poem = open_poem()
for l in poem:
    print(l)