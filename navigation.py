from directkeys import PressKey, ReleaseKey , W, A, S, D
import time

def forward():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    

def right():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)
    

def slow():
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def stop():
    PressKey(S)
    ReleaseKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
