def generate_fibonacci(N):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < N:
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    return fibonacci_sequence

# Input the value of N
N = int(input())

# Generate the first N Fibonacci numbers
fibonacci_numbers = generate_fibonacci(N)

# Print the result as space-separated integers
print(" ".join(map(str, fibonacci_numbers)))