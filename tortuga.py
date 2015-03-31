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
import string
replay = True
le = [] #criando uma lista vazia para contar os erros por jogo para calcular o número médio de erros
window = turtle.Screen()    # cria uma janela
window.bgcolor("black")
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
    time.sleep(1)

def braco_direito(): #desenha braço direito
    t.showturtle()
    t.pu()
    t.setpos(-100,140)
    t.pd()
    t.setpos(-70,110)
    t.ht()
    t.pu()
    time.sleep(1)    

def braco_esquerdo(): #desenha braço esquerdo
    t.st()
    t.pu()
    t.setpos(-100,140)
    t.pd()
    t.setpos(-130,110)
    t.ht()
    t.pu()
    time.sleep(1)

def perna_esquerda(): #desenha perna esquerda
    t.st()
    t.pu()
    t.setpos(-100,120)
    t.pd()
    t.setpos(-120,75)
    t.pu()
    t.ht()
    time.sleep(1)    
    
def perna_direita(): #desenha perna direita
    t.st()
    t.pu()
    t.setpos(-100,120)
    t.pd()
    t.setpos(-80,75)
    t.pu()
    t.ht()
    time.sleep(1)
    
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

def media(lista):
    x = 0
    if len(lista) > 0:  
        for i in range(len(lista)):
            x += lista[i]
        x = x / len(lista)
        x = str(x)
        t.pu()
        t.setpos(80, 200)
        t.pd()
        t.write('Média de erros para vitória:' +x, font=('Arial', '12'))
        t.pu()
 
pusadas = ['x']  #cria a lista de palavras usadas para que o programa feche quando toda a lista já tenha sido usada       
letras = list(string.ascii_uppercase)
letras += ['Ç']

