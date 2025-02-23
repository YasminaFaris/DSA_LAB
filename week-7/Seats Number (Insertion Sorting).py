import json
def insertionSort(list, last):
    current = 1
    compare = 0
    while current <= last:
        hold = list[current]
        walker = current - 1
        while (walker >= 0 and hold[0]  < list[walker][0] or (hold[0]  == list[walker][0] and int(hold[1:])  < int(list[walker][1:]))):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        if walker >= 0:
            compare += 1
        list[walker+1] = hold
        current += 1
        print(list)
    print("Comparison times:",compare)
insertionSort(json.loads(input()), int(input()))