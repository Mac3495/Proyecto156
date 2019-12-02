import tkinter as tk
from tkinter import *

from sympy import * #importamos la libreria sympy
from sympy import lambdify

import matplotlib.pyplot as plt
import numpy as np

def bisec():
    x = symbols('x')

    a = int(ia.get())
    b = int(ib.get())

    ca = a
    cb = b

    tolerancia = float(t.get())

    c = 0.0

    expr = expre.get()

    expr = sympify(expr)

    f = lambda xk: expr.subs(x, xk).evalf()

    N = int(log(b - a) - log(tolerancia) / log(2))
    print('N = ', N)
    N1.set(N)
    if f(a) * f(b) > 0:  # verificamos que exista una raiz
        print('No existe raiz en el intervalo')
    else:
        for i in range(N):
            c = (a + b) / 2.0  # hallamos el punto medio
            print('k = %d, a = %.3f, c = %.3f, b = %.3f' % (i + 1, a, c, b))
            if f(a) * f(c) < 0:  # la raiz esta en [a,c]
                b = c
            elif f(c) * f(b) < 0:  # la raiz esta en [b, c]
                a = c
            else:
                break  # encontramos la raiz
        print('La raiz es %.5f' % (c))# imprimir con formato
        C1.set('%.5f' % (c))

    lam_x = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(a-3, b+3, 50)
    y_vals = lam_x(x_vals)
    plt.axhline(color='black')

    plt.title('Gráfica')
    plt.xlabel('eje x')
    plt.ylabel('eje y')
    plt.text(c, 10, expr, fontsize=18, color='red')

    plt.plot(x_vals, y_vals, color='red')
    plt.grid(True)
    plt.axvline(x=c, color='green', label='raiz')
    plt.axvline(x=ca, color='yellow', label='a')
    plt.axvline(x=cb, color='yellow', label='b')


def graficar():
    plt.show()


def simp():
    x = symbols('x')
    a = int(sa.get())
    b = int(sb.get())
    n = int(sn.get())

    expr = sexpre.get()

    expr = sympify(expr)

    f = lambda valor: expr.subs(x, valor).evalf()
    h = (b - a) / n
    m = (n - 2) / 2
    m = int(m) + 1
    xi = lambda y: a + y * h
    s1 = 0.0
    s2 = 0.0
    s = 0.0
    for i in range(0, m):
        s1 = s1 + f(xi(2 * i + 1))
    for i in range(1, m):
        s2 = s2 + f(xi(2 * i))
    s = f(xi(0)) + f(xi(n)) + 4 * s1 + 2 * s2
    s = (h / 3) * s
    print('el resultado es: ', s)
    R.set(s)

    lam_x = lambdify(x, expr, modules=['numpy'])
    x_vals = np.linspace(a - 2, b + 2, 100)
    y_vals = lam_x(x_vals)

    plt.title('Gráfica')
    plt.xlabel('eje x')
    plt.ylabel('eje y')

    plt.axvline(x=a, color='green', label='a')
    plt.axvline(x=b, color='green', label='b')

    plt.plot(x_vals, y_vals, color='red')
    plt.axhline(color='black')
    plt.fill_between(x_vals, y_vals, where=[(x_vals >= 0) and (x_vals <= b) and (x_vals >= a) for x_vals in x_vals])

    h = "$\int_"
    i = "^"
    j = "\mathrm{d}x$"
    k = str(expr)
    l = str(a)
    ll = str(b)
    plt.text(0.5 * (a + b), 25, "{}{}{}{}{}{}".format(h, l, i, ll, k, j), horizontalalignment='center', fontsize=18)
    #plt.show()

def volver(root, win):
    root.deiconify()
    win.destroy()

