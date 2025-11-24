#character hashing 
s="azyxyyzaaaa"
q=["d","a","y","x"]
freq_map=dict()
for ch in s:
    freq_map[ch]=freq_map.get(ch,0)+1 
for ch in q:
    if(ch in freq_map):
        print(freq_map[ch])
    else:print(0)               