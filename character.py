def first_unique_char(s):
    freq = {}

    # count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # find first unique
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i

    return -1


# -------- USER INPUT --------
s = input("Enter a string: ")

result = first_unique_char(s)

if result != -1:
    print(f"First non-repeating character index: {result}")
    print(f"Character: {s[result]}")
else:
    print("No non-repeating character found")