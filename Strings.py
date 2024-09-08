#Length

len("These aren't the droids you're looking for.")

#ALL CAPS

str = 'confetti floating everywhere'

str.upper()

#Ignoring Case

name = 'Roger'
str = 'RoGeR'
str2 = 'DAVE'

print(name.casefold() == str.casefold())
print(name.casefold() == str2.casefold())

#Multiline String

str = "A pirate I was meant to be!\nTrim the sails and roam the sea!"

str = '''A pirate I was meant to be!
Trim the sails and roam the sea!
'''

print(str)

#Contains Character

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

char_sequence.find('x')

print('x' in char_sequence)

#Is Empty?

def is_empty(string):
    return len(string) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# Is Empty or Blank?

def is_empty_or_blank(string):
     return not string.strip()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# Capitalize Words

'launch school tech & talk'.title()

# Check Prefix

def starts_with(string, prefix):
     index = len(prefix) 
     return string[0:index] == prefix
     

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

#THERE IS A STARTSWITH BUILT IN METHOD
def starts_with(string, prefix):
    return string.startswith(prefix)

# Count Substrings

def count_substrings(string, substring):
     return string.count(substring)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0