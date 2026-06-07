def lcg(seed, a, c, m, length):
    sequence = []
    x = seed
    for _ in range(length):
        x = (a * x + c) % m
        sequence.append(x)
    return sequence

seed = 7
a = 1664525
c = 1013904223
m = 2**32

sequence = lcg(seed, a, c, m, 20)

print(f"Seed:       {seed}")
print(f"Parameters: a={a}, c={c}, m={m}")
print(f"\nGenerated sequence (20 values):")
for i, val in enumerate(sequence):
    print(f"  [{i+1:02}] {val}")