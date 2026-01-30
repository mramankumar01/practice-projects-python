from time import *
import random as rd

def mistakes(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    error_count = 0
    mistake_list = []

    for o_word, t_word in zip(original_words, typed_words):
        if o_word != t_word:
            error_count += 1
            mistake_list.append(f'{o_word} -> {t_word}')

    # Count any extra words typed
    error_count += abs(len(original_words) - len(typed_words))

    return error_count, mistake_list

def wpm(original, typed, elapsed_time):
    typed_words = len(typed.split())
    minutes = elapsed_time / 60
    return (typed_words / minutes) if minutes > 0 else 0

test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.", "A paragraph consists of one or more sentences that are grouped together to express a single thought or topic.", "Paragraphs are used to organize and structure written content, making it easier for readers to follow and understand the information being presented.", "They typically begin with a topic sentence that introduces the main idea, followed by supporting sentences that provide details, examples, or explanations related to that idea. Paragraphs can vary in length, but they should always maintain coherence and unity around the central theme."]

test1 = rd.choice(test)
print("***** Typing Test *****")
print("Type the following paragraph as quickly and accurately as you can:")
print(test1)
print()
print()
start_time = time()
test_input = input("Start typing here:\n")
end_time = time()
print(f"Time taken: {(end_time - start_time)/60} minutes")
print(f"Your typing speed is {wpm(test1, test_input, end_time - start_time)} words per minute.")
print(f"You made {mistakes(test1, test_input)} mistakes.")


'''
# ============================================================================
# TYPING SPEED TEST PROGRAM
# ============================================================================
# This program measures typing speed (WPM) and accuracy by comparing
# user input against a randomly selected paragraph
# ============================================================================

from time import *       # Import all time-related functions (time, sleep, etc.)
import random as rd      # Import random module as 'rd' for selecting test paragraphs

# ============================================================================
# FUNCTION 1: COUNT TYPING MISTAKES
# ============================================================================
def mistakes(original, typed):
    """
    Compares the original text with typed text to count errors.
    
    Parameters:
    - original: The correct paragraph that should be typed
    - typed: The text that the user actually typed
    
    Returns:
    - error_count: Total number of mistakes made
    - mistake_list: List of incorrect word pairs (original -> typed)
    """
    
    # Split both strings into lists of individual words
    # Example: "Hello world" becomes ["Hello", "world"]
    original_words = original.split()
    typed_words = typed.split()
    
    # Initialize counter for errors
    error_count = 0
    
    # List to store specific mistakes (which words were wrong)
    mistake_list = []

    # Compare words one-by-one using zip()
    # zip() pairs up corresponding words from both lists
    # Example: zip(["Hi", "there"], ["Hi", "their"]) → [("Hi", "Hi"), ("there", "their")]
    for o_word, t_word in zip(original_words, typed_words):
        # Check if the original word doesn't match the typed word
        if o_word != t_word:
            error_count += 1  # Increment error counter
            # Record the mistake in format: "correct_word -> wrong_word"
            mistake_list.append(f'{o_word} -> {t_word}')

    # Account for missing or extra words
    # If user typed fewer or more words than original, count as errors
    # abs() ensures the difference is always positive
    # Example: original has 10 words, typed has 8 → adds 2 errors
    error_count += abs(len(original_words) - len(typed_words))

    # Return both the total error count and the list of specific mistakes
    return error_count, mistake_list

# ============================================================================
# FUNCTION 2: CALCULATE WORDS PER MINUTE (WPM)
# ============================================================================
def wpm(original, typed, elapsed_time):
    """
    Calculates typing speed in words per minute.
    
    Parameters:
    - original: The correct paragraph (not used in calculation, but kept for consistency)
    - typed: The text typed by the user
    - elapsed_time: Time taken to type (in seconds)
    
    Returns:
    - WPM (words per minute) as a float
    """
    
    # Count the number of words typed by the user
    # split() breaks the string into words and len() counts them
    typed_words = len(typed.split())
    
    # Convert elapsed time from seconds to minutes
    # Example: 30 seconds → 0.5 minutes
    minutes = elapsed_time / 60
    
    # Calculate WPM: total words divided by minutes
    # If minutes is 0 (instant typing), return 0 to avoid division by zero
    # Ternary operator: (value_if_true) if condition else (value_if_false)
    return (typed_words / minutes) if minutes > 0 else 0

# ============================================================================
# STEP 1: PREPARE TEST PARAGRAPHS
# ============================================================================
# Create a list of sample paragraphs for the typing test
# User will randomly get one of these paragraphs to type
test = [
    "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
    "A paragraph consists of one or more sentences that are grouped together to express a single thought or topic.",
    "Paragraphs are used to organize and structure written content, making it easier for readers to follow and understand the information being presented.",
    "They typically begin with a topic sentence that introduces the main idea, followed by supporting sentences that provide details, examples, or explanations related to that idea. Paragraphs can vary in length, but they should always maintain coherence and unity around the central theme."
]

# ============================================================================
# STEP 2: SELECT RANDOM PARAGRAPH
# ============================================================================
# rd.choice() randomly picks one paragraph from the test list
# Each time the program runs, user gets a different paragraph (possibly)
test1 = rd.choice(test)

# ============================================================================
# STEP 3: DISPLAY INSTRUCTIONS AND TEST PARAGRAPH
# ============================================================================
print("***** Typing Test *****")
print("Type the following paragraph as quickly and accurately as you can:")
print(test1)       # Display the randomly selected paragraph
print()            # Blank line for spacing
print()            # Another blank line for better readability

# ============================================================================
# STEP 4: START TIMER AND GET USER INPUT
# ============================================================================
# Record the current time in seconds (Unix timestamp)
# This marks the START of the typing test
start_time = time()

# Wait for user to type the paragraph
# input() pauses execution until user presses Enter
# Everything typed is stored in test_input variable
test_input = input("Start typing here:\n")

# Record the current time again (Unix timestamp)
# This marks the END of the typing test
end_time = time()

# ============================================================================
# STEP 5: CALCULATE AND DISPLAY RESULTS
# ============================================================================
# Calculate elapsed time by subtracting start from end
# Divide by 60 to convert seconds to minutes
print(f"Time taken: {(end_time - start_time)/60} minutes")

# Call wpm() function to calculate typing speed
# Display result rounded to appropriate decimal places
print(f"Your typing speed is {wpm(test1, test_input, end_time - start_time)} words per minute.")

# Call mistakes() function to count errors
# Display total number of mistakes made
# Note: This prints a tuple (error_count, mistake_list)
print(f"You made {mistakes(test1, test_input)} mistakes.")
'''