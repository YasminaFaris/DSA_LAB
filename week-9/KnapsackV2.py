import json
def knapsackV2(amount, itemList):
    n = len(itemList)

    dp = [0] * (amount + 1)
    keep = [[False] * (amount + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, price, weight = itemList[i - 1]
        for j in range(amount, weight - 1, -1):
            if dp[j - weight] + price > dp[j]:
                dp[j] = dp[j - weight] + price
                keep[i][j] = True
    total = dp[amount]

    selected = []
    j = amount
    for i in range(n, 0, -1):
        if keep[i][j]:
            name, price, weight = itemList[i - 1]
            selected.append((name, price, weight))
            j -= weight

    selected.sort(key=lambda x: x[0])

    print(f"Total: {total}")
    for name, price, weight in selected:
        print(f"{name} -> {weight} kg -> {price} THB")

def main():
    itemList = json.loads(input())
    amount = int(input())

    knapsackV2(amount, itemList)
main()
