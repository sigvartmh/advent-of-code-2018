from functools import reduce
from collections import Counter

def read_file(fn):
    f = open(fn)
    txt = f.read()
    return txt.splitlines()


def checksum(lst):
    values = list()
    for box_id in lst:
        letter_count = set(Counter(box_id).values())
        values.append(list(filter(lambda x: x > 1, letter_count)))
    flatten = [value for value_list in values for value in value_list] 
    return reduce(lambda x, y: x*y, Counter(flatten).values())

def check_difference(check_id, box_id):
   return len(set(check_id).difference(set(box_id)))

def common_letters(lst):
    matches = []
    for y in lst:
        matches.append([set(x).intersection(set(y)) for x in lst if check_difference(x,y) == 1])
    print(matches)
    #return reduce(lambda x, 
lst = read_file("input")
chk = checksum(lst)
common = common_letters(lst)
print(common)
print(chk)
