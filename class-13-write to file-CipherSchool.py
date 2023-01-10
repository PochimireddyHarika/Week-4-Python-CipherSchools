with open('file.txt', 'w') as f:
    f.write('hello')
with open('file.txt', 'r+') as f:
    f.write('please do it')
with open('file.txt', 'r+') as f:
    f.seek(len(f.read()))
    f.write('please do it')