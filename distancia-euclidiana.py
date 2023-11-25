#Distancia Euclidiana
X = [float(input("Diga o X do primeiro ponto:  ")),float(input("Diga o X do segundo ponto:  "))]
Y = [float(input("Diga o Y do primeiro ponto:  ")),float(input("Diga o Y do segundo ponto:  "))]
def de(X,Y):
    calc = ((X[0] - X[1])**2 + (Y[0] - Y[1])**2)**(1/2)
    print("A Distância Euclidiana entre eles é: ",calc)
de(X,Y)