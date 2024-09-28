import random

class RubikCube:
    def __init__(self):
        self.colors_l = ["W", "R", "G", "Y", "O", "B"]
        self.cubo = [[i]*8 for i in range(6)]
        self.caras = [0, 2396745, 4793490, 7190235, 9586980, 11983725]
    
    def calcular_caras(self, f1):
        for i in range(0, 6):
            if i == f1 or i == f1+3: 
                continue
            nuevo = self.cubo[i][0]*(2097152) + self.cubo[i][1]*(262144) + self.cubo[i][2]*(32768) + self.cubo[i][3]*(4096)
            nuevo += self.cubo[i][4]*(512) + self.cubo[i][5]*(64) + self.cubo[i][6]*(8) + self.cubo[i][7]
            self.caras[i] = nuevo
    
    def cambio(self, cara1, cara2, cara3, cara4, a1, a2, a3, a4, b1, b2, b3, b4, c1, c2, c3, c4):
        aux = self.cubo[cara1][a1]
        self.cubo[cara1][a1] = self.cubo[cara2][a2]
        self.cubo[cara2][a2] = self.cubo[cara3][a3]
        self.cubo[cara3][a3] = self.cubo[cara4][a4]
        self.cubo[cara4][a4] = aux

        aux = self.cubo[cara1][b1]
        self.cubo[cara1][b1] = self.cubo[cara2][b2]
        self.cubo[cara2][b2] = self.cubo[cara3][b3]
        self.cubo[cara3][b3] = self.cubo[cara4][b4]
        self.cubo[cara4][b4] = aux

        aux = self.cubo[cara1][c1]
        self.cubo[cara1][c1] = self.cubo[cara2][c2]
        self.cubo[cara2][c2] = self.cubo[cara3][c3]
        self.cubo[cara3][c3] = self.cubo[cara4][c4]
        self.cubo[cara4][c4] = aux
    
    def cambio_cara(self, cara, horario):
        if(horario):
            aux = self.cubo[cara][1]
            self.cubo[cara][1] = self.cubo[cara][3]
            self.cubo[cara][3] = self.cubo[cara][6]
            self.cubo[cara][6] = self.cubo[cara][4]
            self.cubo[cara][4] = aux
            aux = self.cubo[cara][0]
            self.cubo[cara][0] = self.cubo[cara][5]
            self.cubo[cara][5] = self.cubo[cara][7]
            self.cubo[cara][7] = self.cubo[cara][2]
            self.cubo[cara][2] = aux
        else:
            aux = self.cubo[cara][1]
            self.cubo[cara][1] = self.cubo[cara][4]
            self.cubo[cara][4] = self.cubo[cara][6]
            self.cubo[cara][6] = self.cubo[cara][3]
            self.cubo[cara][3] = aux
            aux = self.cubo[cara][0]
            self.cubo[cara][0] = self.cubo[cara][2]
            self.cubo[cara][2] = self.cubo[cara][7]
            self.cubo[cara][7] = self.cubo[cara][5]
            self.cubo[cara][5] = aux

    def R1(self):
        self.cambio(0, 4, 3, 1, 4, 4, 3, 4, 2, 2, 5, 2, 7, 7, 0, 7)
        self.cambio_cara(2, True)
    def R2(self):
        self.cambio(0, 1, 3, 4, 4, 4, 3, 4, 2, 2, 5, 2, 7, 7, 0, 7)
        self.cambio_cara(2, False)

    def L1(self):
        self.cambio(0, 1, 3, 4, 3, 3, 4, 3, 0, 0, 7, 0, 5, 5, 2, 5)
        self.cambio_cara(5, True)
    def L2(self):
        self.cambio(0, 4, 3, 1, 3, 3, 4, 3, 0, 0, 7, 0, 5, 5, 2, 5)
        self.cambio_cara(5, False)

    def U1(self):
        self.cambio(0, 2, 3, 5, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2)
        self.cambio_cara(1, True)
    def U2(self):
        self.cambio(0, 5, 3, 2, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2)
        self.cambio_cara(1, False)

    def D1(self):
        self.cambio(0, 5, 3, 2, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7)
        self.cambio_cara(4, True)
    def D2(self):
        self.cambio(0, 2, 3, 5, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7)
        self.cambio_cara(4, False)

    def F1(self):
        self.cambio(1, 5, 4, 2, 5, 7, 2, 0, 6, 4, 1, 3, 7, 2, 0, 5)
        self.cambio_cara(0, True)
    def F2(self):
        self.cambio(1, 2, 4, 5, 5, 0, 2, 7, 6, 3, 1, 4, 7, 5, 0, 2)
        self.cambio_cara(0, False)

    def B1(self):
        self.cambio(1, 2, 4, 5, 0, 2, 7, 5, 1, 4, 6, 3, 2, 7, 5, 0)
        self.cambio_cara(3, True)
    def B2(self):
        self.cambio(1, 5, 4, 2, 0, 5, 7, 2, 1, 3, 6, 4, 2, 0, 5, 7)
        self.cambio_cara(3, False)
    
    def shuffle_azar(self, N):
        for _ in range(N):
            x = random.randint(0, 11)
            self.movs(x)

    def shuffle(self, movimientos):
        for i in movimientos:
            self.movs(i)
        
    
    def movs(self, mov):
        if mov == 0:
            self.R1()
            self.calcular_caras(2)
            return "R1"
        elif mov == 1:
            self.R2()
            self.calcular_caras(2)
            return "R2"
        elif mov == 2:
            self.L1()
            self.calcular_caras(2)
            return "L1"
        elif mov == 3:
            self.L2()
            self.calcular_caras(2)
            return "L2"
        elif mov == 4:
            self.U1()
            self.calcular_caras(1)
            return "U1"
        elif mov == 5:
            self.U2()
            self.calcular_caras(1)
            return "U2"
        elif mov == 6:
            self.D1()
            self.calcular_caras(1)
            return "D1"
        elif mov == 7:
            self.D2()
            self.calcular_caras(1)
            return "D2"
        elif mov == 8:
            self.F1()
            self.calcular_caras(0)
            return "F1"
        elif mov == 9:
            self.F2()
            self.calcular_caras(0)
            return "F2"
        elif mov == 10:
            self.B1()
            self.calcular_caras(0)
            return "B1"
        else:
            self.B2()
            self.calcular_caras(0)
            return "B2"


    def print_faces(self):
        for j in range(2):
            i = j*3
            print("---------------------------------------------")
            print("CARA", i+1, "\t\tCARA", i+2, "\t\tCARA", i+3)
            print("---------------------------------------------")
            print(self.colors_l[self.cubo[i][0]], self.colors_l[self.cubo[i][1]], self.colors_l[self.cubo[i][2]], end="\t\t")
            print(self.colors_l[self.cubo[i+1][0]], self.colors_l[self.cubo[i+1][1]], self.colors_l[self.cubo[i+1][2]], end="\t\t")
            print(self.colors_l[self.cubo[i+2][0]], self.colors_l[self.cubo[i+2][1]], self.colors_l[self.cubo[i+2][2]])

            print(self.colors_l[self.cubo[i][3]], self.colors_l[i], self.colors_l[self.cubo[i][4]], end="\t\t")
            print(self.colors_l[self.cubo[i+1][3]], self.colors_l[i+1], self.colors_l[self.cubo[i+1][4]], end="\t\t")
            print(self.colors_l[self.cubo[i+2][3]], self.colors_l[i+2], self.colors_l[self.cubo[i+2][4]])

            print(self.colors_l[self.cubo[i][5]], self.colors_l[self.cubo[i][6]], self.colors_l[self.cubo[i][7]], end="\t\t")
            print(self.colors_l[self.cubo[i+1][5]], self.colors_l[self.cubo[i+1][6]], self.colors_l[self.cubo[i+1][7]], end="\t\t")
            print(self.colors_l[self.cubo[i+2][5]], self.colors_l[self.cubo[i+2][6]], self.colors_l[self.cubo[i+2][7]])
