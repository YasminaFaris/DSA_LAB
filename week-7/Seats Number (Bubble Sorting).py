import json
def bubbleSort(list, last):
    current = 0
    sorted = False
    compare = 0
    while current <= last and sorted is False:
        walker = last
        sorted = True
        while walker > current:
            compare += 1
            if (list[walker][0] < list[walker - 1][0]):
                sorted = False
                list[walker], list[walker-1] = list[walker-1], list[walker]
            elif list[walker][0] == list[walker - 1][0]:
                if int(list[walker][1:]) < int(list[walker - 1][1:]):
                    sorted = False
                    list[walker], list[walker-1] = list[walker-1], list[walker]
            walker -= 1
        current += 1
        print(list)
    print("Comparison times:", compare)
bubbleSort(json.loads(input()), int(input()))