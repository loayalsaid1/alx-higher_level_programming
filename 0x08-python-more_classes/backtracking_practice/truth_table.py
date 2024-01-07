"""Try the truth table that it written in c++ in this video
https://youtu.be/VPtd_jZoomA
"""


def solve(n, i=0):
    if i == n:
        print(value)
        return

    value.append('0')
    solve(n, i+1)
    value.pop()
    
    value.append('1')
    solve(n, i+1)
    value.pop()



if __name__ == '__main__':
    value = []
    solve(3)
    print(value)
