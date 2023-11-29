#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i < j):
            print(f"{i}{j}", end="")
            if (i + j < 17):
                print(", ", end="")
            else:
                print("")
