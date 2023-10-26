"""
***Task***
Write a Python script to:

-Display all the prime numbers between 1 to 250.
-Store the results in a results.txt file.
Test the script. Verify that it produced the expected results in the results.txt file.

Save the script and make a note of its location (absolute path) for future reference.
"""
# defining a fucntion to check if its a prime number
def prime_no(n):

# starting loop at 2 and keep going until you reach the square root of n
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        
# Returns True if n is a prime number, and n/a if false
      return False
  return True
"""
if n % i == 0:
- If you can divide n by any number from 2 to its square root without getting a remainder, then n is not a prime number.
- If you cannot divide n by any number from 2 to its square root without getting a remainder, then n is a prime number.
- The remainder is calculated using the '%' operator in Python
"""
# creating list of the prime numbers
prime_numbers = []

# staring loop at 2 and keep going until 250
for i in range(2, 250):

# If the number is prime, add it to the list
  if prime_no(i):
    prime_numbers.append(i)

# Store the results in a results.txt file
with open("results.txt", "w") as f:
  for prime_number in prime_numbers:
    f.write(str(prime_number) + "\n")

# Print the results to the console
print(prime_numbers)