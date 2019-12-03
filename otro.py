import tkinter
from tkinter import *  # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from math import *
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy


def mostrar(ventana1, ventana2):
    ventana2.withdraw()
    ventana1.deiconify()


def ocultar(ventana):
    ventana.withdraw()


def integrar_trapecio(n, a, b, funcion, r):
    x = symbols('x')  # establecemos a x como variable simbolica
    n1 = int(n.get())
    a1 = int(a.get())
    b1 = int(b.get())

    expresion = funcion.get()
    expresion = sympify(expresion)

    # evaluamos la funcion
    f = lambda xk: expresion.subs(x, xk).evalf()

    h = float((b1 - a1) / n1)
    sum = 0

    for i in range(1, n1):
        xk = a1 + i * h
        sum = sum + f(xk)
        plt.plot(i, f(i), 'co')
    r.set(h * (((f(a1) + f(b1)) / 2) + sum))

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Trapecio')
    plt.grid(True)
    plt.show()


def interpolacion(xi, yi, n, ecu, r):
    x = np.fromstring(xi.get(), dtype=int, sep=',')
    y = np.fromstring(yi.get(), dtype=int, sep=',')
    n1 = int(n.get())

    result = scipy.poly1d([0.0])

    for i in range(0, len(x)):
        temp_numerador = scipy.poly1d([1.0])
        denominador = 1.0
        for j in range(0, len(x)):
            if i != j:
                temp_numerador *= scipy.poly1d([1.0, -x[j]])
                denominador *= x[i] - x[j]
        result += (temp_numerador / denominador) * y[i]
    ecu.set(result)
    ev = result(n1)
    r.set(ev)

    x_val = np.arange(min(x), max(x) + 1, 0.1)
    plt.xlabel('x');
    plt.ylabel('y')
    plt.grid(True)

    for i in range(0, len(x)):
        plt.plot([x[i]], [y[i]], 'ro')
    plt.plot(x_val, result(x_val))
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.show()


def ventanaTrapecio():
    ocultar(ventanaPrincipal)
    ventana = Toplevel(ventanaPrincipal)
    ventana.title("Metodo de Integracion")
    ventana.resizable(0, 0)
    ventana.geometry("450x200")
    ventana.configure(background='#B2FFFF')
    Label(ventana, text="REGLA COMPUESTA DEL TRAPECIO").grid(row=0, column=3)

    n = StringVar()
    a = StringVar()
    b = StringVar()
    funcion = StringVar()
    r = StringVar()

    Label(ventana, text="n: ").grid(pady=5, row=1, column=0)
    Entry(ventana, justify="right", width="5", textvariable=n).grid(padx=5, row=1, column=1)

    Label(ventana, text="a: ").grid(pady=5, row=1, column=2)
    Entry(ventana, justify="right", width="5", textvariable=a).grid(padx=5, row=1, column=3)

    Label(ventana, text="b: ").grid(pady=5, row=1, column=4)
    Entry(ventana, justify="right", width="5", textvariable=b).grid(padx=5, row=1, column=5)

    Label(ventana, text="f(x): ").grid(pady=5, row=2, column=0)
    Entry(ventana, justify="right", width="25", textvariable=funcion).grid(padx=5, row=2, column=1, columnspan=5)

    integrar = ttk.Button(ventana, text="Integrar", command=lambda: integrar_trapecio(n, a, b, funcion, r)).grid(pady=5,
                                                                                                                 row=3,
                                                                                                                 column=0,
                                                                                                                 columnspan=5)

    Label(ventana, text="Resultado: ").grid(pady=5, row=4, column=0)
    Entry(ventana, justify="right", width="20", textvariable=r).grid(padx=5, row=4, column=1, columnspan=5)

    volver = ttk.Button(ventana, text="Volver", command=lambda: mostrar(ventanaPrincipal, ventana)).grid(pady=5, row=6,
                                                                                                         column=0,
                                                                                                         columnspan=6)


def ventanaFalsaP():
    ocultar(ventanaPrincipal)
    ventana = Toplevel(ventanaPrincipal)
    ventana.title("Metodo")
    ventana.resizable(0, 0)
    ventana.geometry("450x300")
    ventana.configure(background='#B2FFFF')
    Label(ventana, text="POLINOMIO").grid(row=0, column=1)

    xi = StringVar()
    yi = StringVar()
    n = StringVar()
    ecu = StringVar()
    r = StringVar()

    Label(ventana, text="Puntos xi: ").grid(pady=5, row=1, column=0)
    Entry(ventana, justify="right", width="20", textvariable=xi).grid(padx=5, row=1, column=1)

    Label(ventana, text="Puntos yi: ").grid(pady=5, row=2, column=0)
    Entry(ventana, justify="right", width="20", textvariable=yi).grid(padx=5, row=2, column=1)

    Label(ventana, text="Numero a evaluar: ").grid(pady=5, row=3, column=0)
    Entry(ventana, justify="right", width="5", textvariable=n).grid(padx=5, row=3, column=1)

    interpolar = ttk.Button(ventana, text="Interpolacion", command=lambda: interpolacion(xi, yi, n, ecu, r)).grid(
        pady=5, row=4, column=0, columnspan=5)

    Label(ventana, text="Ecuacion: ").grid(pady=5, row=5, column=0)
    Label(ventana, justify="right", textvariable=ecu).grid(padx=5, row=5, column=1)

    Label(ventana, text="Resultado: ").grid(pady=5, row=6, column=0)
    Entry(ventana, justify="right", width="20", textvariable=r).grid(padx=5, row=6, column=1)

    volver = ttk.Button(ventana, text="Volver", command=lambda: mostrar(ventanaPrincipal, ventana)).grid(pady=5, row=7,
                                                                                                         column=0,
                                                                                                         columnspan=6)


ventanaPrincipal = Tk()
ventanaPrincipal.title("PROYECTO INF - 156")
ventanaPrincipal.resizable(0, 0)
ventanaPrincipal.geometry("400x300")
ventanaPrincipal.configure(background='#808000')
Label(ventanaPrincipal, text="MENU", bg="#808000", font="Helvetica 30 bold italic").place(x=150, y=30)

integrar = ttk.Button(ventanaPrincipal, text="Regla Trapecio", command=ventanaTrapecio).place(x=120, y=80, width=150,
                                                                                              height=50)
falsaP = ttk.Button(ventanaPrincipal, text="falsa posicion", command=ventanaFalsaP).place(x=100, y=140, width=190,
                                                                                          height=50)

ventanaPrincipal.mainloop()
