import os

path = os.getcwd()
    
def dir_show(path, level):
    x = level * '--'
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path,item)
        if os.path.isfile(item_path):
            print(''.join([x,item]))
        elif os.path.isdir(item_path):
            print(''.join([x,'[',item,']']))
            dir_show(item_path, level + 1)
            
dir_show(path,0)
