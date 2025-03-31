#Luna e os Segredos do Código
#Luna estava animada com tudo o que havia aprendido com o Mestre Byte. Mas ela sabia que ainda havia muitos mistérios a desvendar sobre a linguagem mágica de Python.
#-Mestre Byte, que outros segredos o Python guarda? — perguntou Luna com os olhos brilhando de curiosidade.
# sábio sorriu e disse:
#-Agora que você conhece as variáveis e os operadores mágicos, é hora de entender os tipos de dados, os identificadores, Estruturas Condicionais e os operadores especiais.

#Os Tipos de Dados: O Que Podemos Guardar nas Caixinhas?
#Mestre Byte explicou que as variáveis podem guardar diferentes tipos de informações, e cada tipo tem um propósito especial.
#Ele mostrou a Luna os principais tipos de dados em Python:

# Tipo numérico inteiro (int)
idade = 10 

# Tipo numérico decimal (float)
altura = 1.35  

# Tipo texto (string - str)
nome = "Luna"  

# Tipo verdadeiro ou falso (booleano - bool)
aprendendo_python = True  

#Cada variável tem um tipo que define que tipo de valor ela pode guardar, — explicou Mestre Byte.
#Luna experimentou os diferentes tipos e percebeu como cada um tinha seu próprio comportamento.

#Identificadores: O Nome das Variáveis
#— Agora, Luna, — continuou Mestre Byte —, sempre que criamos uma variável, precisamos dar um nome a ela. Mas não pode ser qualquer nome!
#Ele então explicou as regras dos identificadores:
#Podem conter letras, números e _ (underline).
#Não podem começar com números.
#Não podem ter espaços.
##Não podem ser palavras reservadas do Python (como print, if, while).
#Luna tentou criar algumas variáveis com nomes inválidos, mas o computador reclamou.
#— Ahh, entendi! Preciso seguir essas regras para que o Python não fique confuso! — disse Luna.

#Expressões Mágicas: Como o Computador Resolve Cálculos?
#Mestre Byte mostrou que podemos combinar variáveis e operadores para criar expressões.
a = 10
b = 5
c = a + b  # Aqui temos uma expressão matemática!
print(c)  # Resultado: 15

#Os Operadores: As Ferramentas do Feiticeiro
#— Agora, Luna, vou te mostrar os operadores mágicos! Eles servem para fazer contas, comparar valores e tomar decisões!

#Operadores de Atribuição (usados para guardar valores em variáveis)

x = 10  # Atribui o valor 10 a x
x += 5  # Equivale a x = x + 5 (agora x vale 15)
x -= 3  # Equivale a x = x - 3 (agora x vale 12)

#Operadores Aritméticos (para fazer contas)

soma = 3 + 2   # Adição
sub = 10 - 4   # Subtração
mult = 5 * 2   # Multiplicação
div = 10 / 2   # Divisão
mod = 10 % 3   # Módulo (resto da divisão)
exp = 2 ** 3   # Exponenciação (2³ = 8)

#Operadores Relacionais (para comparar valores)

print(10 > 5)   # Verdadeiro
print(3 == 3)   # Verdadeiro
print(4 != 2)   # Verdadeiro
print(5 <= 2)   # Falso

#Operadores Lógicos (para fazer verificações)

a = True
b = False

print(a and b)  # Retorna False (só é verdadeiro se ambos forem verdadeiros)
print(a or b)   # Retorna True (basta um ser verdadeiro)
print(not a)    # Inverte o valor (se a é True, vira False)

#Luna viu que podia combinar esses operadores para criar regras mágicas no código!

#Desafio da Ponte Lógica
#Mestre Byte sorriu e apontou para uma ponte mágica sobre um rio de dados.
#— Agora, Luna, você precisa atravessar essa ponte! Mas só pode passar se resolver este desafio:

#idade = 12
#altura = 1.40

#pode_passar = idade >= 10 and altura >= 1.35

print("Luna pode atravessar a ponte?", pode_passar)

#Luna pensou e percebeu que, como idade é maior ou igual a 10 e altura é maior ou igual a 1.35, a resposta seria True!

#O Feitiço do "Se": A Estrutura if
#O Mestre Byte explicou que o comando if permite que o computador tome decisões.
#— Vamos supor que você está explorando Pythonia e precisa decidir se entra ou não em uma caverna. Se estiver com uma lanterna, pode entrar. Caso contrário, é melhor ficar do lado de fora.
#Luna viu o código que representava essa decisão:

tem_lanterna = True  

if tem_lanterna:  
    print("Luna entra na caverna.") 

#Ela testou o código e viu que, como tem_lanterna era True, a mensagem aparecia.
#— Uau! Então, se a condição for verdadeira, o código executa esse trecho!
#Mestre Byte acenou com a cabeça.

#O Caminho Alternativo: if e else
#— Mas, Luna, e se você não tiver uma lanterna? O código precisa saber o que fazer!
#Ele mostrou como usar else, que define um caminho alternativo:

tem_lanterna = False  

if tem_lanterna:  
    print("Luna entra na caverna.")  
else:  
    print("Luna espera do lado de fora.")  

#Agora, Luna testou com tem_lanterna = False e viu que o código escolheu a outra opção.
#— Isso é incrível! Posso dar diferentes caminhos para o código seguir!

#As Várias Possibilidades: elif
#Mestre Byte então mostrou que, às vezes, há mais de duas opções.
#— Imagine que você está diante de três portas mágicas. Cada uma tem um número diferente. Dependendo da escolha, um destino diferente se revelará.
#Ele escreveu:

porta = 2  

if porta == 1:  
    print("Luna encontra um tesouro!")  
elif porta == 2:  
    print("Luna conhece um dragão sábio!")  
elif porta == 3:  
    print("Luna entra em um portal para outro mundo!")  
else:  
    print("Essa porta não existe!")  

#Luna testou mudando o número da porta e viu que cada número levava a um resultado diferente!
#— Então o elif serve para quando há várias possibilidades!

#O Desafio do Guardião da Ponte
#Mestre Byte apontou para um troll que guardava uma ponte.

#— O Guardião só deixa passar quem for mais alto que 1.30m ou tiver um passe mágico. Como podemos programar isso?
#Luna pensou e escreveu o código:

altura = 1.25  
tem_passe = True  

if altura >= 1.30 or tem_passe:  
    print("O Guardião deixa Luna atravessar a ponte.")  
else:  
    print("Luna não pode atravessar.")  

#Mestre Byte sorriu.
#— Excelente, Luna! Você usou or para dizer que basta uma das condições ser verdadeira!
#Luna comemorou.
#— Estou cada vez mais perto de me tornar uma grande programadora de Pythonia!