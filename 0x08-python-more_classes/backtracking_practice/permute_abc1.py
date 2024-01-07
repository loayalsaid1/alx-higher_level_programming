"""
    Try the permutations on abc that it written in c++ in this video
https://youtu.be/VPtd_jZoomA



    the second version of permute_abc, but with adding constrains

    first approach
"""

def is_distinct(solution):
    length = len(solution)
    if length > 1:
        for index in range(length -1):
            if solution[index] == solution[index+1]:
                return False
    
    return True


def permute_abc(length, chars, solution, i=0):
    """

        MISSING CHECK FOR OUT OF RANGE INDEX 
        WHEN USER WANTS MORE THAT 25 (LEN OF ALPHABIT)

    """
    if i == length:
        if is_distinct(solution):
            solutions.append(solution)
        return

    for x in range(chars):
        permute_abc(length, chars, solution+list(alphabit[x]), i+1)

if __name__ == "__main__":
    alphabit = [chr(x) for x in range(65, 91)]
    solutions = []
    permute_abc(3, 2, [])
    for x in solutions:
        print(x)
