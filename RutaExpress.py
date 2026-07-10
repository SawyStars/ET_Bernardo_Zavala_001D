recorridos = {
'R001': ['Santiago', 'Valparaíso', 120, 'normal', 'día', True],
'R002': ['Santiago', 'Concepción', 500, 'cama', 'noche', True],
'R003': ['La Serena', 'Coquimbo', 15, 'normal', 'día', False],
'R004': ['Temuco', 'Valdivia', 165, 'semi-cama', 'día', True],
'R005': ['Iquique', 'Arica', 310, 'cama', 'noche', False],
'R006': ['Santiago', 'Rancagua', 90, 'normal', 'día', True]
}

venta = {
'R001': [7990, 20],
'R002': [25990, 0],
'R003': [1990, 35],
'R004': [12990, 8],
'R005': [18990, 3],
'R006': [4990, 12],
}
while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Asientos por ciudad de origen")
    print("2. Búsqueda de recorridos por rango de precio")
    print("3. Actualizar precio de recorrido")
    print("4. Agregar recorrido")
    print("5. Eliminar recorrido")
    print("6. Salir")
    print("=====================================")
    op = int(input("Ingrese alguna opción: "))
    match op:
        case 1:
            Origen = input("Ingrese ciudad de origen a consultar: ")
            if Origen.isupper() or Origen.islower() or Origen.istitle():
                recorridos.get(Origen)
                print(recorridos.get(1, Origen))
                
        case 2:
            p_min = int(input("Ingrese precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))
            def Busqueda_Precio(p_min, p_max):
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    return
        case 3:
            Actualizar = input("Ingrese codigo del recorrido: ")
            venta.update()
            repetir = input("Desa actualizar otro precio (s/n)? :")
        case 4:
            codigo = input("Ingrese el codigo del recorrido")
            if not codigo.isspace() and not codigo.isalpha() == 0 and not codigo != recorridos.keys():
                recorridos.fromkeys(codigo)
                Nuev_Origen = input("Ingrese origen: ")
                if  Nuev_Origen.isspace() and  Nuev_Origen.isalpha() == 0 and  Nuev_Origen != recorridos.keys():
                    recorridos.fromkeys(codigo, Nuev_Origen)
                    Nuev_Destino = input("Ingrese Destino: ")
                    if  Nuev_Destino.isspace() and  Nuev_Destino.isalpha() == 0:
                        recorridos.fromkeys(codigo, Nuev_Destino)
                        Distancia = int(input("Ingrese Distancia (km): "))
                        if Distancia > 0:
                            recorridos.fromkeys(codigo, Distancia)
                            T_DeBus = input("Ingrese tipo de bus (normal/semi-cama/cama): ")
                            if T_DeBus.isupper() or T_DeBus.islower() or T_DeBus.istitle():
                                recorridos.fromkeys(codigo, T_DeBus)
                                Servicio = input("Ingrese servicio (Día/Noche): ")
                                if Servicio.isupper() or Servicio.islower() or Servicio.istitle():
                                    recorridos.fromkeys(codigo, Servicio)
                                    WiFi = input("¿Tiene WiFi (S/N): ")
                                    if WiFi.isupper() or WiFi.islower() or WiFi.istitle() and WiFi == "Si" or WiFi == "s" or WiFi == "No" or WiFi == "n":
                                        Nuev_Precio = int(input("Ingrese Precio: "))
                                        if Nuev_Precio > 0:
                                            Asientos = int(input("Ingrese asientos: "))
                                            if Asientos > 0:
                                                print("Recorrido Agregado.")
        case 5:
            recorridos.pop()
            venta.pop()
        case 6:
            print("Programa Finalizado")
            break
        case _:
            print("Eliga una opcion correcta.")