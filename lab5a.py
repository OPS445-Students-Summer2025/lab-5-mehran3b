#!/usr/bin/env python3
# Author ID: mebrahimi22

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except:
        return ""

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip('\n') for line in f.readlines()]
    except:
        return []

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
