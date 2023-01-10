import os

print(os.path.exists('movies'))
if os.path.exists('movies'):
    print('already exists')
else:
    os.mkdir('movies')

open('file.txt', 'a').close()
print(os.listdir())

