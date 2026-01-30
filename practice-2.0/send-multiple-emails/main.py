import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
try:
    ob.login('xyz@gmail.com', 'skhp hgas asds tdga')
except Exception as e:
    print(f'Login failed: {e}')
else:
    print('Login successful')
subject = 'Test Mail'
body = 'This is a test mail sent using Python.'
message = f'Subject: {subject}\n\n{body}'
list_add = ['abc@gmail.com', 'def@gmail.com', 'ghi@gmail.com', 'jkl@gmail.com']
try:
    ob.sendmail('xyz@gmail.com', list_add, message)
except Exception as e:
    print(f'Error occurred: {e}')
else:
    print('Mail sent successfully')
ob.quit()


'''
# ============================================================================
# EMAIL AUTOMATION SCRIPT USING SMTP (Gmail)
# ============================================================================
# This script connects to Gmail's SMTP server, authenticates, and sends
# an email to multiple recipients with proper error handling
# ============================================================================

import smtplib as s

# ============================================================================
# STEP 1: ESTABLISH CONNECTION TO GMAIL'S SMTP SERVER
# ============================================================================
# Create an SMTP (Simple Mail Transfer Protocol) object
# 'smtp.gmail.com' = Gmail's outgoing mail server address
# 587 = Port number for TLS encryption (standard for secure SMTP)
ob = s.SMTP('smtp.gmail.com', 587)

# ============================================================================
# STEP 2: INITIATE HANDSHAKE WITH THE SERVER
# ============================================================================
# Send EHLO (Extended Hello) command to identify client to the server
# This establishes the connection and checks what features the server supports
# Required before any SMTP commands can be executed
ob.ehlo()

# ============================================================================
# STEP 3: ENABLE ENCRYPTION FOR SECURE COMMUNICATION
# ============================================================================
# Upgrade the connection to TLS (Transport Layer Security)
# Encrypts all data transmitted between client and server
# Protects sensitive information like login credentials and email content
# MUST be called before login() to ensure credentials are encrypted
ob.starttls()

# ============================================================================
# STEP 4: AUTHENTICATE WITH GMAIL ACCOUNT (WITH ERROR HANDLING)
# ============================================================================
try:
    # Attempt to log in to Gmail account
    # 'xyz@gmail.com' = sender's email address
    # 'skhp hgas asds tdga' = App Password (NOT regular Gmail password)
    # 
    # NOTE: App Passwords are 16-character codes generated from Google Account
    # Required when 2-Factor Authentication is enabled
    # Generate at: https://myaccount.google.com/apppasswords
    ob.login('xyz@gmail.com', 'skhp hgas asds tdga')

except Exception as e:
    # If login fails (wrong credentials, network issues, account restrictions)
    # Print detailed error message showing what went wrong
    print(f'Login failed: {e}')

else:
    # This block executes ONLY if login was successful (no exception occurred)
    # Confirms that authentication completed without errors
    print('Login successful')

# ============================================================================
# STEP 5: COMPOSE THE EMAIL MESSAGE
# ============================================================================
# Define the subject line of the email
subject = 'Test Mail'

# Define the main content/body of the email
body = 'This is a test mail sent using Python.'

# Construct the complete email message with proper formatting
# Email format requires: 'Subject: <text>\n\n<body>'
# - First line: Subject header
# - \n\n: Two newlines separate headers from body (REQUIRED)
# - Remaining text: Email body content
message = f'Subject: {subject}\n\n{body}'

# ============================================================================
# STEP 6: DEFINE RECIPIENT EMAIL ADDRESSES
# ============================================================================
# Create a list of recipient email addresses
# The email will be sent to ALL addresses in this list
# Can contain 1 to many recipients
list_add = [
    'abc@gmail.com',      # Recipient 1
    'def@gmail.com',      # Recipient 2
    'ghi@gmail.com',      # Recipient 3
    'jkl@gmail.com'       # Recipient 4
]

# ============================================================================
# STEP 7: SEND THE EMAIL (WITH ERROR HANDLING)
# ============================================================================
try:
    # Attempt to send the email to all recipients
    # sendmail() parameters:
    # 1. from_addr: Sender's email (must match the logged-in account)
    # 2. to_addrs: Recipient(s) - can be a string or list
    # 3. msg: Complete message including headers and body
    ob.sendmail('xyz@gmail.com', list_add, message)

except Exception as e:
    # If sending fails (invalid email, network issue, server rejection, etc.)
    # Print detailed error message showing the specific problem
    # Common errors: 
    # - SMTPRecipientsRefused: Invalid recipient address
    # - SMTPServerDisconnected: Connection lost
    # - SMTPDataError: Message format issues
    print(f'Error occurred: {e}')

else:
    # This block executes ONLY if email was sent successfully (no exception)
    # Confirms that all recipients received the email
    print('Mail sent successfully')

# ============================================================================
# STEP 8: CLEANUP - CLOSE THE SMTP CONNECTION
# ============================================================================
# Terminate the SMTP session and close the connection to the server
# Important to:
# - Free up server resources
# - Prevent leaving orphaned connections
# - Ensure proper cleanup even if errors occurred
# Always call quit() at the end, regardless of success/failure
ob.quit()
'''