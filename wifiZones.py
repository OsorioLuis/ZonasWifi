import re
from operator import itemgetter, truediv
import random
import math
#recreando los retos de mision tic

usuario = "51675"
contra = "57615"

print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
def try_numeros(valor, evaluador):
    try:
        if(valor == evaluador):
            return True
    except ValueError:
        return "Error, no digitaste un numero"

def captcha(user, password):
    #comprobacion de captcha sencillo
    try:
        if(user == True and password == True):
            valor1 = 675
            valor2 = 5-5+6+1
            result = 682
            print("Resuelve el siguiente captcha: ")
            valor_introducido = int(input(f"{valor1} + {valor2}: "))

            if(valor_introducido == result):
                return "Sesion iniciada"
            else:
                return "Error"
        return "Error"
    except ValueError:
        print("No dijitaste un numero")
        return "Error"

class reto2:
    def __init__(self):
        self.array = [] #inicia creando un array vacio para poder asignar self a los metodos
    
    def opcionFavorita(self, verificante):
        try:
            if(verificante == 1):
                self.array = [1,2,3,4,5]
                cambio = reto2()
                cambio.menu(self.array)
            else:
                opcion = int(input("Seleccione la opción favorita: "))
                if(opcion > 5):
                    return "Error"
                else:
                    adv1 = int(input("Soy una l invertida con columna torcida: "))
                    if(try_numeros(adv1, 7) == True):
                        adv2 = int(input("Soy el 5: "))
                        if(try_numeros(adv2, 5) == True):
                            arraycopy = [1,2,3,4,5]
                            
                            #las lineas a continuación se encargan de reordenar el arreglo según la opción elegida
                            temp = arraycopy[opcion-1]
                            arraycopy[0] = opcion
                            arraycopy[opcion-1] = 1

                            #llamamos al self.array para que tenga el valor del array desordenado segun la opcion elegida
                            self.array = arraycopy
                            cambio = reto2() #instanciamos objetos y hacemos que este imprima el nuevo menu
                            #desordenado para que el metodo menu que tiene el sorted reorganice el menu segun
                            #la opcion elegida
                            return cambio.menu(arraycopy)
                        else:
                            return "Error"
                    else:
                        return "Error"
        except ValueError:
            return "Error"

    def menu(self, arrays):
        self.array = arrays

        print("\n=============MENU=============")
        opciones = {"Cambiar contraseña" : self.array[0],
        "Ingresar coordenadas actuales": self.array[1],
        "Ubicar zona wifi mas cercana" : self.array[2],
        "Guardar archivo con ubicacion": self.array[3],
        "Actualizar registros de zonas wifi desde archivo": self.array[4],
        "Elegir opción de menu favorita" : 6,
        "Cerrar sesión" : 7}
        #este hace lo siguiente:
        '''menu_sort sera un diccionario que estará organizado por los items de opciones
        (siempre estará operando cada vez que se llame este metodo, por lo que cuando
        eligamos opcion preferida este menu se reordenara con los nuevos valores enviados por 
        el metodo opcionpreferida) con la forma itemgetter que reorganiza el diccionario según su valor'''
        menu_sort = dict(sorted(opciones.items(), key=itemgetter(1)))
        for key, value in menu_sort.items():
            menuopciones = "%s. %s" % (value, key)
            print(menuopciones)
        
