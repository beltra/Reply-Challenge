import sched, time

class Solve:
    def __init__(self, matrix):
        self.giri = 0
        self.matrix = matrix
        self.hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        while self.checkEmpty():
            self.giri += 1
            for idxR in range(len(self.matrix)):
                r = self.matrix[idxR]
                for idxE in range(len(r)):
                    e = r[idxE]
                    possible = []
                    for i in self.hex:
                        #print(idxR, idxE, e, i)
                        if e == ' ' and not self.rowCheck(idxR, i) and not self.colCheck(idxE, i) and not self.checkSquare([idxR, idxE], i):
                            possible.append(i)
                    #print(possible)
                    if len(possible) == 1:
                        print(idxR, idxE, e, possible[0])
                        self.matrix[idxR][idxE] = possible[0]
            '''if not self.giri % 2000:
                print(self.giri)
                print(self.matrix)'''
        print(self.matrix)
        ris = ""
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                ris = ris + self.matrix[r][c]

        print(ris)
    
    def rowCheck(self, row, num):
        ls = self.matrix[row]
        for c in ls:
            if c == num:
                return True
        return False
        
    def colCheck(self, col, num):
        for r in self.matrix:
            if r[col] == num:
                return True
        return False
    
    def checkEmpty(self):
        for r in self.matrix:
            for c in r:
                if c == ' ':
                    return True
        return False
        
    def checkSquare(self, pos, num):
        init = [None, None]
        final = [None, None]

        init[0] = pos[0] - pos[0]%4
        init[1] = pos[1] - pos[1]%4
        final[0] = init[0] + 3
        final[1] = init[1] + 3

        for r in range(init[0], final[0]+1):
            for c in range(init[1], final[1]+1):
                if self.matrix[r][c] == num:
                    return True
        return False