#Capitulo 1 Conociendo Python

"""En una playa de estacionamiento cobran
    
    $. 2.00 por hora o fracción los días lunes, Martes y Miércoles, 
    $. 2.50. los días jueves y viernes, 
    $. 3.00 los días sábado y Domingo. 
    
    Se considera fracción de hora cuando haya pasado de 5 minutos. 
    
Diseñe un programa que determine cuánto debe pagar un cliente por su estacionamiento en un solo día de la semana. Si el tiempo ingresado es incorrecto imprima un mensaje de error."""

#Est funcion permite calcular el valor del parqueo dependiendo del dia de la semana y el tiempo que duro la persona. 

def parking_cost(parked_hours, parked_minutes, week_day):
    valid_days_week = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    
    #Verificar si el dia de la semana es valido en el vector establecido. No importa si el usuario lo escribe en mayuscula o minuscula ya que, con l afunncion lower se convierte a minuscula
    if week_day.lower() not in valid_days_week:
        return "Debe ingresar un dia a la semana válido"

    #calcula el tiempo total en minutes
    total_time_minutes = parked_hours * 60 + parked_minutes 

    #Se crea un diccionario con las tarifas de cada día de la semana
    tarifas = {"lunes": 2.00, 
               "martes": 2.00, 
               "miercoles": 2.00, 
               "jueves": 2.50,
               "viernes": 2.50,
               "sabado": 3.00,
               "domingo": 3.00}
    
    #Se  utiliza el método get() para obtener el valor asociado con la clave y si no encuentra el dia de la semana  el valor predeterminado será None.
    tarifa = tarifas.get(week_day.lower(), None)

    if tarifa is None:
        return "Error en el día de la semana"
    
    fraction_minute = 5
    
    if parked_minutes > fraction_minute:
        parked_hours += 1
        parked_minutes = 0

    total_hours = parked_hours + parked_minutes / 60

    costo_total = tarifa * total_hours
    return costo_total
    

#S piden los datos al usuario
days_weekday = input("Ingrese el dia de la semana: ")
parked_hours = int(input("Ingrese las horas estacionadas: "))
parked_minutes = int(input("Ingrese los minutos estacionados: "))

final_parking_cost = parking_cost(parked_hours, parked_minutes, days_weekday)

if type(final_parking_cost) == str:
    print(final_parking_cost)
else:
    print(f"Costo de estacionamiento que debe pagar es: ${final_parking_cost:.2f}")