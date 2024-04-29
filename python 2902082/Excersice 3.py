parcial1 = int(input("Ingrese calificacion de parcial 1"))
parcial2 = int(input("Ingrese calificacion de parcial 2"))
parcial3 = int(input("Ingrese calificacion de parcial 3"))

examenF = int(input("Ingrese calificacion de examen final"))

trabajoF = int(input("Ingrese calificacion de trabajo final"))

Avg = (parcial1 + parcial2 + parcial3) / 3

CalificacionF = (Avg * 0.55) + (examenF * 0.30) + (trabajoF * 0.15)

print("Su calificacion parcial es:",CalificacionF)