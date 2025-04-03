def coinExchangeV2(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    coin_count = {int(coin): coins[coin] for coin in coins}

    for coin in sorted(coin_count.keys(), reverse=True):
        max_count = coin_count[coin]
        for i in range(amount, coin - 1, -1):
            for count in range(1, max_count + 1):
                if i - coin * count >= 0 and dp[i - coin * count] + count < dp[i]:
                    dp[i] = dp[i - coin * count] + count
                    coin_used[i] = coin

    if dp[amount] == float('inf'):
        print(f"Amount: {amount}")
        print("Can not exchange.")
        return

    print(f"Amount: {amount}")
    print("Coin exchange result:")

    remaining = amount
    used_coins = {coin: 0 for coin in coin_count}
    total_coins = 0

    while remaining > 0:
        coin = coin_used[remaining]
        if coin != -1:
            used_coins[coin] += 1
            total_coins += 1
            remaining -= coin
        else:
            break

    for coin in sorted(used_coins.keys(), reverse=True):
        print(f"  {coin} baht = {used_coins[coin]} coins")

    print(f"Number of coins: {total_coins}")

def main():
    import json
    amount = int(input())
    coins = json.loads(input())
    coinExchangeV2(amount, coins)
main()
