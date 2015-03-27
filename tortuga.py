# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:28:42 2015

@author: Pedro
"""
#Pedro Cunial Campos
import random
import turtle
import tkinter
import time
replay = True

window = turtle.Screen()    # cria uma janela
window.bgcolor("white")
window.title("Jogo")
    
def forca():    #desenha a forca
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
    
def linhas(p):   #linhas para escrever
    for i in range(len(p)):
        if p[i] == ' ':
            t.penup()
            t.fd(13)
        else:    
            t.pendown()
            t.fd(10)
            t.penup()
            t.fd(3)
            
def cabeca():  #desenha cabeça
    t.showturtle()
    t.pu()
    t.setpos(-100, 150)
    t.pd()
    t.circle(10)
    t.pu()
    t.hideturtle()

def corpo(): #desenha corpo (tronco)
    t.showturtle()
    t.pu()
    t.setpos(-100,150)
    t.pd()
    t.setpos(-100,120)
    t.pu()
    t.hideturtle()
    time.sleep(2)

def braco_direito(): #desenha braço direito
    t.showturtle()
    t.pu()
    t.setpos(-100,140)
    t.pd()
    t.setpos(-70,110)
    t.ht()
    t.pu()
    time.sleep(2)    

def braco_esquerdo(): #desenha braço esquerdo
    t.st()
    t.pu()
    t.setpos(-100,140)
    t.pd()
    t.setpos(-130,110)
    t.ht()
    t.pu()
    time.sleep(2)

def perna_esquerda(): #desenha perna esquerda
    t.st()
    t.pu()
    t.setpos(-100,120)
    t.pd()
    t.setpos(-120,75)
    t.pu()
    t.ht()
    time.sleep(2)    
    
def perna_direita(): #desenha perna direita
    t.st()
    t.pu()
    t.setpos(-100,120)
    t.pd()
    t.setpos(-80,75)
    t.pu()
    t.ht()
    time.sleep(2)
    
def escrita(i,j):
    t.st()        
    t.setpos(-98 + 13*i, 0)
    t.write(j)
    t.ht()
    time.sleep(1)
    
def tentativas(g,j):
    t.st()    
    t.setpos(-98 + 13*g, -50)
    t.write(j)
    t.ht()
    
while replay == True:
    t   = turtle.Turtle()  # Cria um objeto "desenhador"
    t.speed(5)  # define a velocidade
    t.penup()       # Remova e veja o que acontece
    t.pendown()
    t.color("orange")
    t.shape("turtle")
    
    print("playing")
    replay == False
    dic = open('entrada.txt', encoding= 'utf-8')
    dic = dic.readlines()
    
    for i in range(len(dic)-1): #por algum motivo o meu programa estava criando um valor ' ' (vazio) 
        dic[i] = dic[i].strip().upper()
        if dic[i] == '': #deletando o espaço vazio, no entanto isso cria um problema com o valor 'estônia', que assume 'estônia\n'
            del dic[i]
        dic[i] = dic[i].strip().upper() #"reaplicando" o algoritmo para "limpar" o erro no valor 'estônia'
        
    print('Escolhas possíveis: ' ,dic)
    p = random.choice(dic)
    
    t.pu()
    print(p)    
    t.setpos(-200,0)
    jogo = True
    erro = 0
    acerto = 0
    t.pd()
    forca()
    linhas(p)    
    t.hideturtle()
    guesses = [ ]
            
    while jogo == True:  
        print("jogo true")
        aceita = False
        
        while aceita == False:     #loop caso a entrada não seja válida             
            j = window.textinput("Jogada", "Escolha uma letra. \nMas escolha rápido, a menos que você prefira o Billy morto...") 
            #linha acima é para a entrada da jogada
            if j == None:
                tkinter.messagebox.showwarning('ERRO', 'Você precisa entrar com uma letra,\na menos que você não se importe com o futuro de Billy...\nNão que ele tivesse futuro de qualquer jeito...')
            j = j.upper()   #correção da jogada para caixa alta
            esp = p.count(' ')  
                        
            if len(j) > 1: #caso o usuário entre com mais de uma letra
                tkinter.messagebox.showwarning('ERRO', 'Você digitou mais de uma letra, por favor, tente novamente...\nOu não... Eu adoraria enforcar este humano...')
            elif j in guesses:
                tkinter.messagebox.showwarning('ERRO', 'Você já tentou essa letra, faça outra escolha!\nTEM GENTE TENTANDO MORRER AQUI!')
            
            else:
                aceita = True   #sai do loop caso a entrada seja válida
                guesses += [j]
                tentativas(len(guesses),j)
        for i in range(len(p)):
            if p[i] == j:
                escrita(i,j)
                acerto += 1
            elif j == 'A' and p[i] == 'Ã': #facilitando a vida dos brasileiros...
                escrita(i,p[i])
                acerto += 1
            elif j == 'O' and p[i] == 'Ô':
                escrita(i,p[i])
                acerto += 1
            elif j == 'O' and p[i] == 'Ó':
                escrita(i,p[i])
                acerto += 1
            elif j == 'I' and p[i] == 'Í':
                escrita(i,p[i]) 
                acerto += 1
        if j not in p:
            erro += 1   #adiciona 1 ao contador de erros
        
            if erro == 1:   #if para impressão das partes do boneco (Billy) conforme o usuário erra
                cabeca()
                tkinter.messagebox.showwarning('CUIDADO!', 'Me chamavam de quebra-cabeças na escola...\nHoje eu sei o porquê MUAHAHA')
            elif erro == 2:
                corpo()
                tkinter.messagebox.showwarning('CUIDADO!', 'Nossa Billy, como você está magro!\nQuando foi a ultima vez que eu te dei comida?\nAh! Me lembrei! NUNCA! HAHAHAH')
            elif erro == 3:
                braco_esquerdo()
                tkinter.messagebox.showwarning('CUIDADO!', 'Tudo bem, Billy era destro...\nEu acho.')
            elif erro == 4:
                braco_direito()
                tkinter.messagebox.showwarning('CUIDADO!', 'Problema resolvido!\nSem os braços ele não é mais destro.')
            elif erro == 5:
                perna_direita()
                tkinter.messagebox.showwarning('CUIDADO!', 'Só mais um errinho!!!')
            elif erro == 6:
                perna_esquerda()
                jogo = False
                replay = tkinter.messagebox.askyesno('Game Over', 'DIGA ADEUS PRO SEU AMIGUINHO BILLY\nEU SOU VITORIOSO (como sempre, claro)!!\nVocê perdeu, deseja jogar novamente?')
                t.clear()
                print(replay)
        if acerto == len(p) - esp:  #subtrai-se números de espaços da palavra, considando que espaço não seria uma resposta válida
            jogo = False
            replay = tkinter.messagebox.askyesno('VITÓRIA', 'MALDITO!\nBILLY NÃO SAIRÁ VIVO NA PRÓXIMA!\nDeseja jogar novamente?')
            t.clear()
            print(replay)
     
window.exitonclick()       