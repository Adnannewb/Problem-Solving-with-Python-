def merge_the_tools(string, k):
    # your code goes here
    text=[string[i:i+k] for i in range(0,len(string),k)]
    for element in text:
        result=set(element)
        print("".join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)