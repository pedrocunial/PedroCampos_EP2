# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:28:42 2015

@author: Pedro
"""
#Pedro Cunial Campos
import random
import turtle

dic = open('entrada.txt', encoding= 'utf-8')
dic = dic.readlines()

for i in range(len(dic)-1): #por algum motivo o meu programa estava criando um valor ' ' (vazio) 
    dic[i] = dic[i].strip().upper()
    if dic[i] == '': #deletando o espaço vazio, no entanto isso cria um problema com o valor 'estônia', que assume 'estônia\n'
        del dic[i]
    dic[i] = dic[i].strip().upper() #"reaplicando" o algoritmo para "limpar" o erro no valor 'estônia'
    
print('Escolhas possíveis: ' ,dic)
p = random.choice(dic)

print(p)    

window = turtle.Screen()    # cria uma janela
window.bgcolor("white")
window.title("Jogo")

t   = turtle.Turtle()  # Cria um objeto "desenhador"
t.speed(5)  # define a velocidade
t.penup()       # Remova e veja o que acontece
t.setpos(-200,0)
t.pendown()
t.color("orange")
t.shape("turtle")
t.fd(50)
t.left(90)
t.fd(200)
t.right(90)
t.fd(50)
t.right(90)
t.fd(30)
t.pu()
t.fd(170)
t.left(90)

for i in range(len(p)):
    if p[i] == ' ':
        t.penup()
        t.fd(13)
    else:    
        t.pendown()
        t.fd(10)
        t.penup()
        t.fd(3)

t.hideturtle()

def cabeca():  #desenha cabeça
    t.showturtle()
    t.pu()
    t.setpos(-100, 150)
    t.pd()
    t.circle(10)
    t.pu
    t.hideturtle()

def corpo():
    t.showturtle()
    t.pu()
    t.setpos(-100,150)
    t.pd()
    t.setpos(-100,120)
    t.pu()
    t.hideturtle()

def braco_direito():
    t.showturtle()
    t.pu()
    t.setpos(-100,140)
    t.pd()
    t.setpos(-70,110)
    t.ht()
    t.pu()    

def braco_esquerdo():
    
    
window.exitonclick()