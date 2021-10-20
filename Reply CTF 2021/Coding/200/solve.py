class Puzzle:
    def __init__(self, pieces):
        self.out = []
        for r in range(200):
            self.out.append([])
            for c in range(200):
                self.out[r].append([])
        #print(self.out)
        
        # self.bordo = False
        # contAngolo = 0
        # for e in pieces:
        #     piece = self.retArray(e)
        #     contAngolo += 1
                       
        #     a, up, down, left, right = self.isBordo(piece, pieces)
        #     if a:
        #         if up + down + left + right == 2:
        #             if down and right:
        #                 self.out[0][0] = piece
        #                 pieces.remove(e)
        #                 print(contAngolo)
        #                 cont = 1
        #                 break
        #     if contAngolo % 500 == 0:
        #         print(contAngolo)
        
        cont = 1
        self.out[0][0] = ['38921', '11931', '64227', '142066', '']

        print("********* Angolo ***********")
        for r in range(0, 200, 1):
            #print(self.out[0])
            if r % 2 == 0:
                #print("pari")
                for c in range(0, 200):
                    piece1 = self.out[r][c]
                    for e in pieces:
                        piece2 = self.retArray(e)
                        if piece1[1] == piece2[0] and c == 199:
                            bordoDown = True
                            self.out[r+1][c] = piece2
                            pieces.remove(e)
                            cont += 1
                            break
                        if piece1[3] == piece2[2]:
                            bordoRight = True
                            self.out[r][c+1] = piece2
                            pieces.remove(e)
                            cont += 1
                            break
                print(cont)
                
            else:
                #print("dispari")
                for c in range(199, -1, -1):
                    piece1 = self.out[r][c]
                    for e in pieces:
                        piece2 = self.retArray(e)
                        if piece1[1] == piece2[0] and c == 0:
                            bordoDown = True
                            self.out[r+1][c] = piece2
                            pieces.remove(e)
                            cont += 1
                            break
                        elif piece1[2] == piece2[3]:
                            bordoLeft = True
                            self.out[r][c-1] = piece2
                            pieces.remove(e)
                            cont += 1
                            break
                print(cont)
            
        self.string = ""
        for r in self.out:
            for e in r:
                self.string += e[4]
        
        print(self.string)

    def retArray(self, piece):
        split = piece.split()
        if len(split) == 4:
            return [split[0], split[1], split[2], split[3], '']
        else:
            return split

    def isBordo(self, piece1, pieces):
        bordoUp = False
        bordoDown = False
        bordoLeft = False
        bordoRight = False
        for i in pieces:
            piece2 = self.retArray(i)
            if piece1[0] == piece2[1]:
                bordoUp = True
            if piece1[1] == piece2[0]:
                bordoDown = True
            if piece1[2] == piece2[3]:
                bordoLeft = True
            if piece1[3] == piece2[2]:
                bordoRight = True
        if bordoUp and bordoDown and bordoLeft and bordoRight:
            return False, False, False, False, False
        else:
            return True, bordoUp, bordoDown, bordoLeft, bordoRight

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    coords = [line[:-1] for line in lines]
    puzzle = Puzzle(coords)