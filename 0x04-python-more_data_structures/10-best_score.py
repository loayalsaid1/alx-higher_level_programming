#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or a_dictionary == {}:
        return None

    best_score = 0
    student = None

    for k, v in a_dictionary.items():
        if v > best_score:
            student = k
            best_score = v
    return student
