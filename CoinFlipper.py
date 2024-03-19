import random

def coin_flip(num_flips):
    heads = 0
    tails = 0
    for _ in range(num_flips):
        if random.random() < 0.5:
            heads += 1
        else:
            tails += 1
    return heads, tails

num_flips = int(input("Enter the number of coin flips: "))
heads_count, tails_count = coin_flip(num_flips)
print(f"Heads: {heads_count}, Tails: {tails_count}")
