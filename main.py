# Board initalisiert ( 0 = leer )

board = [
    [0,0,0,0,0,0,0,0,3],
    [0,0,0,0,0,0,7,5,0],
    [0,5,0,4,8,0,0,0,0],
    [0,0,4,0,0,9,0,0,0],
    [1,0,0,0,6,7,0,0,2],
    [0,6,0,0,0,0,0,8,0],
    [0,3,0,2,0,0,0,4,0],
    [0,4,0,1,0,0,0,0,5],
    [8,0,0,0,0,5,6,0,0]
]

# Lösen (rekursiv, backtracing)

def solve(bo):
    
    # rekursiver Startpunkt, Programm startet immer wieder hier
    
    find = find_empty(bo) # Findet nahegelgenen leere Box
    if not find:
        return True # Endpunkt des rekursiven Aufrufes
    else: 
        row, col = find # row, col der leeren Box
        
    for i in range(1,10): # Zählt von 1 - 9 und probiert die Werte aus. 
        if valid(bo, i, (row,col)): # Ist die Eingabe möglich wenn ja:
            bo[row][col] = i # Schreibt die Zahl hinein
            if solve(bo): # Startet die Solve Methode von neu
                return True
            bo[row][col] = 0
    return False

# Checken ob die Eingabe valide ist

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # Geht durch jede Column durch, schaut ob = num. Gibt es die Nummer in der Reihe schon, nicht aktuelle Box
            return False
    
    # Check col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: # Geht durch jede Reihe durch, schaut ob = num. Gibt es die Nummer in der Spalte schon, nicht aktuelle Box
            return False
    
    # Check box
    box_x = pos[1] // 3 # 00 01 02 \n 10 11 12 ... Ergebnis = 0, 1 oder 2
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y*3 +3): # box_y * 3 = Startindex, box_y * 3 + 3 = EndIndex, box_y=0..2, Index=0..9
        for j in range(box_x * 3, box_x*3 +3):
            if bo[i][j] == num and (i,j) != pos:
                return False
            
    return True # Nummer noch nirgends geschrieben

# Board in Konsole ausgeben

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -") # Unterteilung horizontal
            
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="") # Unterteilung vertikal, kein \n am Ende
                
            if j == 8:
                print(bo[i][j]) # Zahlen einfügen am Ende
            else:
                print(str(bo[i][j]) + " ", end="") # Zahlen einfügen vor dem Ende
                
# Leere Spots finden
            
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


print_board(board)
solve(board)
print('\n')
print_board(board)