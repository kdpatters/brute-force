import string
import time

# Constants
alphabet = string.ascii_lowercase
secret = "hello"
length = len(alphabet) - 1 # Count from 0

# Initialize guess variables
guess_index = []
guess_arr = []
guess = ''.join(guess_arr)
min_len = 0
max_len = 16
curr_len = min_len
start = time.clock() # Start a timer

n_possible = 1
not_finished = secret != guess # Check empty string as a guess
#print("Current guess: %s" % (guess))
# Keep guessing until we find the answer
while not_finished:
    curr_len +=1 # Increase the length of our guess
    guess_index = [0,] * curr_len # Array to store index of symbols
    guess_arr = [alphabet[0],] * curr_len # Initialize empty array

    # For a string of length `n` with `k` choices for each character,
    # there will be k^n total possible strings, which we iterate
    # through
    n_possible *= len(alphabet)
    i = 0
    while (not_finished & (i < n_possible)):
        i += 1
        j = curr_len - 1 # Index of last element in list `guess_index`
        while (guess_index[j] == length):
            guess_index[j] = 0
            j -= 1
        guess_index[j] += 1
        guess_arr[j] = alphabet[guess_index[j]]
        # Update previous symbols
        for k in range(j+1, curr_len):
            guess_arr[k] = alphabet[0]
        guess = ''.join(guess_arr)
        #print("Current guess: %s" % (guess))
        # Check if our guess was correct before continuing
        not_finished = (secret != guess)
    not_finished &= curr_len < max_len # Check we're less than max length
            
# Show result
print("Guessed in %0.1f seconds." % (time.clock() - start))
print(guess)                             