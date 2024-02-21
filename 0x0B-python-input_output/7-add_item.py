#!/usr/bin/python3
""" Adds Items to Json file """


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = []
try:
    args = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

for arg in sys.argv[1:]:
    args.append(arg)

save_to_json_file(args, "add_item.json")
