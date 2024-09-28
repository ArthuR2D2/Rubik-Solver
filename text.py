class Texts:
    def w():
        # Método para imprimir un mensaje de advertencia cuando la entrada del usuario es incorrecta
        print('Incorrecto, reintentar')

    def i():
        # Método para imprimir el mensaje de bienvenida y el menú principal del programa
        print('Seleccione acción: ')
        print('------------------')
        print('1. ---|---- N movimientos aleatorios')
        print('2. ---|---- Movimientos específicos')
        print('------------------')

    def i1():
        # Método para solicitar al usuario que ingrese la cantidad de movimientos para revolver el cubo
        print('Digite la cantidad de movimientos: ')

    def i2():
        # Método para solicitar al usuario que ingrese un movimiento específico o -1 para continuar con el cubo
        print('Digite el movimiento ó -1 para continuar con ese cubo: ')

    def movs():
        # Método para mostrar los movimientos disponibles que el usuario puede realizar en el cubo de Rubik
        movimientos = [
            "1.  ------Derecha (1)----",
            "2.  ------Derecha (2)----",
            "3.  ------Izquierda (1)--",
            "4.  ------Izquierda (2)--",
            "5.  ------Arriba (1)-----",
            "6.  ------Arriba (2)-----",
            "7.  ------Abajo (1)------",
            "8.  ------Abajo (2)------",
            "9.  ------Frente (1)-----",
            "10. ------Frente (2)-----",
            "11. ------Atrás (1)------",
            "12. ------Atrás (2)------"
        ]
        # Iterar sobre los movimientos disponibles e imprimir cada uno
        for movimiento in movimientos:
            print('Movimientos disponibles: ')
            print(movimiento)

    def s():
        # Método para solicitar al usuario que elija un método de resolución para resolver el cubo de Rubik
        print('Elige el metodo a usar: ')
        metodos = [
            "1.  ------BFS------------------",
            "2.  ------Best First Search----",
            "3.  ------A Star---------------",
            "4.  ------IDA Star-------------",
        ]
        # Iterar sobre los métodos disponibles e imprimir cada uno
        for metodo in metodos:
            print (metodo)

    def h():
        # Método para solicitar al usuario que elija una heurística para el método de resolución seleccionado
        print('Elige Heuristica a usar: ')
        heuristicas = [
            "1.  ------Manhattan-----------------------------------",
            "2.  ------Caras correctas-----------------------------",
            "3.  ------Bloques misma cara y adjuntos---------------",
            "4.  ------Promedio de Heuristicas---------------------",
        ]
        # Iterar sobre las heurísticas disponibles e imprimir cada una
        for heuristica in heuristicas:
            print (heuristica)

    def t(time):
        # Método para imprimir el tiempo transcurrido en segundos durante el proceso de resolución del cubo de Rubik
        print('Tiempo transcurrido: '+ str(time)+' segundos')
