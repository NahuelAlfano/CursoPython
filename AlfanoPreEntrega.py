menu_messages = {
    "add_product_prompt": "\n¿Desea agregar un producto? (SI para agregar, NO para salir): ",
    "product_name_prompt": "¿Qué producto desea agregar? ",
    "product_weight_prompt": "Ingrese en kg. la cantidad: ",
    "product_price_prompt": "Ingrese el precio: ",
    "invalid_number": "Debe ingresar un número válido.",
    "non_positive_number": "El valor ingresado debe ser mayor a 0.",
    "product_added": "Producto agregado: {nombre}, cantidad={cantidad}kg, precio=${precio}",
    "no_products": "No hay productos en la lista."
}

program_messages = {
    'options': "Seleccione una opción (1-3): ",
    'success_add': "Productos agregados con éxito:",
    'success_exit': "Saliendo del programa...",
    'product_mod_option': "\nSi desea ver la lista de productos, seleccione la opción 2 en el menú."
}

products_list = []


# Funciones principales
def mostrar_menu():
    print('Menú de gestión de productos\n')
    print('Opción 1: Agregar productos')
    print('Opción 2: Listado completo de productos')
    print('Opción 3: Modificar producto')
    print('Opción 4: Salir')


def obtener_opcion_valida(prompt, opciones_validas):
    opcion = input(prompt).upper()
    while opcion not in opciones_validas:
        opcion = input(prompt).upper()
    return opcion


def valid_number_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(menu_messages["non_positive_number"])
            else:
                return value
        except ValueError:
            print(menu_messages["invalid_number"])


def agregar_productos():
    new_products = []
    while obtener_opcion_valida(menu_messages['add_product_prompt'], ["SI", "NO"]) == "SI":
        name = input(menu_messages['product_name_prompt'])
        weight = valid_number_input(menu_messages['product_weight_prompt'])
        price = valid_number_input(menu_messages['product_price_prompt'])
        new_prod = {"nombre": name, "cantidad": weight, "precio": price}
        new_products.append(new_prod)
        print(menu_messages['product_added'].format(nombre=name, cantidad=weight, precio=price))
    return new_products


def listar_productos():
    if products_list:
        print("\nListado de productos:")
        for producto in products_list:
            print(menu_messages['product_added'].format(
                nombre=producto['nombre'],
                cantidad=producto['cantidad'],
                precio=producto['precio']
            ))
    else:
        print(menu_messages["no_products"])

def modificar_productos():
    if products_list:
      for i, product in enumerate(products_list):
        print(f"{i+1}: {product['nombre']} - {product['cantidad']}kg - ${product['precio']}")
      try:
        selected_product = int(input("Seleccione el número del producto que desea modificar: ")) - 1
        if selected_product < 0 or selected_product >= len(products_list):
          print("El número ingresado no corresponde a un producto en la lista.")
        else: 
          new_name = input("Ingrese el nuevo nombre del producto: ")
          new_weight = valid_number_input("Ingrese la nueva cantidad en kg: ")
          new_price = valid_number_input("Ingrese el nuevo precio: ")
          products_list[selected_product] = {"nombre": new_name, "cantidad": new_weight, "precio": new_price}
          print("Producto modificado con éxito.")
      except ValueError:
        print("Debe ingresar un número válido.")
    else:
        print(menu_messages["no_products"])


# Programa principal
while True:
    mostrar_menu()
    opcion = obtener_opcion_valida(program_messages['options'], ["1", "2", "3", "4", "NO"])

    if opcion == "1":
        agregados = agregar_productos()
        if agregados:
            print(program_messages['success_add'])
            products_list += agregados
            print(program_messages['product_mod_option'])
        else:
            print("\nNo se agregó ningún producto.")

    elif opcion == "2":
        listar_productos()
    
    elif opcion == "3":
        modificar_productos()

    elif opcion in ["4", "NO"]:
        print(program_messages['success_exit'])
        break

    if obtener_opcion_valida("¿Desea continuar en el menú? (SI para continuar, NO para salir): ", ["SI", "NO"]) == "NO":
        print("\nGracias por usar el programa.")
        break
