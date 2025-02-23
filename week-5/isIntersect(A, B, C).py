import json
def isIntersect(a, b, c):
    for i in a:
        if i in b and i in c:
            return True
    return False

result = isIntersect(json.loads(input()), json.loads(input()), json.loads(input()))
print(result)