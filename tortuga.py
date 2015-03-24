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

tartaruga   = turtle.Turtle()  # Cria um objeto "desenhador"
tartaruga.speed(5)  # define a velocidade
tartaruga.penup()       # Remova e veja o que acontece
tartaruga.setpos(-200,0)
tartaruga.pendown()
tartaruga.color("orange")
tartaruga.shape("turtle")
tartaruga.fd(50)
tartaruga.left(90)
tartaruga.fd(200)
tartaruga.right(90)
tartaruga.fd(50)
tartaruga.right(90)
tartaruga.fd(30)
tartaruga.pu()
tartaruga.fd(170)
tartaruga.left(90)

for i in range(len(p)):
    if p[i] == ' ':
        tartaruga.penup()
        tartaruga.fd(13)
    else:    
        tartaruga.pendown()
        tartaruga.fd(10)
        tartaruga.penup()
        tartaruga.fd(3)

window.exitonclick()