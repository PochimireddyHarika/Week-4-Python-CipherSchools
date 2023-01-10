with open('LOVE Story.txt', 'r', encoding='UTF-8') as f:
    print(f.encoding)
    data = f.read()
    print(data)

with  open('file.txt', 'r') as f:
    data = f.read()
    print(data)