# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores
# sean eventos. Permití consultar qué actividad hay en cierto día y hora.

agenda = {("lunes", "13:00"): "Visita al cliente",
          ("martes", "20:00"): "Cumpleaños",
          ("miércoles", "21:00"): "Noche de cine",
          ("jueves", "10:00"): "Cita con el cliente",
          ("viernes", "12:00"): "Cocinar para las visitas",
          ("sábado", "14:00"): "Sesión de yoga",
          ("domingo", "17:00"): "Ver el nuevo episodio de la serie"}

dia, hora = map(str,input("¿Qué día de la semana y hora quiere consultar? ").lower().split())
fecha = (dia, hora)

if fecha in agenda:
    print(agenda.get(fecha), '\n')
else:
    print("No encontrado.\n")
