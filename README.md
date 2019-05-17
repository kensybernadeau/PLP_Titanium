import os
entries = os.listdir('PL_project/')

list_New = list()

for entry in entries:
    if(entry.endswith('.txt')):
        list_New.append(entry)

print(list_New)