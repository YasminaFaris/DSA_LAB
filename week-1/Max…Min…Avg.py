"""Max…Min…Avg"""
import json
def main():
    """maxminavg"""
    my_list = json.loads(input())
    a = 0
    mib = my_list[0]
    c = 0
    d = 0
    for i in my_list:
        if i > a:
            a = i
    for j in my_list:
        if j < mib:
            mib = j
    for i in my_list:
        c += i
        d += 1
    print(f"({a}, {mib}, {c/d:.2f})")
main()
