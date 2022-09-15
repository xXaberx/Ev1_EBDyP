import random
import datetime

def registro_salas():
    global salas,eventos
    clave=max(list(salas.keys()),default=0)+1
    nom=input("Escriba el nombre de la sala")
    cupo=input("Seleccione el cupo")

    salas[clave] =nom,cupo,eventos    
    


def registro_evento():
    global eventos,lista,fecha_procesada,salas,evento
    cliente=int(input("Ingrese su clave de cliente"))
    if cliente in lista:        
        horarios = ["M", "V", "N"]
        fecha_actual=datetime.date.today()
        claves=max(list(eventos.keys()),default=0)+1
        evento=input("Ingrese el nombre del evento")
        turno=input("¿En qué turno desea tener su evento?: M/V/N")            
                    
        fecha=input("¿Qué fecha desea que sea su evento? (dd/mm/aaaa): \n")
        fecha_procesada = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        cant_dias = 2
        dia=fecha_actual.day
        dia_n=fecha_procesada.day
        print(dict(salas.items()))
        clave=input('Escribe el código de la sala que desee reservar')
        for clave in salas:
            if claves > 1:
                print('Fecha ocupada')
            else:
                if fecha_procesada < fecha_actual:
                    print("La fecha que usted pusó no se encuentra disponible")
                else:
                    if fecha_actual + datetime.timedelta(days=+cant_dias) <= fecha_procesada:
                        eventos[claves] = evento,turno,fecha_procesada                
                    else:
                        if fecha_actual + datetime.timedelta(days=+cant_dias) >= fecha_procesada: 
                            print("Se debe hacer una reservación al menos 2 días antes de su evento")                        


    
    
    
def registro_clientes():
    global diccionario,lista
    lista = [valor for valor in range(20000,100000)]
    random.shuffle(lista)
    n = 1
    for n in range(n):
        for x in lista:
            print("Ingrese su nombre")
            nombre = input()
            diccionario[x] = nombre
            break
lista=[]
diccionario={}  
salas={}
orden=""
eventos={}
fecha_procesada=""

turno=""

while True:
    print("Le damos la bienvenida, elija una de nuestras opciones de menú"
    """
    1) Registrar la reservación de una sala

    2) Editar el nombre del evento de una reservación ya hecha. ---

    3) Consultar las reservaciones existentes para una fecha específica.

    4) Registrar a un nuevo cliente --
    
    5) Registrar una sala con los siguientes datos --
    
    6) Salir --
    """)
    
    orden=input("¿Qué operación desea realizar?")
    
    if orden=="1":
        registro_evento()
        print(salas)


        
        
    if orden=="2":
        clave=int(input("Ingrese la clave del evento que desea modificar"))
        if clave in eventos:
            nuevo_nombre=input("¿Cómo desea llamar a su evento?")
            eventos[clave] = nuevo_nombre,turno,fecha_procesada
            print(f"La sala se ha modificado y su nombre ahora es: {salas[clave]}")
        else:
            print("Esta clave no esta registrada")
            

            
            
        
     

    if orden=="3":        
        fecha_consulta= input("Escribe la fecha que quieres consultar: ")
        fecha_consultaD=datetime.datetime.strptime(fecha_consulta, "%d/%m/%Y").date()
        for evento,turno in eventos.items():
            if fecha_consulta in eventos[1]:
                print(f"""
                    ***Reporte del dia {fecha_consultaD}
                    Nombre del evento {eventos[0]}
                    Turno del evento {eventos[1]}
                    Fecha del evento{eventos[2]}
                    
                    """)
            else:
                print("Fecha sin eventos")


            
            
        
    if orden == "4":
        registro_clientes()
        print(f"Los clientes registrados son {diccionario}")
        
    if orden == "5":
        
        registro_salas()
        print(salas)
      
        
        
    if orden == "6":
        break
        
        
    