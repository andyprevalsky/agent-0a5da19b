"""Compute and print the Collatz sequence starting from 27."""


def collatz(start):
    """Return (sequence, step_count) from start up to and including the first 1."""
    n = start
    sequence = [n]
    step_count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        step_count += 1
    return sequence, step_count


def main():
    sequence, step_count = collatz(27)

    for n in sequence:
        print(n)
    print(f"Total steps: {step_count}")

    assert sequence[0] == 27
    assert sequence[-1] == 1
    assert sequence.count(1) == 1
    assert step_count == len(sequence) - 1


if __name__ == "__main__":
    main()
