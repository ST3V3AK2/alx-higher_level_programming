#!/usr/bin/python3
for i in range(97, 122 + 1):
    if chr(i) not in 'qe':
        print(f"{chr(i)}", end="")
