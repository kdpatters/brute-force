if __name__ == '__main__':
    import string
    import time

    # Constants
    alphabet = string.ascii_lowercase
    secret = "hello"
    # Wrapper function  
    test_guess = lambda your_guess: your_guess == secret
    length = len(alphabet) - 1 # Count from 0

    brute_force(test_guess, alphabet)

def brute_force(test_guess, alphabet, min_len = 0, max_len = 16, \
    verbose = False):
    '''
    Brute force a string that makes the function `test_guess` true,
    using the `alphabet` specified.  Print the correct string if found.
    :test_guess: a function which returns true or false when called on a
        string
    :alphabet: list of base strings out of which to construct the outputs
    :min_len: minimum length of string to search
    :max_len: maximum length of string to search
    '''
    # Initialize guess variables
    guess_index = []
    guess_arr = []
    guess = ''.join(guess_arr)
    curr_len = min_len
    start = time.clock() # Start a timer

    n_possible = 1
    not_finished = test_guess(guess) # Check empty string as a guess
    if verbose: print("Current guess: %s" % (guess))
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
            if verbose: print("Current guess: %s" % (guess))
            # Check if our guess was correct before continuing
            not_finished = test_guess(guess)
        not_finished &= curr_len < max_len # Check we're less than max length
                
    # Show result
    if test_guess(guess):
        print("Guessed in %0.1f seconds." % (time.clock() - start))
        print(guess)    
    else:
        print("Did not find valid solution within given lengths and" / +
              " alphabet.")                         