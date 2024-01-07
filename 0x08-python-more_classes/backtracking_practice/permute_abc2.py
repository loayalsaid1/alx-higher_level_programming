"""
    Try the permutations on abc that it written in c++ in this video
https://youtu.be/VPtd_jZoomA



    the second version of permute_abc, but with adding constrains

    second approach
"""

def permute_abc(length, chars, solution, i=0):
    """

        MISSING CHECK FOR OUT OF RANGE INDEX 
        WHEN USER WANTS MORE THAT 25 (LEN OF ALPHABIT)

    """
    if i == length:
        solutions.append(solution)
        return

    for x in range(chars):
        if i == 0 or solution[i-1] != alphabit[x]:
            permute_abc(length, chars, solution+list(alphabit[x]), i+1)

if __name__ == "__main__":
    alphabit = [chr(x) for x in range(65, 91)]
    solutions = []
    permute_abc(3, 2, [])
    for x in solutions:
        print(x)
