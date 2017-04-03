import matplotlib.pyplot as plt
import numpy as np
import math as mt

GRAV = 9.8
DT = 0.1
HEIGHT = 100.0
MAX_TIME = 100.0

def freeFallA (x_initial, v_initial, t):
    while (t < MAX_TIME):
        xpos = x_initial + v_initial*t - (GRAV*t*t)/2
        plt.plot(t, xpos, 'kx')
        t += DT
    return

def freeFallE (x_initial, v_initial, t):
    xpos = x_initial
    vcur = v_initial
    while (t < MAX_TIME):
        vcur -= GRAV*DT
        xpos += vcur*DT
        plt.plot(t, xpos, 'rx')
        t += DT
    return

def dyA(x_initial):
    x = x_initial
    while (x < MAX_TIME):
        y = x*x
        plt.plot(x, y, 'rx')
        x += DT
    return

def dyE(x_initial):
    x = x_initial
    y = 0
    while(x < MAX_TIME):
        y += 2*x*DT
        plt.plot(x, y, 'ko')
        x += DT
    return

def shoA (x_initial, v_initial, k, mass):
    x = x_initial
    w = mt.sqrt(k/mass)
    a = x_initial
    b = (v_initial/w)
    while (x < MAX_TIME):
        y = a*mt.cos(w*x) + b*mt.sin(w*x)
        x += DT
        plt.plot(x, y, 'rx')
    return

def shoE (x_initial, v_initial, t_initial, k, mass):
    t = t_initial
    v = v_initial
    x = x_initial
    while (t < MAX_TIME):
        x += v*DT
        v -= (k*x)/mass*DT
        plt.plot(t, x, 'ko')
        t += DT
    return


def main():
    # freeFallA(HEIGHT, 0.0, 0.0)
    # freeFallE(HEIGHT, 0.0, 0.0)
    # dyA(0.0)
    # dyE(0.0)
    shoA(5.0, 0.0, 1, 10)
    shoE(5.0, 0.0, 0.0, 1, 10)
    plt.show()
    return 0

main()

