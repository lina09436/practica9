import numpy as np
class DatosMetereologicos:


    DICT_COORDENADAS = {"N" : 0,
                        "NNE" : 22.5,
                        "NE" : 45,
                        "ENE" : 67.5,
                        "E" : 90,
                        "ESE" : 112.5,
                        "SE" : 135,
                        "SSE" : 157.5,
                        "S" : 180,
                        "SSW" : 202.5,
                        "SW" : 225,
                        "WSW" : 247.5,
                        "W" : 270,
                        "WNW" : 292.5,
                        "NW" : 315,
                        "NNW" : 337.5
    }

    


    def __init__(self, nombre_archivo: str) :
        self.nombre_archivo = nombre_archivo
        

    def procesar_datos(self):
        z = []
        x = []
        archivo = open(self.nombre_archivo, "r")
        archivo_lista = archivo.readlines()
        lista_temperatura = []
        lista_humedad = []
        lista_presion = []
        lista_velocidad = []
        lista_direccion = []
        
        for i in range(len(archivo_lista)):
            z = archivo_lista[i].split()
            # print(z)
            if "Temperatura:" in z:
                lista_temperatura.append(float(z[1]))
            elif "Humedad:" in z:
                lista_humedad.append(float(z[1]))
            elif "Presion:" in z:
                lista_presion.append(float(z[1]))    
            elif "Presion:" in z:
                lista_presion.append(float(z[1])) 
            elif "Viento:" in z:
                x = z[1].split(",")
                lista_velocidad.append(float(x[0]))
                lista_direccion.append(DatosMetereologicos.DICT_COORDENADAS[x[1]]) 
            else:
                continue 
        promedio_predominante = (sum(lista_direccion)/len(lista_direccion))
        # print(promedio_predominante)
        x = 361
        clave = ""
        clave = DatosMetereologicos.DICT_COORDENADAS['N']
        for j in DatosMetereologicos.DICT_COORDENADAS:
            dif = np.abs(promedio_predominante - DatosMetereologicos.DICT_COORDENADAS[j])
            if dif < x:
                x = dif
                clave = j 

         
            

           
            

        promedios = (f"Temperatura: {(sum(lista_temperatura)/len(lista_temperatura))} Humedad: {(sum(lista_humedad)/len(lista_humedad))} Presión: {(sum(lista_presion)/len(lista_presion))} Viento: {(sum(lista_velocidad)/len(lista_velocidad))} Dirección: {clave}")        
        print(promedios)



datos = DatosMetereologicos("datos.txt")          
datos.procesar_datos()  
