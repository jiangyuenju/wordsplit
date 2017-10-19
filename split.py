# -*- coding: utf-8 -*-


def RMM(dict, s):
    splitarray = []
    for i in xrange(len(s)):
        if searchword(dict, s[i:]):
            splitarray.append(s[i:])
            splitarray.extend(RMM(dict, s[:i]))
            break

    return splitarray


def searchword(dict, word):
    for i in xrange(len(dict)):
        if dict[i] == word:
            return True
    return False


def FMM(dict, s):
    splitarray = []
    for i in xrange(len(s)-1, 0, -1):
        if searchword(dict, s[:i]):
            splitarray.append(s[:i])
            splitarray.extend(RMM(dict, s[i:]))
            break

    return splitarray


def printarray(array):
    for i in xrange(len(array)):
        print array[i]+" ",


if __name__ == '__main__':
    file = open('ce.txt', 'r')
    dict = []
    while True:
        word = file.readline()
        if not word:
            break
        word = word.split(',')[0]
        dict.append(unicode(word, 'gbk'))

    while True:
        sentence = raw_input("请输入一句话: ")
        if sentence == "":
            break
        sentence = unicode(sentence, 'utf-8')
        array1 = FMM(dict, sentence)
        array2 = RMM(dict, sentence)

        length = min(len(array1), len(array2))
        identical = True
        for i in xrange(length):
            if array1[i] != array2[i]:
                pass
                identical = False
                break
        if identical:
            printarray(array1)
