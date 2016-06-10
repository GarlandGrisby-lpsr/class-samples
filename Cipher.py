# Done in Trinket.io
# Will NOT work outside of Trinket.io


# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesar's Cipher
# 
# Author: mflax [at] leadps.org

# makes a mapping of encoded alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
import string
def createDictionary(key):
  alphacode = list(string.ascii_lowercase)
  alphacode = list(string.ascii_uppercase)
  setUp = {}
  count = 0
  for a in alphacode:
    setUp[a] = alphacode[(count + key) % 26]
    count += 1
  return setUp
  




# gets the encrypted message from the user
# arguments: none
# returns: encoded message
def getMessage(message):
	return message

# for each letter in message, decodes and records
# arguments: encoded message, dictionary
# returns: decoded message
def decodeMessage(message, dictionary):
  newStr = ''
  for m in message:
    newMsg = dictionary[m]
    newStr = newStr + newMsg
  return newStr
    
  
    
# outputs the decoded message to the terminal
# arguments: decoded message
# returns: none
def printMessage(decMessage):
	print(decMessage)


# execution starts here

# ask user for key
print("What key would you like to use to decode?")
key = int(raw_input())
dictionary = createDictionary(key)
print('What is the message you would like to decode?')
blip = raw_input()


encodedMessage = getMessage(blip)
decodedMessage = decodeMessage(encodedMessage, dictionary)
print("")
print("Here is your decoded message:")
printMessage(decodedMessage)
