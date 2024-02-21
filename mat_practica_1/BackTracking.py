
# Autores: Adrián González (1636620), 
# Descripción: Este programa soluciona un crucigrama mediante backtracking y forward checking
# Fecha: 30/9/2023

print("PRÁCTICA 1: Crossword puzzle (backtracking) - (C)")
print("Autores de la práctica: Adrián González (1636620) y ...")



def CrosswordToMatrix():
    """
    Función que lee el txt del crucigrama y devuelve una matriz con sus atributos. 

    Returns:
        crucigrama: Matriz que simula el crucigrama
        len(crucigrama): y_size -> longitud vertical 
        len(crucigrama[0]): x_size -> longitud horizontal 
    """
    crucigrama = []
    with open("crossword_CB_v2.txt", "r") as txt:
        for linea in txt:
            crucigrama.append([int(-1) if casilla == '#' else int(0) for casilla in linea.split()])
    
    return crucigrama, len(crucigrama), len(crucigrama[0]) if crucigrama else 0


def CrosswordToMatrix(filename: str):
    """
    Función que lee el txt del crucigrama y devuelve una matriz con sus atributos. 

    Returns:
        crucigrama: Matriz que simula el crucigrama
        len(crucigrama): y_size -> longitud vertical 
        len(crucigrama[0]): x_size -> longitud horizontal 
    """
    crucigrama = []
    with open(filename, "r") as txt:
        for linea in txt:
            crucigrama.append([int(-1) if casilla == '#' else int(0) for casilla in linea.split()])
    
    return crucigrama, len(crucigrama), len(crucigrama[0]) if crucigrama else 0


def VocabToDictionary(filename: str):
    """
    Función que lee el txt del vocabulario y devuelve un diccionario con sus atributos. 

    Returns:
        vocab: Matriz que simula el crucigrama
        len(vocab): y_size -> longitud vertical 
    """
    vocab = {}
    with open("crossword_CB_v2.txt", "r") as txt:
        for linea in txt:
            vocab.append(linea)
    
    return vocab, len(vocab) if vocab else 0

def PrimerEspacioOrientado(crucigrama, x_size, y_size, x, y,  direccion):
    """
    Función que verifica si el espacio es el inicio y su orientación 

    Args:
        crucigrama: Matriz que simula el crucigrama
        x_size: Tamaño horizontal
        y_size: Tamaño vertical
        x: Posicion 'x' horizontal espacio inicial
        y: Posicion 'y' vertical espacio inicial
        direccion: Horizontal o vertical

    Returns:

    """
    if direccion == 'horizontal':
        if x == 0:
            return crucigrama[y][x+1] == 0
        elif x < x_size - 1:
            return crucigrama[y][x-1] == -1 and crucigrama[x][x+1] == 0
    elif direccion == 'vertical':
        if y == 0:
            return crucigrama[y+1][x] == 0
        elif y < y_size - 1:
            return crucigrama[y-1][x] == -1 and crucigrama[y+1][x] == 0
    return False



def calcEspacioVacio(crucigrama, x_size, y_size, x, y,  direccion):
    """
    Calcula la longitud vacía donde sea posible introducir palabras,
    tanto en vertical como en horizontal.

    Args:
        crucigrama: Matriz que simula el crucigrama
        x_size: Tamaño horizontal
        y_size: Tamaño vertical
        x: Posicion 'x' horizontal espacio inicial
        y: Posicion 'y' vertical espacio inicial
        direccion: Horizontal o vertical

    Returns:
        size: Longitud vacía

    """
    size = 0
    while True:
        if direccion == 'horizontal':
            if x >= x_size - 1 or crucigrama[y][x + 1] == -1:
                break
            x += 1
        elif direccion == 'vertical':
            if y >= y_size - 1 or crucigrama[y + 1][x] == -1:
                break
            y += 1
        size += 1
    return size


def CheckSolvedCrossword(crucigrama):
    """
    Comprueba que la matriz esté resuelta 
    Args:


    Returns:


    """




def BacktrackingSolucion(crucigrama, vocabulario, ):

    """
    Calcula la solución del crucigrama mediante backtracking
    Guardar la información de las variables en un struct
    Args:


    Returns:


    """


    return 0