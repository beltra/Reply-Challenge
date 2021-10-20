param0 = "nWXGn3RMfqR0z6A4nZ3aWsyAH7tvvgrA"
param1 = "H5QdNZW2nBZwsEzg6FlpSjIf3YyTAR9P"
param2 = 854
output = ""
rick = """
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
"""
roll = "".join(filter(str.isalpha, rick))
for c0, c1 in zip(param0, param1):
  if ord(c0) == ord(c1):
    output += roll[(ord(c0) + ord(c1) + param2) % len(roll)]
    if c0.isnumeric():
      output += c0
  elif ord(c0) > ord(c1):
    output += roll[(ord(c0) + param2) % len(roll)]
    if c0.isnumeric():
      output += c0
  else:
    output += roll[(ord(c1) + param2) % len(roll)]
    if c1.isnumeric():
      output += c1
  output = output[::-1]
output = output[0:32]
print(output)