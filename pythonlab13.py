#!/usr/bin/env python3

import os

def what_size(path):
    size = 0
    if os.path.isfile(path):
        size=os.path.getsize(path)
    else:
        for dirpath,dirnames,filenames in os.walk(path):
            for filename in filenames:
                fpath=os.path.join(dirpath,filename)
                if os.path.isfile(fpath):
                    size += os.path.getsize(fpath)

    return size

def normal_size(size):
    for unit in ['b','kb','mb','gb']:
        if size < 1024:
            break
        size /= 1024
    return "{:.2f}{}".format(size,unit)

def main():
    pwd=os.getcwd()
    files=os.listdir(pwd)
    size_sorting= []

    for i in files:
        fpath=os.path.join(pwd,i)
        size=what_size(fpath)
        size_sorting.append((size,i))
    size_sorting.sort(key=lambda x: x[0], reverse=True)
    for size,i in size_sorting:
        print("\t{} -\t{}".format(normal_size(size),i))

if __name__=="__main__":
    main()