def bisection():
    winB = tk.Toplevel(root)
    winB.geometry('300x650')
    winB.configure(bg = "#2196F3")
    winB.title("Metodo de Bisección")
    Label(winB, text="Introduzca a", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify=CENTER, textvariable = ia).pack()
    Label(winB, text="\nIntroduzca b", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify=CENTER, textvariable = ib).pack()
    Label(winB, text="\nIntroduzca la tolerancia", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify=CENTER, textvariable= t).pack()
    Label(winB, text="\nIntroduzca f(x)", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify=CENTER, textvariable= expre).pack()
    Label(winB, text="", bg="#2196F3", fg="white", font=("",22)).pack()
    Button(winB, text="Bisección", command=bisec).pack()
    Label(winB, text="", bg="#2196F3", fg="white", font=("", 16)).pack()
    Button(winB, text="graficar", command=graficar).pack()

    Label(winB, text="\nSolución", bg="#2196F3", fg="white", font=("",18)).pack()
    Label(winB, text="\nResultado N", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify="center", textvariable=N1, state="disabled").pack()
    Label(winB, text="\nLa raíz es", bg="#2196F3", fg="white", font=("",18)).pack()
    Entry(winB, justify="center", textvariable=C1, state="disabled").pack()

    Label(winB, text="", bg="#2196F3", fg="white", font=("", 22)).pack()
    Button(winB, text="Volver", command= lambda : volver(root, winB)).pack()

    print("Bisection")
    root.withdraw()


def simpson():
    winS = tk.Toplevel(root)
    winS.geometry('300x650')
    winS.configure(bg="#F44336")
    winS.title("Metodo de Simpson")
    Label(winS, text="Introduzca a", bg="#F44336", fg="white", font=("",18)).pack()
    Entry(winS, justify=CENTER, textvariable=sa).pack()
    Label(winS, text="\nIntroduzca b", bg="#F44336", fg="white", font=("",18)).pack()
    Entry(winS, justify=CENTER, textvariable=sb).pack()
    Label(winS, text="\nIntroduzca n (Número par)", bg="#F44336", fg="white", font=("",18)).pack()
    Entry(winS, justify=CENTER, textvariable=sn).pack()
    Label(winS, text="\nIntroduzca f(x)", bg="#F44336", fg="white", font=("",18)).pack()
    Entry(winS, justify=CENTER, textvariable=sexpre).pack()
    Label(winS, text="", bg="#F44336", fg="white", font=("",22)).pack()
    Button(winS, text="Simpson", command=simp).pack()
    Label(winS, text="", bg="#F44336", fg="white", font=("", 16)).pack()
    Button(winS, text="Graficar", command=graficar).pack()

    Label(winS, text="\nSolución", bg="#F44336", fg="white", font=("",18)).pack()
    Label(winS, text="\nEl resultado es", bg="#F44336", fg="white", font=("",18)).pack()
    Entry(winS, justify="center", textvariable=R, state="disabled").pack()

    Label(winS, text="", bg="#F44336", fg="white", font=("", 22)).pack()
    Button(winS, text="Volver", command=lambda: volver(root, winS)).pack()

    root.withdraw()


root = tk.Tk()

ia = StringVar()
ib = StringVar()
t = StringVar()
expre = StringVar()
N1 = StringVar()
C1 = StringVar()

sa = StringVar()
sb = StringVar()
sn = StringVar()
sexpre = StringVar()
R = StringVar()


root.geometry('300x650')

root.configure(bg = '#009688')

root.title('Proyecto de 156')

Label(root, text="", bg="#009688", fg="white", font=("",32)).pack()

Label(root, text="INF - 156" , bg="#009688", fg="white", font=("",32)).pack()

Label(root, text="", bg="#009688", fg="white", font=("",32)).pack()

Label(root, text="Integrantes:", bg="#009688", fg="white", font=("",22)).pack()
Label(root, text="- Torrez Azuga Marcelo", bg="#009688", fg="white", font=("",22)).pack()
Label(root, text="- Lemus Miranda Josué", bg="#009688", fg="white", font=("",22)).pack()
Label(root, text="- Gemio Quispe José Miguel", bg="#009688", fg="white", font=("",22)).pack()

Label(root, text="", bg="#009688", fg="white", font=("",16)).pack()

Button(root, text='Bisección', command=bisection).pack()

Label(root, text="", bg="#009688", fg="white", font=("",16)).pack()

Button(root, text='Simpson', command=simpson).pack()

Label(root, text="", bg="#009688", fg="white", font=("",16)).pack()

Button(root, text='Salir', command=quit).pack()

root.mainloop()