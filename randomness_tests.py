def frequency_test(sequence):
    ones = sum(sequence)
    zeros = len(sequence) - ones
    total = len(sequence)
    print("=== Frequency Test ===")
    print(f"Total bits: {total}")
    print(f"Ones:       {ones} ({(ones/total)*100:.1f}%)")
    print(f"Zeros:      {zeros} ({(zeros/total)*100:.1f}%)")
    balance = abs(ones - zeros) / total
    print(f"Balance:    {'PASS' if balance < 0.1 else 'FAIL'}")

def runs_test(sequence):
    runs = 1
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            runs += 1
    expected = (2 * sum(sequence) * (len(sequence) - sum(sequence))) / len(sequence)
    print("\n=== Runs Test ===")
    print(f"Total runs:    {runs}")
    print(f"Expected runs: {expected:.1f}")
    print(f"Result:        {'PASS' if abs(runs - expected) < 10 else 'FAIL'}")

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

sequence = lfsr([1, 0, 1, 1], [0, 3], 100)
print(f"Testing sequence of {len(sequence)} bits\n")
frequency_test(sequence)
runs_test(sequence)