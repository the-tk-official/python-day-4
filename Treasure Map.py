row1 = ['📋', '📋', '📋']
row2 = ['📋', '📋', '📋']
row3 = ['📋', '📋', '📋']

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}\n')

position = input('Where do u wnat to put the treasure? ')

horizonal = int(position[0]) - 1
vertical = int(position[1]) - 1

# select_row = map[vertical]
# select_row[horizonal] = '❎'

map[vertical][horizonal] = '❎'

print(f'{row1}\n{row2}\n{row3}')
