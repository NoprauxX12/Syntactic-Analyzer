no_terminales = []
producciones = {}
cadena = " "

def parse_recursivo(lugar_actual, puntero=0):
    if lugar_actual == cadena:
        return True
    
    if (puntero > len(lugar_actual)-1 or puntero > len(cadena)-1):  
        return False
    
    if lugar_actual[puntero] == cadena[puntero]:
        return parse_recursivo(lugar_actual, puntero+1)
    elif lugar_actual[puntero] in no_terminales:
        if len(lugar_actual) > len(cadena):
            return False
        lugar_actual_temporal = lugar_actual
        puntero_temporal = puntero
        for produccion in producciones[lugar_actual[puntero]]:
            lugar_actual = lugar_actual.replace(lugar_actual[puntero], produccion, 1)
            if (parse_recursivo(lugar_actual, puntero) is True):
                return True
            else:
                lugar_actual = lugar_actual_temporal
                puntero = puntero_temporal
        return False        
    
    

if __name__ == '__main__':
     num = input()
     x = num.split(' ')
     n = int(x[0])
     m = int(x[1])
     k = int(x[2])
     no_terminal = input()
     no_terminales = no_terminal.split(' ')

     lista_cadena = []

     for _ in range(0, m):
         reglas = input()
         lista_reglas = reglas.split('-')
         if lista_reglas[0] not in producciones:
             producciones[lista_reglas[0]] = []
             producciones[lista_reglas[0]].append(lista_reglas[1])
         producciones[lista_reglas[0]].append(lista_reglas[1])
    
     for _ in range(0, k):
         cadena = input()
         lista_cadena.append(cadena)

     for i in range(len(lista_cadena)):
         cadena = lista_cadena[i]
         if parse_recursivo(no_terminales[0]):
             print("yes")
         else:
             print("no")

     
      