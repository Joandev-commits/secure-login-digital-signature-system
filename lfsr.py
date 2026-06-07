def lfsr(seed, taps, length):
    state = seed[:]
    sequence = []
    for _ in range(length):
        output = state[0]
        sequence.append(output)
        feedback = 0
        for tap in taps:
            feedback ^= state[tap]
        state = state[1:] + [feedback]
    return sequence

seed = [1, 0, 1, 1]
taps = [0, 3]
length = 20

sequence = lfsr(seed, taps, length)
print(f"Seed:     {seed}")
print(f"Taps:     {taps}")
print(f"Sequence: {sequence}")
print(f"Length:   {length} bits")

# detect period
for period in range(1, length):
    if sequence[:period] == sequence[period:2*period]:
        print(f"Period:   {period}")
        break