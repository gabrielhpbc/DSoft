import turtle
import time

print ("Olá! Este é o Draw Your Fractal, neste programa você poderá desenhar um fractal a partir de alguns comandos!")
time.sleep(5)
print("A letra utilizada de comando será o F! Levando a caneta de desenho, no caso uma flecha, para a direção desejada!")
print("Para iniciar é importante saber que há um comando básico, ou seja para todo F digitado há um 'replace' para um comando capaz de ser replicado e formar o fractal final")
time.sleep(7)
print("O desenho ainda necessita que sejam passados alguns parâmetros a seguir: ")
Clinha = int(input('Digite o comprimento de cada linha (tamanho): '))
AngInicial = int(input('Escolha um valor para o ângulo entre comandos: '))
Repetições = int(input('Digite um valor inteiro para número de repetições do comando: '))
Cor = input("Digite uma cor para o desenho (em inglês): ")
print("Lembrando que o código é descrito em F's, para parâmetros iniciais o valor de F, ou seja F, comando para frente, +F, virar para direita, -F, virar para esquerda")
print(" e por último [F, comando para trás")
print ("Esses digitos só serão executados dessa maneira no replace para o código básico de fractal, ao escrever como comando a seguir ele será apenas capaz de variar a direção do ângulo inicial! ")
time.sleep(3)
#A partir daqui cria-se uma função com os paramêtros designados para criação do desenho
def y (Clinha,AngInicial,Repetições):
	o = str(input('Descreva o código do fractal:'))
	t = turtle.Turtle()
	t.lt(90)
	t.pencolor(Cor)
	t.speed(10)
	p=0
	while p<Repetições:
#O replace a seguir servirá para trocar as strings em função de F passadas para substituir por um código maior que irá se repetir da maneira escrita 
		o = o.replace('F','F--FF+FF[+F[-FF-F[+F')
		print(o)
#Definição de direção para cada tipo de F passado para mudar a direção do ângulo inicial
		for i in range(len(o)):
			if o[i] == 'F':
				t.forward(Clinha)
			if o[i] == '+':
				t.rt(AngInicial)
			if o[i] == '-':
				t.lt(AngInicial)
			if o[i] == '[':
				t.back(Clinha)
		p=p+1

y(Clinha,AngInicial,Repetições)


#Comando para não fechar ao terminar o desenho 
turtle.exitonclick()