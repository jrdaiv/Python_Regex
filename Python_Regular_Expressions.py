import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", 
         "Jordan Alexander Williams", "Madonna", "programming is cool"]

def validate(names):
    pattern = re.compile(r"([A-Z]+?)+[^Ma]")
        
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid Name")


validate(names)














