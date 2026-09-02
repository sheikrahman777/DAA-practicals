print("**ITERATIVE FACTORIAL**")
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num_iter = int(input("Enter a single non-negative integer for iterative factorial: ").strip())
print(f"Iterative factorial of {num_iter} is: {iterative_factorial(num_iter)}")

print("\n**RECURSIVE FACTORIAL**")
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

num_rec = int(input("Enter a single non-negative integer for recursive factorial: ").strip())
print(f"Recursive factorial of {num_rec} is: {recursive_factorial(num_rec)}")
