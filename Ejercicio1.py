
print("Bienvenido a La biblioteca digital ReadCloud")
def main():

    libros = {
        'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
        'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
        'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
        'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
        'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
        'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False]
    }


    prestamos = {
        'L001': [500, 4],
        'L002': [700, 0],
        'L003': [300, 10],
        'L004': [400, 2],
        'L005': [600, 1],
        'L006': [350, 6]
    }

    
    while True:
        print("MENÚ PRINCIPAL =")
        print("1. Copias por género")
        print("2. Búsqueda de libros por rango de multa")
        print("3. Actualizar multa de libro")
        print("4. Agregar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        
        opcion = leer_opcion()
        
        if opcion == 1:
            genero_buscar = input("Ingrese el nombre del género literario: ")
            copias_genero(genero_buscar, libros, prestamos)
            
        elif opcion == 2:
            pedir_rango = True
            while pedir_rango:
                try:
                    minimo_multa = int(input("Ingrese el valor mínimo de la multa: "))
                    maximo_multa = int(input("Ingrese el valor máximo de la multa: "))
                    
                    if minimo_multa >= 0 and maximo_multa >= 0 and minimo_multa <= maximo_multa:
                        pedir_rango = False
                    else:
                        print("Error: Los valores deben ser mayores o iguales a cero, y el mínimo no puede superar al máximo.")
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            busqueda_multa(minimo_multa, maximo_multa, libros, prestamos)
            
        elif opcion == 3:
            actualizar_mas = True
            while actualizar_mas:
                codigo_libro = input("Ingrese el código del libro: ").upper()
                
                try:
                    nueva_multa = int(input("Ingrese el nuevo valor de multa (entero positivo): "))
                    if nueva_multa > 0:
                        exito = actualizar_multa(codigo_libro, nueva_multa, prestamos)
                        if exito:
                            print("Multa actualizada")
                        else:
                            print("El código no existe")
                    else:
                        print("La multa debe ser un entero mayor que cero.")
                except ValueError:
                    print("Error: El valor de la multa debe ser un número entero.")
                
                respuesta = input("\n¿Desea actualizar otra multa (si/no)?: ").lower()
                while respuesta != 'si' and respuesta != 'no':
                    respuesta = input("Por favor ingrese 'si' o 'no': ").lower()
                
                if respuesta == 'n':
                    actualizar_mas = False
                    
        elif opcion == 4:
            print("INGRESO DE NUEVO LIBRO")
            codigo = input("Código: ").upper()
            titulo = input("Título: ")
            autor = input("Autor: ")
            genero = input("Género: ")
            ano_str = input("Año de publicación: ")
            editorial = input("Editorial: ")
            novedad = input("¿Es novedad editorial? (si/no): ").lower()
            multa_str = input("Precio multa por día: ")
            copias_str = input("Copias disponibles: ")
            

            if not validar_codigo(codigo, libros):
                print("Error: El código no puede estar vacío, contener solo espacios o ya existir.")
            elif not validar_texto(titulo):
                print("Error: El título no puede estar vacío ni contener solo espacios.")
            elif not validar_texto(autor):
                print("Error: El autor no puede estar vacío ni contener solo espacios.")
            elif not validar_texto(genero):
                print("Error: El género no puede estar vacío ni contener solo espacios.")
            elif not validar_ano(ano_str):
                print("Error: El año debe ser un número entero mayor que cero.")
            elif not validar_texto(editorial):
                print("Error: La editorial no puede estar vacía ni contener solo espacios.")
            elif not validar_novedad(novedad):
                print("Error: Debe responder 'si' o 'no' para la novedad.")
            elif not validar_precio_multa(multa_str):
                print("Error: El precio de la multa debe ser un número entero mayor que cero.")
            elif not validar_copias(copias_str):
                print("Error: Las copias disponibles deben ser un número entero mayor o igual a cero.")
            else:

                ano_int = int(ano_str)
                multa_int = int(multa_str)
                copias_int = int(copias_str)
                
                if novedad == 'si':
                    novedad_bool = True
                else:
                    novedad_bool = False
                    
                resultado = agregar_libro(codigo, titulo, autor, genero, ano_int, editorial, novedad_bool, multa_int, copias_int, libros, prestamos)
                if resultado:
                    print("Libro agregado")
                else:
                    print("El código ya existe")
                    
        elif opcion == 5:
            codigo_eliminar = input("Ingrese el código del libro que desea eliminar: ").upper()
            exito_eliminar = eliminar_libro(codigo_eliminar, libros, prestamos)
            if exito_eliminar:
                print("Operación exitosa: El libro ha sido eliminado de ambos registros.")
            else:
                print("Error: El código ingresado no existe en el sistema.")
                
        elif opcion == 6:
            print("Saliendo del sistema... ¡Hasta luego!")


def leer_opcion():
    while True:
        try:
            opc = int(input("Seleccione una opción: "))
            if opc >= 1 and opc <= 6:
                return opc
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")



def copias_genero(genero, dic_libros, dic_prestamos):
    total_copias = 0
    genero_buscado = genero.lower()
    
  
    for codigo in dic_libros:
        datos_libro = dic_libros[codigo]
        genero_libro = datos_libro[2].lower() 
        
        if genero_libro == genero_buscado:
            if codigo in dic_prestamos:
                copias = dic_prestamos[codigo][1] 
                total_copias = total_copias + copias
                
    print(f"Total de copias disponibles para el género '{genero}': {total_copias}")


def busqueda_multa(multa_minima, multa_maxima, dic_libros, dic_prestamos):
    lista_resultados = []
    
    for codigo in dic_prestamos:
        datos_prestam = dic_prestamos[codigo]
        multa = datos_prestam[0]
        copias = datos_prestam[1]
        
        if multa >= multa_minima and multa <= multa_maxima and copias > 0:
            if codigo in dic_libros:
                titulo = dic_libros[codigo][0] 
                cadena = f"{titulo}{codigo}"
                lista_resultados.append(cadena)
                
    if len(lista_resultados) == 0:
        print("No hay libros en ese rango de multa.")
    else:

        lista_resultados.sort()
        print("Libros encontrados en el rango")
        for item in lista_resultados:
            print(item)



def buscar_codigo(codigo, dic_prestamos):
    cod_buscar = codigo.upper()
    for cod in dic_prestamos:
        if cod.upper() == cod_buscar:
            return True
    return False

def actualizar_multa(codigo, nueva_multa, dic_prestamos):

    existe = buscar_codigo(codigo, dic_prestamos)
    if existe:
        cod_correcto = codigo.upper()

        dic_prestamos[cod_correcto][0] = nueva_multa
        return True
    return False


def validar_codigo(codigo, dic_libros):
    if codigo.strip() == "" or codigo in dic_libros:
        return False
    return True

def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True

def validar_ano(ano_str):
    try:
        valor = int(ano_str)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False

def validar_novedad(nov_str):
    if nov_str == 's' or nov_str == 'n':
        return True
    return False

def validar_precio_multa(multa_str):
    try:
        valor = int(multa_str)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False

def validar_copias(copias_str):
    try:
        valor = int(copias_str)
        if valor >= 0:
            return True
        return False
    except ValueError:
        return False

def agregar_libro(codigo, titulo, autor, genero, ano, editorial, es_novedad, precio_multa, copias_disponibles, dic_libros, dic_prestamos):
    if codigo in dic_libros:
        return False
    

    dic_libros[codigo] = [titulo, autor, genero, ano, editorial, es_novedad]
  
    dic_prestamos[codigo] = [precio_multa, copias_disponibles]
    return True

def eliminar_libro(codigo, dic_libros, dic_prestamos):
    if codigo in dic_libros and codigo in dic_prestamos:
        del dic_libros[codigo]
        del dic_prestamos[codigo]
        return True
    return False


main()