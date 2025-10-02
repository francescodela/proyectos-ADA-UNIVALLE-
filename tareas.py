

def funcionMergetSort(tareas):


    if len(tareas) <= 1:

        return tareas

    divisionMedio = len(tareas) // 2
    izquierda = funcionMergetSort(tareas[:divisionMedio])
    derecha = funcionMergetSort(tareas[divisionMedio:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    rec_ind_izq_i  =  0
    rec_ind_der_J = 0

    while rec_ind_izq_i  < len(izquierda) and rec_ind_der_J < len(derecha):
        
        if izquierda[rec_ind_izq_i ]["prioridad"] < derecha[rec_ind_der_J]["prioridad"]:
            resultado.append(izquierda[rec_ind_izq_i ])
            rec_ind_izq_i  += 1

        elif izquierda[rec_ind_izq_i ]["prioridad"] > derecha[rec_ind_der_J]["prioridad"]:
            resultado.append(derecha[rec_ind_der_J])
            rec_ind_der_J += 1

        else:
            
            if izquierda[rec_ind_izq_i ]["tiempo"] <= derecha[rec_ind_der_J]["tiempo"]:
                resultado.append(izquierda[rec_ind_izq_i ])
                rec_ind_izq_i  += 1
            else:

                resultado.append(derecha[rec_ind_der_J])
                rec_ind_der_J += 1


    resultado.extend(izquierda[rec_ind_izq_i :])
    resultado.extend(derecha[rec_ind_der_J:])

    return resultado



print("LISTA ANTIGUA DE LAS TAREAS:")  
tareas = [
        {"comer": "Tarea 1", "prioridad": 2, "tiempo": 5},
        {"hacer tareas ": "Tarea 2", "prioridad": 1, "tiempo": 3},
        {"ir al trabajo": "Tarea 3", "prioridad": 1, "tiempo": 7},
        {"comprar huevos ": "Tarea 4", "prioridad": 3, "tiempo": 2},
        {"estudiar ADA": "Tarea 5", "prioridad": 2, "tiempo": 1},
    ]


for valor  in tareas:
    print(valor )

ordenadas = funcionMergetSort(tareas)

print("\n LISTA ORDENADA DE TAREAS TENIENDO EN CUENTA LA PRIORIDAD Y TEMPO:")
for valor  in ordenadas:
    print(valor )
