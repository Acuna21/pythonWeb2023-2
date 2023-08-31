"""PARCIAL: SARA ACUÑA BENAVIDES --->
Dado un conjunto de puntos en un plano cartesiano, se te pide encontrar los dos puntos más cercanos entre sí. 
Implementa una función llamada pares_cercanos que tome una lista de coordenadas (puntos en el plano) y devuelva las coordenadas de los dos puntos más cercanos junto con su distancia. 

Utiliza el algoritmo "Divide y Vencerás" para resolver este problema de manera eficiente, este ejercicio deberá usar Decoradores, como args y kwargs
.
"""
import math  

# Para medir el tiempo de ejecución de una función
def calcular_tiempo(func):
    import time  #para asi poder medir el tiempo 
    def wrapper(*args, **kwargs):
        inicio = time.time()  
        resultado = func(*args, **kwargs)  # Ejecutamos la función
        
         # Tomamos el tiempo al final de la función
        fin = time.time() 
        print(f"El tiempo final de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado  # Devolvemos el resultado de la función
    return wrapper

# Para encontrar la distancia entre dos puntos
def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función principal que encuentra los dos puntos más cercanos en la lista de los puntos que se va a presentar
@calcular_tiempo  # Aplicamos el decorador para medir el tiempo de ejecución
def pares_cercanos(puntos):
    puntos_ordenados = sorted(puntos)  # Ordenamos los puntos por su coordenada x
    return encontrar_pares_cercanos(puntos_ordenados)


"Tener en cuenta --> Divide y vencerás para resolver el problema por partes y disnuir la complejidad un paso a la vez"
#  Aqui se evidencia divide y Vencerás para encontrar los pares más cercanos
def encontrar_pares_cercanos(puntos):
    tamaño = len(puntos)
    if tamaño <= 3:
        return min([(puntos[i], puntos[j], distancia(puntos[i], puntos[j]))
                    for i in range(tamaño) for j in range(i + 1, tamaño)],
                   key=lambda x: x[2])
    
    medio = tamaño // 2
    punto_medio = puntos[medio]
    izquierda = puntos[:medio]
    derecha = puntos[medio:]
    
    par_izquierda_encontrado = encontrar_pares_cercanos(izquierda)
    par_derecha_encontrado = encontrar_pares_cercanos(derecha)
    
    distancia_izquierda = distancia(*par_izquierda_encontrado[:2])
    distancia_derecha = distancia(*par_derecha_encontrado[:2])
    
    distancia_minima = min(distancia_izquierda, distancia_derecha)
    
    par_combinado_final = par_izquierda_encontrado if distancia_izquierda < distancia_derecha else par_derecha_encontrado
    
    strip = [punto for punto in puntos if abs(punto[0] - punto_medio[0]) < distancia_minima]
    
    strip_min = distancia_minima
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] < strip_min:
                distancia_obtenida = distancia(strip[i], strip[j])
                if distancia_obtenida < strip_min:
                    strip_min = distancia_obtenida
                    par_combinado_final = (strip[i], strip[j], distancia_obtenida)
    
    return par_combinado_final

# Puntos para probar el ejercicio
puntos_coordenada = [(14, 77),(84, 95),(21, 7), (23, 15), (8, 10), (34, 15),(45, 55),(4, 105),(31, 4),(22, 34),(15, 10),(14, 65),(11, 9),(42, 87),(92, 87)]
resultado = pares_cercanos(puntos_coordenada)

#RESULTADO FINAL
print("Los dos puntos más cercanos son: --->", resultado[:2])

print("Su distancia es: ---> {:.2f}".format(resultado[2]))
