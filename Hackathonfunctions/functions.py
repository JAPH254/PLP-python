def fibonacci(n):
  """
  This function generates the Fibonacci sequence up to a specified term n using iteration.

  Args:
      n: The number of terms in the Fibonacci sequence.

  Returns:
      A list containing the Fibonacci sequence up to n terms.
  """
  if n <= 1:
    return n  # Base case: the first two terms are 0 and 1
  else:
    a, b = 0, 1  # Initialize variables for the first two terms
    for _ in range(2, n + 1):
      c = a + b  # Calculate the next term
      a, b = b, c  # Update variables for the next iteration
    return c  # Return the last calculated term (nth term)

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms: "))

# Generate the Fibonacci sequence
fibonacci_sequence = []
for i in range(num_terms):
  fibonacci_sequence.append(fibonacci(i))

# Print the Fibonacci sequence
print(fibonacci_sequence)
