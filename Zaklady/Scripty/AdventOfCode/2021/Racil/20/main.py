from os import path


def printList(list):
    for line in list:

        print(''.join(line).replace('0', '.').replace('1', '#'))


def findNeighbors(list, x, y, char):
    directions = [(-1, -1), (0, -1), (1, -1),
                  (-1, 0), (0, 0), (1, 0),
                  (-1, 1), (0, 1), (1, 1)]
    binary = ''
    for direction in directions:
        if 0 <= direction[1]+y and direction[1]+y < len(list)\
                and 0 <= direction[0]+x and direction[0]+x < len(list[0]):
            binary += list[direction[1]+y][direction[0]+x]
        else:
            binary += char
    return int(binary, 2)


def expandField(list, char):
    radek = [char for item in range(len(list[0]))]
    return [[char]+row+[char]for row in [radek]+list+[radek]]


def countOnes(image):
    val = 0
    for row in image:
        val += row.count('1')
    return val


def enhanceImage(image, value_res, char):
    image = expandField(image, char)

    new_image = [[None for col in row] for row in image]
    for idy, row in enumerate(image):
        for idx, column in enumerate(row):
            val = findNeighbors(image, idx, idy, char)
            symbol = value_res[val]
            new_image[idy][idx] = symbol
    return new_image


with open(path.join(
        path.dirname(path.realpath(__file__)),
        "input.txt"), "r") as file:
    data = [item for item in file.read().split('\n\n')]
    value_res = ['1' if item ==
                 '#' else '0' for item in data[0] if item != "\n"]
    image = [['1' if symbol == '#' else '0' for symbol in line]
             for line in data[1].split("\n")]


i = 0
while i < 50:
    image = enhanceImage(
        image, value_res, value_res[0] if i % 2 == 0 else value_res[255])
    i += 1
print(countOnes(image))
