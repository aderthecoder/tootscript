import time

src = open('code.txt', 'r')
code = str(src.read())
src.close()

cell = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ptr = 0
word_counter = 0
word = ''

for a in code:
    word_counter = word_counter + 1
    word = str(word) + str(a)
    if word_counter == 3:
        if word == 'too':
            if ptr <= 0:
                print('Error :(')
                break
            ptr = ptr - 1
        if word == 'oot':
            if ptr == 10:
                print('Error :(')
                break
            ptr = ptr + 1
        if word == 'ttt':
            cell_now = cell[ptr]
            cell[ptr] = cell_now + 1
        if word == 'ooo':
            if cell[ptr] == 0:
                print('Error :(')
                break
            cell_now = cell[ptr]
            cell[ptr] = cell_now - 1
        if word == 'oto':
            print(cell[ptr])
        if word == 'tot':
            cell[ptr] = int(input('input'))
        word_counter = 0
        word = ''
time.sleep(10)
