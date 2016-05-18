# applycipher.py
# A program to encrypt/decrypt user text        
# Using Caesar's Cipher
#
# Author: rc.grisby.garlandrhea [at] leadps.org

# Makes a mapping of encoded alphabet to decoded alphabet
# Arguments: Key
# Returns: Dictionary of mapped letters
def createdictionary(key):

        # Placeholder
        return{}

# Gets the encrypted message from the user
# Arguments: None
# Returns: Encoded message
def getmessage():
        pass

# For each letter in the message, it decodes and records
# Arguments: Encoded message, Dictionary
# Returns decoded message
def decodemessage(message, dictionary):
        pass

# Gets the encrypted message from the user
# Arguments: None
# Returns: Encoded message
def getmessage():
        pass

# For each letter in the message, it decodes and records
# Arguments: Encoded message, Dictionary
# Returns decoded message
def decodemessage(message, dictionary):
        pass


# Outputs the decoded message to the terminal
# Arguments: Decoded message
# Returns: None
def printmessage(message):
        pass


# Execution starts here

# Ask user for key
print('What key would you like to use to decode')
key = int(raw_input())

dictionary = createdictionary(key)
encodedmessage = getmessage()
decodedmessage = decodemessage(message, dictionary)

printmessage(decodedmessage)
