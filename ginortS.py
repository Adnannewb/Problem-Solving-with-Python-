s = input()
def sort_key(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit():
        if int(c) % 2 != 0:
            return (2, c)  
        else:
            return (3, c)  


print("".join(sorted(s, key=sort_key)))