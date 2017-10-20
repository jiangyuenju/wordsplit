# -*- coding: utf-8 -*-
import math


def wordsplit(mydict, f, s):
    a1 = fmm(mydict, s)
    a2 = rmm(mydict, s)
    length = min(len(a1), len(a2))
    a = a1
    for i in xrange(length):
        if a1[i] != a2[i]:
            last1 = last2 = i+3
            if (i+3) > len(a1):
                last1 = len(a1)
            if (i+3) > len(a2):
                last2 = len(a2)
            chunk1 = a1[i:last1]
            chunk2 = a2[i:last2]
            index = choosechunk(chunk1, chunk2, f)
            break

    printarray(a1, a2, index)


def printarray(a1, a2, type):
    if type == 1:
        for i in xrange(len(a1)):
            print a1[i]+" ",
        print ""
    else:
        for i in xrange(len(a2)-1, -1, -1):
            print a2[i]+" ",
        print ""


def choosechunk(c1, c2, f):
    # maximum matching
    total_l1 = 0
    total_l2 = 0
    for i in xrange(len(c1)):
        total_l1 += len(c1[i])
    for i in xrange(len(c2)):
        total_l2 += len(c2[i])
    print("total length1: %d, total length2: %d" % (total_l1, total_l2))
    if total_l1 > total_l2:
        return 1
    elif total_l1 < total_l2:
        return 2

    # largest average word length
    average_l1 = total_l1 / len(c1)
    average_l2 = total_l2 / len(c2)
    print("average length1: %d, average length2: %d" % (average_l1, average_l2))
    if average_l1 > average_l2:
        return 1
    elif average_l1 < average_l2:
        return 2

    # smallest variance of word length
    var_1 = 0.0
    var_2 = 0.0
    for i in xrange(len(c1)):
        var_1 += (len(c1[i]) - average_l1) ** 2
    var_1 = var_1 / len(c1)
    for i in xrange(len(c2)):
        var_2 += (len(c2[i]) - average_l2) ** 2
    var_2 = var_2 / len(c2)
    print("var1: %f, var2: %f" % (var_1, var_2))
    if var_1 < var_2:
        return 1
    elif var_1 > var_2:
        return 2

    # Largest sum of degree of morphemic freedom of one-character words
    log1 = log2 = 0.0
    for i in xrange(len(c1)):
        if len(c1[i]) == 1:
            log1 += math.log(float(f[c1[i]]))
    for i in xrange(len(c2)):
        if len(c2[i]) == 1:
            log2 += math.log(float(f[c2[i]]))
    print("log1: %f, log2: %f" % (log1, log2))
    if log1 >= log2:
        return 1
    else:
        return 2


def fmm(mydict, s):
    splitarray = []

    for i in xrange(len(s), 0, -1):
        word = s[:i]
        if searchword(mydict, word):
            splitarray.append(word)
            splitarray.extend(fmm(mydict, s[i:]))
            break

    return splitarray


def rmm(mydict, s):
    splitarray = []
    for i in xrange(len(s)):
        if searchword(mydict, s[i:]):
            splitarray.append(s[i:])
            splitarray.extend(rmm(mydict, s[:i]))
            break

    return splitarray


def searchword(mydict, word):
    for i in xrange(len(mydict)):
        if word == mydict[i]:
            return True
    return False


if __name__ == '__main__':
    file = open('ce.txt', 'r')
    words = []
    while True:
        line = file.readline()
        if not line:
            break
        word = line.split(",")[0]
        words.append(unicode(word, 'gbk', 'ignore'))

    file2 = open('chars.dic', 'r')
    freq = {}
    while True:
        line = file2.readline()
        if not line:
            break
        word_freq = line.split(" ")
        word_freq[0] = unicode(word_freq[0], 'utf-8')
        freq[word_freq[0]] = word_freq[1]

    while True:
        sentence = raw_input("输入一个句子: ")
        if sentence == "":
            break
        sentence = sentence.decode('utf-8')
        wordsplit(words, freq, sentence)