class reto3():
    #atributos 
    lista = []
    conexiones = [[1.811, -75.280, 58],
                [1.919, -75.820, 1290],
                [1.875, -75.877, 110],
                [1.938, -75.764, 114]]
    radio = 6372.795477598

    informacion = {}

    #######################################  Metodos
    def cambiar_contrasena(contra):
        antigua = input("Digita la contraseña anterior: ")
        if(antigua == contra):
            confirma_antigua = input("Confirma tu contraseña: ")
            if(confirma_antigua == contra):
                nueva = input("Digita la nueva contrasena: ")
                contra = nueva
                #print(contra)
                print("Contraseña cambiada")
                
            else:
                print("Error")
                return 0
        else:
            print("Error")
            return 0
    #////////////////////////////////hacer retoques para condicionales///////////////////////////////
    def crea_matrices(): #en caso de digitar mal una coordenada devuelve 0
        
        for i in range(3): #numero de filas
            reto3.lista.append([])
            for j in range(2):
                coordenada = float(input("Digita la coordenada: "))
                if(coordenada <= 1.998 and coordenada >= 1.741):
                    print("Coordenada correcta")
                    reto3.lista[i].append(coordenada)
                elif(coordenada >= -75.950 and coordenada <= -75.132):
                    print("Coordenada correcta")
                    reto3.lista[i].append(coordenada)
                else:
                    return 0
                    
        print("Coordenadas registradas")
        #print(reto3.lista)
        return reto3.lista

    #/////////////////////////////////////////agregar promedios y determinar proximidad en sur, norte etc///////////////////////////////
    def actualiza_coordenada():
        coordenadas = reto3.lista
        copia = coordenadas.copy()
        for i in range(len(coordenadas)):
            print(f"Coordenada [latitud, longitud] {i+1}: {coordenadas[i]}")
        print(f"La coordenada {random.randrange(2)+1} está más al oriente")
        print(f"La coordenada {random.randrange(2)+1} está más al occidente")
        print("Presione 1,2 o 3 para actualizar la respectiva coordenada")
        try:
           res = int(input("Presiona 0 para regresar al menú: "))
        except ValueError:
            print("Error, no digitaste una opción correcta")
            return 0
        for i in range(len(coordenadas)):
            if(res == 0):
                break
            if(res == i+1):
                try:
                    for j in range(len(coordenadas[i])):
                        coordenada = float(input("Digita la coordenada: "))
                        if(coordenada <= 1.998 and coordenada >= 1.741):
                            print("Coordenada correcta")
                            coordenadas[i][j] = coordenada
                        elif(coordenada >= -75.950 and coordenada <= -75.132):
                            print("Coordenada correcta")
                            coordenadas[i][j] = coordenada
                        else:
                            #en caso de que una coordenda haya quedado mala también se hace una copia de seguridad y se guarda en el atributo 800iq
                            coordenadas.remove(coordenada)
                            reto3.lista = copia
                            return 0
                except ValueError:
                    print("Error, coordenada no valida")
                    return 0
    def reto4_coordenadas():
        coordenadas = reto3.lista
        for i in range(len(coordenadas)):
            print(f"coordenada [latitud, longitud] {i+1}: {coordenadas[i]}")
        try:
            eleccion = int(input("Por favor elija su ubicación actual (1,2,3) para calcular la distancia de los puntos de conexion: "))
            copia = coordenadas[eleccion-1]

            # atributos de las coordenadas wifi
            distancia = reto3.calculamenores(copia, reto3.conexiones)
            if (distancia != 1):
                print("Para llegar a la zona wifi debe dirigirse primero a occidente y luego al sur")
                tiempo_moto = distancia / 19.44
                tiempo_pie = distancia / 0.483
                print(f"Tiempo promedio para llegar en moto es de {round(tiempo_moto, 0)} minutos")
                print(f"Tiempo promedio para llegar a pie es de {round(tiempo_pie, 0)} minutos")
                try:
                    salida = int(input("Presione 0 para salir: "))
                    if(salida != 0):
                        print("Error, no digitaste cero")
                        return 1
                except:
                    print("Error")
            else:
                return 1
                
        except ValueError: 
            return 1

    def calculamenores(inicial, conexion):
        recive = conexion.copy()
        lista = []
        seleccion = [inicial[0], inicial[1]]
        temp = None
        num = 0
        cercana = []
        for j in range(2):
            lista.append([])
            for item in range(4):
                resta = recive[item][j] - seleccion[num]
                if(temp == None):
                    temp = resta
                if(resta < temp):
                    temp = resta
                    lat2 = recive[item][j]
                    cercana = recive[item]
            lista[j].append(temp)
            num += 1

        distancia = 2*reto3.radio*(math.asin(math.sqrt(((math.sin(lista[1][0]/2))**2)+(math.cos(seleccion[0]))*(math.cos(lat2))*((math.sin(lista[0][0]/2))**2))))
        print("Zona wifi cercanas con menos usuarios")
        for i in range(2):
            print(f"La zona wifi {i+1} ubicada en {cercana[0:2]} a {round(distancia, 0)} metros, tiene un promedio de {cercana[2]} usuarios")
        seleccion = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
        if (seleccion == True):
            return round(distancia, 0)
        else:
            return 1

            
    def guardararchivo():
        if(len(reto3.lista) == 0):
            return 1
        else:
            pass

def menu_inicial():
    inicio = reto2()
    return inicio.menu([1,2,3,4,5])

## lista de coordenadas [1.995, -75.951], 
##########################################################################

#########################################  sistema  ###################      
nombre_usuario = input("Digita tu nombre de usuario: ")
if(nombre_usuario == usuario):

    contrasena_usuario = input("Digita tu contraseña: ")
    valueuser = True #valor de confirmacion para la funcion captcha

    if(contrasena_usuario == contra):

        valuepass = True
        if(captcha(valueuser, valuepass) == "Sesion iniciada"):
            objetomenu = reto2()
            continuar = False
            if(continuar == False):
                menu_inicial()
            
            while True:
                
                try:
                    seleccion = int(input("\nElija una opción: "))
                    if(seleccion == 6):
                        objetomenu.opcionFavorita(None)
                        continuar = True
                    elif(seleccion == 1):
                        obj2 = reto3
                        if(obj2.cambiar_contrasena(contra) == 0): #verifica de una vez si hay error, caso contrario continua
                            break
                        else:
                            # funciona para imprimir el menu, siempre podemos elegir la opcion
                            # preferida cuando queramos pero no al contrario luego de haber escogido otra opciona antes
                            objetomenu.opcionFavorita(1)
                    elif (seleccion == 2):
                        matriz = reto3
                        if len(matriz.lista) > 0:
                            matriz.actualiza_coordenada()

                            menu_inicial()
                        else:
                            evaluador = matriz.crea_matrices()
                            if(evaluador == 0):
                                print("Error coordenada")
                                del evaluador
                                break
                            else:
                                menu_inicial()
                    elif (seleccion == 3):
                        # verifica si el objeto matriz existe, y como la opcion 2 no fue ejecutada
                        # pues simplemente matriz no existe
                        if('matriz' not in locals()):
                            print("Error sin registro de coordenadas")
                            break
                        else:
                            
                            if(matriz.reto4_coordenadas() == 1):
                                print("Error ubicación")
                                break
                            else:
                                menu_inicial()
                    elif (seleccion == 4):

                        reto5 = reto3
                        if(reto5.guardararchivo() == 1):
                            print("Error de aislamiento")
                            break
                        else:
                            break

                    elif (seleccion == 7):
                        print("Hasta pronto")
                        break
                    else:
                        print("Has escogido la opcion " + str(seleccion))
                        break
                except ValueError:
                    print("Error, no digitaste un numero")
                    break
    else:
        print("error")
else:
    print("Error")

