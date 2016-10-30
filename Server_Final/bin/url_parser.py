#!/usr/bin/python3

#import queue
import Q

#address = queue.Queue(maxsize=0)

def parse(string):
    if '/' in string:
        idx = string.find('/')
        string = string[idx+1:]
        if '/' in string:
            idx = string.find('/')
            path = string[:idx]
            string = string[idx:]
            #print(path)
            #print(string)
            Q.push(path)
        elif len(string) > 0:
            #print(string)
            #print(len(string))
            Q.push(string)
            string=""
    if len(string) == 0:
        return
    elif len(string) == 1 and string=='/':
        string=None
        return
    else:
        parse(string)

def main():
    #testing purpose
    path = "/example.com/test/best/index.html"
    poth = "/example.com/test/best/public_index.html"
    parse(path)
    print("First:")
    #print(address.empty())
    while not Q.isEmpty():
        print(Q.pop())
    print("Second:")

    parse(poth)

    while not Q.isEmpty():
        print(Q.pop())
    print("END")

if __name__ == "__main__":
    main()
