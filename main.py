from solver import RubikSolver, Heuristics
from text import Texts
import time

'''
Rubik's cube python proyect
Oscar Fabrizio de Alba
Jose Arturo Reza Quezada
'''
class Main:
    def __init__(self):
        # Inicialización de la clase Main
        # Se crea una instancia de RubikSolver para resolver el cubo de Rubik
        self.solver = RubikSolver()
    
    def menu(self):
        # Método para mostrar el menú principal y gestionar las acciones del usuario
        Texts.i()  # Muestra el mensaje de bienvenida
        while True:
            action = input()  # Espera la entrada del usuario
            if action == '1' or action == '2':  # Si la acción es válida
                self.action(action)  # Llama al método action con la acción seleccionada
                break
            Texts.w()  # Muestra un mensaje de advertencia si la entrada no es válida
        
    def action(self, action):
        # Método para manejar las acciones del usuario
        if action == '1':
            Texts.i1()  # Muestra el mensaje para ingresar el número de movimientos para revolver el cubo
            n = int(input())  # Lee el número de movimientos desde la entrada
            self.solver.revolver(True, n)  # Revuelve el cubo con el número de movimientos especificado
            self.solve()  # Llama al método solve para resolver el cubo después de revolverlo
        else:
            Texts.movs()  # Muestra el mensaje para realizar movimientos en el cubo
            
            while True:
                Texts.i2()  # Muestra el mensaje para ingresar un movimiento
                m = int(input())  # Lee el movimiento desde la entrada
                if m == -1:  # Si el usuario ingresa -1, termina el proceso de resolución
                    self.solve()  # Llama al método solve para resolver el cubo
                    break
                elif m >= 1 and m <= 12:  # Si el movimiento es válido
                    self.solver.make_move(m)  # Realiza el movimiento en el cubo
                else:
                    Texts.w()  # Muestra un mensaje de advertencia si el movimiento no es válido
    
    def solve(self):
        # Método para resolver el cubo de Rubik
        Texts.s()  # Muestra el mensaje para elegir un método de resolución
        while True:
            metodo = int(input())  # Lee el método de resolución desde la entrada
            if metodo > 0 and metodo <= 4:  # Si el método es válido
                break
            
        

        # Si el método no requiere heurística
        if metodo == 1:
            inicio = time.time()  # Guarda el tiempo de inicio
            self.solver.bfs()  # Resuelve el cubo utilizando Breadth-First Search
            fin = time.time()  # Guarda el tiempo de finalización
            Texts.t(fin - inicio)  # Muestra el tiempo transcurrido en la resolución del cubo

        # Si el método requiere heurística
        elif metodo in [2, 3, 4]:
            Texts.h()  # Muestra el mensaje para elegir una heurística
            while True:
                heuristica = int(input())  # Lee la heurística desde la entrada
                if heuristica > 0 and heuristica <= 4:  # Si la heurística es válida
                    break
                Texts.w()  # Muestra un mensaje de advertencia si la heurística no es válida
                
            heuristic_functions = {
                1: Heuristics.heu_1,
                2: Heuristics.heu_2,
                3: Heuristics.heu_3,
                4: Heuristics.heu_4
            }

            # Verificar si la heurística seleccionada es válida
            if heuristica in heuristic_functions:
                heuristic_function = heuristic_functions[heuristica]
                if metodo == 2:
                    inicio = time.time()
                    self.solver.best_first_search(heuristic_function)  # Resuelve el cubo utilizando Best First Search
                    fin = time.time()
                    Texts.t(fin - inicio)
                elif metodo == 3:
                    inicio = time.time()
                    self.solver.a_star(heuristic_function)  # Resuelve el cubo utilizando A*
                    fin = time.time()
                    Texts.t(fin - inicio)
                elif metodo == 4:
                    inicio = time.time()
                    self.solver.ida_star(heuristic_function)  # Resuelve el cubo utilizando IDA*
                    fin = time.time()
                    Texts.t(fin - inicio)
    
main = Main()  # Crea una instancia de la clase Main

main.menu()  # Ejecuta el método menu para iniciar el programa
