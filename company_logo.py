# if __name__ == '__main__':
#     s = input().lower()
#     char_list={}
#     for char in s:
#         char_list[char]=char_list.get(char,0)+1
#     sorted_char=sorted(char_list.items(),key=lambda item: (-item[1], item[0]))
#     for key, count in sorted_char[:3]:
#         print(key, count)

from collections import Counter
s = input().strip()
counts = Counter(sorted(s))
for char, count in counts.most_common(3):
    print(char, count)