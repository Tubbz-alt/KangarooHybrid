#!/usr/bin/python

import sys


def comparatora(tame0, tame1, tame2, tame3, wild0, wild1, wild2, wild3):
    A, Ak, B, Bk = [], [], [], []
    with open('tame-0.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                A.append(a)
                Ak.append(b)
    with open('tame-1.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                A.append(a)
                Ak.append(b)
    with open('tame-2.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                A.append(a)
                Ak.append(b)
    with open('tame-3.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                A.append(a)
                Ak.append(b)
    with open('wild-0.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                B.append(a)
                Bk.append(b)
    with open('wild-1.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                B.append(a)
                Bk.append(b)
    with open('wild-2.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                B.append(a)
                Bk.append(b)
    with open('wild-3.txt', 'r') as f:
        for line in f:
            if len(line) == 130:
                L = line.split()
                a = int(L[0], 16)
                b = int(L[1], 16)
                B.append(a)
                Bk.append(b)
    result = list(set(A) & set(B))
    if len(result) > 0:
        sol_kt = A.index(result[0])
        sol_kw = B.index(result[0])
        d = Ak[sol_kt] - Bk[sol_kw]
        print('\n' + '\n' + 'SOLVED: ' + hex(d) + '\n')
        print('  Tips: 1NULY7DhzuNvSDtPkFzNo6oRTZQWBqXNE9 ' + '\n')
        file = open("BoooooooooooooooyahooooooooooooyaBs.txt", 'a')
        file.write("----------------------------------------\n")
        file.write(hex(Ak[sol_kt] - Bk[sol_kw]) + "\n")
        file.write("----------------------------------------\n")
        file.write("Tips: 1NULY7DhzuNvSDtPkFzNo6oRTZQWBqXNE9\n")
        file.close()
        sys.exit(0)
    else:
        sys.exit(1)

def main():

    s_tame0 = 'tame-0.txt'
    s_tame1 = 'tame-1.txt'
    s_tame2 = 'tame-2.txt'
    s_tame3 = 'tame-3.txt'
    s_wild0 = 'wild-0.txt'
    s_wild1 = 'wild-1.txt'
    s_wild2 = 'wild-2.txt'
    s_wild3 = 'wild-3.txt'
    #print('\n' + 'Compare:' + s_tame + s_wild + '\n')
    comparatora(s_tame0, s_tame1, s_tame2, s_tame3, s_wild0, s_wild1, s_wild2, s_wild3)
    

if __name__ == "__main__":
    main()
