with open('BT.txt') as f:
    lines = f.readlines()
    print([x.strip().split('\t') for x in lines[4:]])
