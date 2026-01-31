from deep_translator import GoogleTranslator

# Get supported languages as a dictionary (code: name)
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

# Create reverse mapping (name: code) for easier lookup
LANG_CODES = {v: k for k, v in LANGUAGES.items()}

print("***** Supported Languages *****")
for lang, code in LANGUAGES.items():
    print(f"{lang} -> {code}")

src_lang = input("Enter source language code: ").lower()
src_text = input('Enter the text to translate: \n')

tgt_lang = input("Enter target language code: ").lower()

# Check if input is a language name (e.g., "english") or code (e.g., "en")
if src_lang in LANGUAGES:
    src_code = src_lang
elif src_lang in LANG_CODES:
    src_code = LANG_CODES[src_lang]
else:
    print("Invalid source language code!")
    exit()

if tgt_lang in LANGUAGES:
    tgt_code = tgt_lang
elif tgt_lang in LANG_CODES:
    tgt_code = LANG_CODES[tgt_lang]
else:
    print("Invalid target language code!")
    exit()

try:
    translated = GoogleTranslator(source=src_code, target=tgt_code).translate(src_text)
    print("***** Translated Text *****")
    print(translated)
except Exception as e:
    print("Translation Failed: ", e)


'''
**Now you can use either:**
- Short codes: `en`, `hi`, `fr`
- Full names: `english`, `hindi`, `french`

**Example:**
Enter source language code: en
Enter the text to translate: 
Bobby is a Python Backend AI engineer.
Enter target language code: hi
***** Translated Text *****
बॉबी एक पायथन बैकएंड एआई इंजीनियर हैं।
'''

'''
# CORE LOGIC:
----------------------------------------------
from deep_translator import GoogleTranslator

source_lang = input("Enter source language code: ")
text = input("Enter the text to translate: ")
target_lang = input("Enter target language code: ")

try:
    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    print("***** Translated Text *****")
    print(translated)
except Exception as e:
    print(f"Translation Failed: {e}")
'''

'''
# ============================================================================
# LANGUAGE TRANSLATION PROGRAM USING GOOGLE TRANSLATE API
# ============================================================================
# This program translates text from one language to another using the
# deep_translator library, which interfaces with Google Translate
# ============================================================================

from deep_translator import GoogleTranslator

# ============================================================================
# STEP 1: RETRIEVE SUPPORTED LANGUAGES
# ============================================================================
# Get a dictionary of all languages supported by Google Translate
# Format: {language_code: language_name}
# Example: {'en': 'english', 'es': 'spanish', 'fr': 'french', ...}
# 
# as_dict=True returns a dictionary instead of a list
# This makes it easier to look up languages by their codes
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)

# ============================================================================
# STEP 2: CREATE REVERSE MAPPING FOR FLEXIBLE INPUT
# ============================================================================
# Create a reverse dictionary: {language_name: language_code}
# Example: {'english': 'en', 'spanish': 'es', 'french': 'fr', ...}
# 
# Dictionary comprehension: {new_key: new_value for old_key, old_value in dict.items()}
# This swaps keys and values from LANGUAGES dictionary
# 
# Purpose: Allows users to input either "en" OR "english" for English
LANG_CODES = {v: k for k, v in LANGUAGES.items()}

# ============================================================================
# STEP 3: DISPLAY ALL SUPPORTED LANGUAGES
# ============================================================================
print("***** Supported Languages *****")

# Loop through all language codes and their names
# Example output: "english -> en"
for lang, code in LANGUAGES.items():
    print(f"{lang} -> {code}")

# ============================================================================
# STEP 4: GET USER INPUT FOR TRANSLATION
# ============================================================================
# Get the source language (language of the original text)
# .lower() converts input to lowercase for case-insensitive matching
# User can enter either "en" or "english" or "English" (all valid)
src_lang = input("Enter source language code: ").lower()

# Get the text that needs to be translated
# \n creates a newline for better formatting
src_text = input('Enter the text to translate: \n')

# Get the target language (language to translate into)
# .lower() ensures case-insensitive matching
tgt_lang = input("Enter target language code: ").lower()

# ============================================================================
# STEP 5: VALIDATE AND NORMALIZE SOURCE LANGUAGE INPUT
# ============================================================================
# Check if user entered a valid language code or name
# This block handles THREE scenarios:

# SCENARIO 1: User entered a language CODE (e.g., "en")
if src_lang in LANGUAGES:
    # Code is valid, use it directly
    src_code = src_lang

# SCENARIO 2: User entered a language NAME (e.g., "english")
elif src_lang in LANG_CODES:
    # Name is valid, look up its corresponding code
    # Example: "english" -> "en"
    src_code = LANG_CODES[src_lang]

# SCENARIO 3: User entered something invalid (e.g., "xyz" or "alien")
else:
    # Input doesn't match any code or name
    print("Invalid source language code!")
    exit()  # Terminate the program immediately

# ============================================================================
# STEP 6: VALIDATE AND NORMALIZE TARGET LANGUAGE INPUT
# ============================================================================
# Exact same logic as Step 5, but for target language

# SCENARIO 1: User entered a language CODE (e.g., "es")
if tgt_lang in LANGUAGES:
    tgt_code = tgt_lang

# SCENARIO 2: User entered a language NAME (e.g., "spanish")
elif tgt_lang in LANG_CODES:
    # Look up the code for the language name
    # Example: "spanish" -> "es"
    tgt_code = LANG_CODES[tgt_lang]

# SCENARIO 3: Invalid input
else:
    print("Invalid target language code!")
    exit()  # Exit the program

# ============================================================================
# STEP 7: PERFORM TRANSLATION WITH ERROR HANDLING
# ============================================================================
try:
    # Create a GoogleTranslator object configured with:
    # - source: The language code of the original text
    # - target: The language code to translate into
    # 
    # .translate() performs the actual translation
    # Returns the translated text as a string
    # 
    # Example: GoogleTranslator(source='en', target='es').translate('Hello')
    # Returns: "Hola"
    translated = GoogleTranslator(source=src_code, target=tgt_code).translate(src_text)
    
    # Display the translated result
    print("***** Translated Text *****")
    print(translated)

except Exception as e:
    # Catch any errors that occur during translation:
    # - Network connectivity issues
    # - API rate limits exceeded
    # - Invalid text encoding
    # - Service unavailable
    # 
    # Display the specific error message to help diagnose the problem
    print("Translation Failed: ", e)
'''