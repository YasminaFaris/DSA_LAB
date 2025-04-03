def coinExchange(amount, coins):
    result = {10: 0, 5: 0, 2: 0, 1: 0}

    for coin in [10, 5, 2, 1]:
        needed = min(amount // coin, coins[coin])
        result[coin] = needed
        amount -= needed * coin
    if amount > 0:
        return None
    return result

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    import json
    
    amount = int(input())
    coins = convert_key(json.loads(input()))
    
    result = coinExchange(amount, coins)
    
    print(f"Amount: {amount}")
    
    if result is None:
        print("Coins are not enough.")
    else:
        print("Coin exchange result:")
        for coin in [10, 5, 2, 1]:
            print(f"  {coin} baht = {result[coin]} coins")
        
        total_coins = sum(result.values())
        print(f"Number of coins: {total_coins}")

main()