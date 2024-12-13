with open('dictionary/textfile.txt','r') as textfile:
    data = dict()

    items = textfile.read()
    lines = items.split(',')
    print(len(lines))

    for content in lines:
        if content in data:
            data[content] = data[content] + 1
        else:
            data[content] = 1
    print(data)
    