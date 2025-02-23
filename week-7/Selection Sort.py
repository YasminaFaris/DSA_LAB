import json
def selectionSort(list, last):
    current = 0
    compare = 0
    while (current < last):
        smallest = current
        walker = current + 1
        while (walker <= last):
            compare += 1
            if (list[walker] < list[smallest]):
                smallest = walker
            walker += 1
        list[current], list[smallest] = list[smallest], list[current]
        print(list)
        current += 1
    print("Comparison times:", compare)
selectionSort(json.loads(input()), int(input()))