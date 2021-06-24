import matplotlib
import matplotlib.pyplot as plt

# DDA PARA EL CUADRADO
def DDA(x1, y1, x2, y2):
    fig = plt.figure(1).add_subplot(111)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    plt.xlim([x1-2,x2+2])
    plt.ylim([y1-2, y2+2])
    plt.title("Algoritmo DDA. \nCUADRADO")
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)
    #PARA Y1
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 = y1 + yInc
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA X2
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 = x1 + xInc
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA Y2
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x2), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 = y1 - yInc
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA EL ORIGEN X1
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x2), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x2 = x2 - xInc
        print("VALOR DE X:", x2, "VALOR DE Y:", y1)
    plt.grid()
    plt.show()

# DDA PARA EL RECTANGULO
def DDA1(x1, y1, x2, y2):
    fig = plt.figure(1).add_subplot(111)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    plt.xlim([x1-2,x2+2])
    plt.ylim([y1-2, y2+2])
    plt.title("Algoritmo DDA. \nRECTANGULO")
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)
    #PARA Y1
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 = y1 + yInc
        print("!VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA X2
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 = x1 + xInc
        print("&VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA Y2
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x2), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 = y1 - yInc
        print("+VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA EL ORIGEN X1
    for i in range(0, int(steps)):
        grafica= matplotlib.patches.Rectangle((round(x2), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x2 = x2 - xInc
        print("*VALOR DE X:", x2, "VALOR DE Y:", y1)
    plt.grid()
    plt.show()

# DDA PARA EL TRIANGULO
def DDA2(x1, y1, x2, y2):
    fig = plt.figure(1).add_subplot(111)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    plt.xlim([x1-2,x2+10])
    plt.ylim([y1-2, y2+4])
    plt.title("Algoritmo DDA.\nTRIANGULO")
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)
    #PARA Y1
    for i in range(0, int(steps+1)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 += xInc
        y1 += yInc
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA Y2
    for i in range(0, int(steps+1)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 -= 1
        x1 += 1
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #
    for i in range(0, int(steps+7)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 -= 1
        print("{VALOR DE X:", x1, "VALOR DE Y:", y1)
    plt.grid()
    plt.show()

# DDA PARA EL TRIANGULO RECTANGULO.
def DDA3(x1, y1, x2, y2):
    fig = plt.figure(1).add_subplot(111)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    plt.xlim([x1-2,x2+10])
    plt.ylim([y1-2, y2+4])
    plt.title("Algoritmo DDA.\nTRIANGULO RECTANGULO")
    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)
          
    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc,1)
    yInc = round(yInc,1)
    #PARA Y1
    for i in range(0, int(steps+1)):
        grafica= matplotlib.patches.Rectangle((round(x1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 += xInc
        y1 += yInc
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    #PARA Y2
    for i in range(0, int(steps+1)):
        grafica= matplotlib.patches.Rectangle((round(x2), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        y1 = y1 - yInc
        print("+VALOR DE X:", x1, "VALOR DE Y:", y1)
    #
    for i in range(0, int(steps+1)):
        grafica= matplotlib.patches.Rectangle((round(x1-1), round(y1)),1,1,linewidth=2,edgecolor='b', facecolor='none')
        fig.add_patch(grafica)
        x1 -= 1
        print("VALOR DE X:", x1, "VALOR DE Y:", y1)
    plt.grid()
    plt.show()

# BRESENHAMS PARA EL CUADRADO
def bre(x1, y1, x2, y2):
        fig = plt.figure(1).add_subplot(111)
        x = x1
        y = y1
        dx = abs (x2 -x1)
        dy = abs (y2 - y1)
        p = 2*dy - dx
        plt.xlim([x1-5,x2+5])
        plt.ylim([y1-5, y2+5])
        plt.title("Algoritmo Bresenhams\nCUADRADO")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print("#VALOR DE X:", x, "VALOR DE Y:", y)
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            if (dx < 0):
                x-=1
            else:
                x+= 1
                
            if (dy < 0):
                if (p<0):
                    p = p + 2 * dy
                    y-=1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if (p<0):
                    p = p + 2 * dy
                else: 
                    p= p + (2*dy) - (2*dx)
                    y+=1

        for i in range (y+1, x2):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            y+=1
            print("*VALOR DE X:", x, "VALOR DE Y:", y)

        for i in range (x2-x1,x):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            x-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        for i in range (y-y+2,x2):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            y-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        plt.grid()
        plt.show()

# BRESENHAMS PARA EL RECTANGULO
def bre1(x1, y1, x2, y2):
        fig = plt.figure(1).add_subplot(111)
        x = x1
        y = y1
        dx = abs (x2 -x1)
        dy = abs (y2 - y1)
        p = 2*dy - dx
        plt.xlim([x1-5,x2+5])
        plt.ylim([y1-5, y2+5])
        plt.title("Algoritmo Bresenhams\nRECTANGULO")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print("#VALOR DE X:", x, "VALOR DE Y:", y)
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            if (dx < 0):
                x-=1
            else:
                x+= 1
                
            if (dy < 0):
                if (p<0):
                    p = p + 2 * dy
                    y-=1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if (p<0):
                    p = p + 2 * dy
                else: 
                    p= p + (2*dy) - (2*dx)
                    y+=1

        for i in range (y+1, x2+4):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            y+=1
            print("*VALOR DE X:", x, "VALOR DE Y:", y)

        for i in range (x2-x1,x):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            x-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        for i in range (y-y+2,x2+4):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            y-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        plt.grid()
        plt.show()

# BRESENHAMS PARA EL TRIANGULO 
def bre2(x1, y1, x2, y2):
        fig = plt.figure(1).add_subplot(111)
        x = x1
        y = y1
        dx = abs (x2 -x1)
        dy = abs (y2 - y1)
        p = 2*dy - dx
        plt.xlim([x1-2,x2+10])
        plt.ylim([y1-2, y2+4])
        plt.title("Algoritmo Bresenhams\nTRIANGULO")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print("#VALOR DE X:", x, "VALOR DE Y:", y)
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            if (dx < 0):
                x-=1
            else:
                x+= 1
                
            if (dy < 0):
                if (p<0):
                    p = p + 2 * dy
                    y-=1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if (p<0):
                    p = p + 2 * dy
                else: 
                    p= p + (2*dy) - (2*dx)
                    y+=1

        for i in range (x, x2+7):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            x += 1
            y -= 1
            print("*VALOR DE X:", x, "VALOR DE Y:", y)
        for i in range (x,x2+20):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            x-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        plt.grid()
        plt.show()

# BRESENHAMS PARA EL TRIANGULO RECTANGULO
def bre3(x1, y1, x2, y2):
        fig = plt.figure(1).add_subplot(111)
        x = x1
        y = y1
        dx = abs (x2 -x1)
        dy = abs (y2 - y1)
        p = 2*dy - dx
        plt.xlim([x1-2,x2+10])
        plt.ylim([y1-2, y2+4])
        plt.title("Algoritmo Bresenhams\nTRIANGULO RECTANGULO")
        while (x <= x2):
            plt.plot(round(x), round(y))
            print("#VALOR DE X:", x, "VALOR DE Y:", y)
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            if (dx < 0):
                x-=1
            else:
                x+= 1
                
            if (dy < 0):
                if (p<0):
                    p = p + 2 * dy
                    y-=1
                else:
                    p = p + (2*dy) - (2*dx)
            else:
                if (p<0):
                    p = p + 2 * dy
                else: 
                    p= p + (2*dy) - (2*dx)
                    y+=1

        for i in range (x, x2+8):
            grafica= matplotlib.patches.Rectangle((x,y-1),1,1,linewidth=2,edgecolor='b', facecolor='none')
            fig.add_patch(grafica)
            y -= 1
            print("*VALOR DE X:", x, "VALOR DE Y:", y)
        for i in range (x,x2+13):
            grafica= matplotlib.patches.Rectangle((x,y),1,1,linewidth=2,edgecolor='r', facecolor='none')
            fig.add_patch(grafica)
            x-=1
            print("°VALOR DE X:", x, "VALOR DE Y:", y)

        plt.grid()
        plt.show()

def main():
    # SE SOLICITA O PIDE QUE SELECCIONES UN ALGORITMO
    tipo = int(
        input("ALGORITMOS..\n1.DDA \n2.Bresenhams \nSelecciona un algoritmo: "))
    # OPCION DDA
    if tipo == 1:
        print("******ALGORITMO DDA******")
        cuantos = int(input(
            "\nSelecciona uno.\n1.Cuadrado\n2.Rectangulo\n3.Triangulo \n4.triangulo rectangulo\nSelecciona la figura con la que quieres trabajar: "))
        if cuantos == 1:
            print("CUADRADO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            DDA(x1, y1, x2, y2)
        if cuantos == 2:
            print("RECTANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            DDA1(x1, y1, x2, y2)
        if cuantos == 3:
            print("TRIANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            DDA2(x1, y1, x2, y2)
        if cuantos == 4:
            print("TRIANGULO RECTANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            DDA3(x1, y1, x2, y2)
# OPCION BRESENHAMS
    if tipo == 2:
        print("*****ALGORITMO BRESENHAMS******")
        cuantos = int(input("Selecciona uno\n1.Cuadrado\n2.Rectangulo\n3.Triangulo \n4.triangulo rectangulo\nSelecciona la figura con la que quieres trabajar: "))
        if cuantos == 1:
            print("CUADRADO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: ")) 
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            bre(x1, y1, x2, y2)
        if cuantos == 2:
            print("RECTANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            bre1(x1, y1, x2, y2)
        if cuantos == 3:
            print("TRIANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            bre2(x1, y1, x2, y2)
        if cuantos == 4:
            print("TRIANGULO RECTANGULO")
            x1 = int(input("INGRESA EL VALOR DE X1: "))
            y1 = int(input("INGRESA EL VALOR DE Y1: "))
            x2 = int(input("INGRESA EL VALOR DE X2: "))
            y2 = int(input("INGRESA EL VALOR DE Y2: "))
            bre3(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
