#!/usr/bin/python3
def roman_to_int(roman_string):
    s = roman_string
    chars_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    if not isinstance(s, str):
        return 0

    result = 0

    for i in range(len(s)):
        if i + 1 < len(s) and chars_map[s[i]] < chars_map[s[i+1]]:
            result -= chars_map[s[i]]
        else:
            result += chars_map[s[i]]
    return result
