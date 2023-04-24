# Importamos la libreria Time

import time

class HorarioTrabajo:
    def __init__(self, hora_inicio=9, hora_fin=17):
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        
    def es_hora_de_irse(self):
        hora_actual = time.localtime().tm_hour
        if hora_actual >= self.hora_fin:
            print("¡Es hora de ir a casa!")
        else:
            minutos_restantes = (self.hora_fin - hora_actual) * 60 - time.localtime().tm_min
            horas_restantes = minutos_restantes // 60
            minutos_restantes = minutos_restantes % 60
            print(f"Aún quedan {horas_restantes} horas y {minutos_restantes} minutos de trabajo.")

horario = HorarioTrabajo()
horario.es_hora_de_irse()
