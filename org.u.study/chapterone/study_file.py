


import os


def printInLine(file):

    text = file.readlines()
    n = 1  # 行号的初始值
    for i in text:
        print('%d:%s' % (n, i), end='')
        n += 1


def backFile(filePath):

    originFile = open(filePath, 'r');
    print(f'文件目录：{os.getcwd()} --- 原文件名：{originFile.name}---原文件编码：{originFile.encoding}')
    printInLine(originFile)

    newName = filePath.split('.')[0] + '[备份].' + filePath.split('.')[1]
    print(f'{newName}')

    try:
        newFile = open(newName,'w')
        print(f'新文件名：{newFile.name}---新文件编码：{newFile.encoding}')

        readFile = originFile.read()
        newFile.write(readFile)


    except Exception as e:
        print(f'原文件名：{originFile.name}---原文件编码：{originFile.encoding}---{e}')
    finally:
        originFile.close()
        newFile.close()
        print(f'原文件名：{originFile.name}---原文件编码：{originFile.encoding}---{originFile.close()}')


path = 'D:/XBF2/python-old.txt'
backFile(path)



