STRING = "AAAACCCGGT"
output = ""

# complememt part
for character in STRING:
    if character == "C":
        output += "G"
    elif character == "G":
        output += "C"
    elif character == "A":
        output += "T"
    elif character == "T":
        output += "A"

# reversing part
output = output[::-1]

print(output)
