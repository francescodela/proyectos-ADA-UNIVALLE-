
# usé casi la misma estructura que el ejer 1 

import csv

def funcionMergetSort(productos):
    if len(productos) <= 1:
        return productos

    divMedio = len(productos) // 2
    izquierda = funcionMergetSort(productos[:divMedio])
    derecha = funcionMergetSort(productos[divMedio:])

    return merge(izquierda, derecha)


def merge(izquierda, derecha):
    resultado = []
    rec_ind_izq_i  =  0
    rec_ind_der_J = 0

    while rec_ind_izq_i < len(izquierda) and rec_ind_der_J < len(derecha):
       
        if izquierda[rec_ind_izq_i]["calificacion"] > derecha[rec_ind_der_J] ["calificacion" ]:
            resultado.append(izquierda[rec_ind_izq_i])
            rec_ind_izq_i += 1

        elif izquierda[rec_ind_izq_i]["calificacion"] < derecha  [rec_ind_der_J]["calificacion"]:
            resultado.append(derecha[rec_ind_der_J])
            rec_ind_der_J += 1

        else:
            

            if izquierda  [rec_ind_izq_i]  ["precio"] <= derecha[rec_ind_der_J]["precio"]:
                resultado.append  (izquierda[rec_ind_izq_i])
                rec_ind_izq_i += 1

            else:

                resultado.append(derecha[rec_ind_der_J])
                rec_ind_der_J += 1

    resultado.extend(izquierda[rec_ind_izq_i:])

    resultado.extend(derecha[rec_ind_der_J:])

    return resultado



def cvsAnalisis(nombre_archivo):
    productos = []

    with open(nombre_archivo, newline='', encoding='utf-8') as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            productos.append({
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "precio": float(row["precio"]),
                "calificacion": int(row["calificacion"]),
                "stock": int(row["stock"])
            })
    return productos



documentoDatos = "ejer 2\productos.csv"
productos = cvsAnalisis(documentoDatos)



ordenados = funcionMergetSort(productos)




with open("productosYAordenados.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["id", "nombre", "precio", "calificacion", "stock"]
    escribie = csv.DictWriter(f, fieldnames=campos)
    escribie.writeheader()
    escribie.writerows(ordenados)

print("\n Archivo csv hecho correctamente con todos los productos ordenados")