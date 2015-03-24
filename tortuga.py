# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:28:42 2015

@author: Pedro
"""
import random
import turtle

dic = ['São Paulo', 'São Bernardo do Campo', 'Baleia Azul', 'leão marinho', 'wikipedia','videojogo', 'equinócio', 'Estônia', 'cenozóico', 'tardígrado', 'covalente']
i = 0
for i in range(0,len(dic)):
    dic[i] = dic[i].upper()
    
p = random.choice(dic)
print('Escolhas possíveis: ' ,dic)

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

for i in range(len(p)):
    tartaruga.pendown()
    tartaruga.fd(40)
    tartaruga.penup()
    tartaruga.fd(10)

window.exitonclick()