while replay == True:
    t   = turtle.Turtle()  # Cria um objeto "desenhador"
    t.speed(5)  # define a velocidade
    t.penup()       # Remova e veja o que acontece
    t.pendown()
    t.color("white")
    t.shape("turtle")    
    replay == False
    dic = open('entrada.txt', encoding= 'utf-8')
    dic = dic.readlines()
    plivre = False
    
    for i in range(len(dic)-1): #por algum motivo o meu programa estava criando um valor ' ' (vazio) 
        dic[i] = dic[i].strip().upper()
        if dic[i] == '': #deletando o espaço vazio, no entanto isso cria um problema com o valor 'estônia', que assume 'estônia\n'
            del dic[i]
        dic[i] = dic[i].strip().upper() #"reaplicando" o algoritmo para "limpar" o erro no valor 'estônia'

    if len(pusadas) > len(dic):
        tkinter.messagebox.showinfo(':\'(','Acabaram as palavras possíveis, até a próxima!')
        window.bye()    #não sei exatamente o porquê, mas fechar o programa só uma vez não foi suficiente
        window.bye()    #portanto, fechei duas.
    else:
        while plivre == False: #loop para conferir se a palavra a ser sorteada já foi usada
            p = random.choice(dic)  #sorteia a palavra
            if p not in pusadas:    #caso já tenha sido usada, entra no loop
                plivre = True
                pusadas += [p]
            else: #caso contrário
                plivre = False
        
        p2 = p.replace('Ã','A').replace('Ô','O').replace('Ó','O').replace('Í','I')  #corrige a palavra sem acentos para os brasileiros
        t.pu()
        t.setpos(-200,0)
        jogo = True
        erro = 0
        acerto = 0
        t.pd()
        forca()
        linhas(p)    
        t.hideturtle()
        guesses = [ ]
        media(le)
        chute = False
            
        while jogo == True:  
            aceita = False
            
            while aceita == False:     #loop caso a entrada não seja válida             
                j = window.textinput("Jogada", "Escolha uma letra. \nMas escolha rápido, a menos que você prefira o Billy morto...") 
                #linha acima é para a entrada da jogada
                if j == None:
                    window.bye() #caso o usuário clique em "cancel" o jogo será fechado
                j = j.upper()   #correção da jogada para caixa alta
                esp = p.count(' ')  
                            
                if len(j) > 1: #caso o usuário entre com mais de uma letra o jogo o dará mais uma chance, caso seja um erro de digitação etc, ele pode clicar em 'não' e voltar a jogar, mas caso esteja tentando chutar a palavra o jogo reagirá propriamente
                    chute = tkinter.messagebox.askyesno('ATENÇÃO!', 'Então quer dizer que você acha que sabe a palavra?\nVou te dar mais uma chance, clique em Sim se realmente deseja chutar a palavra\nOu clique em Não, se for um frcassado como Billy...')
                    if chute == True:
                        if j == p2: #caso a pessoa digite a palavra inteira corretamente ela ganha
                            aceita = True                        
                            jogo = False
                            replay = tkinter.messagebox.askyesno('VITÓRIA', 'MALDITO!\nBILLY NÃO SAIRÁ VIVO NA PRÓXIMA!\n\nDeseja jogar novamente?')
                            t.clear()
                            le = le + [erro]
                        else: #caso contrário...
                            aceita = True                        
                            jogo = False
                            replay = tkinter.messagebox.askyesno('Game Over', 'DIGA ADEUS PARA O BILLY\nEU SOU VITORIOSO !!(como sempre, claro)\n\nVocê perdeu, deseja jogar novamente?')
                            t.clear()
                            le = le + [erro + 1] #é adicionado +1 ao valor de erros dessa rodada
                    else:
                        tkinter.messagebox.showwarning('CUIDADO!', 'Huh, um engano?\n Não vá se acostumando, mas vou te dar mais uma chance...\nHumanos estúpidos...')
                elif j in guesses:
                    tkinter.messagebox.showerror('ERRO', 'Você já tentou essa letra, faça outra escolha!\nTEM GENTE TENTANDO MORRER AQUI!')
                elif j not in letras:
                    tkinter.messagebox.showerror('ERRO', 'Você não sabe o que são letras?\nPare de entrar com essas estranhices!\n\nParece mais burro que o Billy!')
                else:
                    aceita = True   #sai do loop caso a entrada seja válida
                    guesses += [j]
                    tentativas(len(guesses),j)
            if chute == False:
                correto = False
                for i in range(len(p)):
                    if p[i] == j or p2[i] == j:
                        escrita(i,p[i])
                        acerto += 1
                        correto = True #define o palpite como correto
                
                if correto == False:    #caso o palpite esteja errado (não passou pelo "filtro" if anterior):
                    erro += 1   #adiciona 1 ao contador de erros
                
                    if erro == 1:   #if para impressão das partes do boneco (Billy) conforme o usuário erra
                        cabeca()
                        tkinter.messagebox.showwarning('CUIDADO!', 'Me chamavam de quebra-cabeças na escola...\nHoje eu sei o porquê MUAHAHA')
                    elif erro == 2:
                        corpo()
                        tkinter.messagebox.showwarning('CUIDADO!', 'Nossa Billy, como você está magro!\nQuando foi a ultima vez que eu te dei comida?\nAh! Me lembrei! NUNCA! HAHAHAH')
                    elif erro == 3:
                        braco_direito()
                        tkinter.messagebox.showwarning('CUIDADO!', 'Tudo bem, Billy era destro...\nEu acho.')
                    elif erro == 4:
                        braco_esquerdo()
                        tkinter.messagebox.showwarning('CUIDADO!', 'Problema resolvido!\nSem os braços ele não é mais destro.')
                    elif erro == 5:
                        perna_direita()
                        tkinter.messagebox.showwarning('CUIDADO!', 'Só mais um errinho!!!')
                    elif erro == 6:
                        perna_esquerda()                    
                        jogo = False
                        replay = tkinter.messagebox.askyesno('Game Over', 'DIGA ADEUS PARA O BILLY\nEU SOU VITORIOSO !!(como sempre, claro)\n\nVocê perdeu, deseja jogar novamente?')
                        t.clear()
                        le = le + [erro]
            if acerto == len(p) - esp:  #subtrai-se números de espaços da palavra, considando que espaço não seria uma resposta válida
                    jogo = False
                    replay = tkinter.messagebox.askyesno('VITÓRIA', 'MALDITO!\nBILLY NÃO SAIRÁ VIVO NA PRÓXIMA!\n\nDeseja jogar novamente?')
                    t.clear()
                    le = le + [erro]    #adiciona o valor de erros deste jogo à lista que será usada para calcular a média
         
window.exitonclick()       