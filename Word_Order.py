from collections import OrderedDict
n=int(input())
word_list=OrderedDict()
for _ in range(n):
    word=input().lower().strip(" ")
    word_list[word]=word_list.get(word,0)+1
print(len(word_list))
counts=word_list.values()
print(*counts)


