# Coin Change Problem

def rec_coin_dynam(target, coins, cache):

    min_coins = target

    if target in coins:
        cache[target]= 1
        return 1

    elif cache[target] > 0:
        return cache[target]

    else:

        for coin in [c for c in coins if c <= target]:

            number_coins = 1 + rec_coin_dynam(target-coin, coins, cache)

            if(number_coins < min_coins):
                cache[target] = number_coins
                min_coins = number_coins

    return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)

rec_coin_dynam(target,coins,known_results)
