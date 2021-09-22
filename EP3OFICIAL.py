#------------------------------------------------------------------
# Nome: Lyliana Myllena Santos de Sousa
# NUSP: 11223740
# EP1: Caca ao Ouro no Mundo do Wumpus
#-----------------------------------------------------------------


'''
    Ao preencher esse cabecalho com o meu nome e o meu numero USP,
    declaro que todas as partes originais desse exercicio programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto nao 
    constituem desonestidade academica ou plagio.
    Declaro tambem que sou responsavel por todas as copias desse
    programa e que nao distribui ou facilitei a sua distribuicao.
    Estou ciente que os casos de plagio e desonestidade academica
    serao tratados segundo os criterios divulgados na pagina da 
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderao ser punidos por desonestidade academica.
    Descricao de ajuda ou indicacao de fonte: Nesse EP eu nao utilizei a
    a ajuda de nenhum amigo, monitor ou professor. A logica do progrma a 
    foi montada com base no que aprendi em sala de aula.

'''

#primeiro vou definir a funcao que le o nosso arquivo txt e o transforma em uma lista
def mundo(entrada):
    L = []
    #definimos o parametro "r" na função a seguir porque queremos apenas que o arquivo txt seja apenas lido
    with open (entrada, "r", encoding = "utf-8") as arq:
        for linha in arq:
            x = linha.strip("\n")
            L.append(x)
    return L

#vou criar uma funcao para criar uma matriz onde eu preencherei a mundo
def criando_mundo_vazia(N):
    mundo = []
    for lin in range (N):
        linha = []
        for col in range(N):
            linha.append("")
        mundo.append(linha)
    return mundo

def le_mundo(l,N):
    #o elemento zero da lista L nos dara as dimensoes das matrizes
    i = (len(l) - 1)
    mundo = criando_mundo_vazia(N)
    percepcao = criando_mundo_vazia(N)
    while i>0:
        for lin in range (N):
            for col in range(N):
                x = int(l[i])
                coluna = (x - ((lin + 1)*100))//10
                linha = x//100
                item = (x - ((lin + 1)*100) - ((col +1)*10))
                if (linha == (lin+1)) and (coluna == (col + 1)) and (item == 1):
                    #se isso ocorre significa que nesse espaço existe um poco 
                   mundo[lin][col] = "P"
                   if ((col - 1) >= 0):
                       percepcao[lin][col - 1] =  percepcao[lin][col - 1] + "B"
                   if ((col + 1) < N):
                       percepcao[lin][col + 1] =  percepcao[lin][col + 1] + "B"
                   if ((lin - 1) >= 0):
                       percepcao[lin - 1][col] =  percepcao[lin - 1][col] + "B"
                   if ((lin +1) < N): 
                       percepcao[lin + 1][col] =  percepcao[lin + 1][col] + "B" 
                
                elif (linha == (lin+1)) and (coluna == (col + 1)) and (item == 2):
                    #se isso ocorre significa que nesse espaco existe um Wumpus 
                    mundo[lin][col] = "W"
                    Wumpus = [lin,col]
                    if ((col - 1) >= 0):
                         percepcao[lin][col - 1] = percepcao[lin][col - 1] +  "F"
                    if ((col + 1) < N):
                         percepcao[lin][col + 1] = percepcao[lin][col + 1] + "F"
                    if ((lin - 1) >= 0):   
                         percepcao[lin - 1][col] =  percepcao[lin - 1][col] + "F"
                    if ((lin +1) < N):    
                         percepcao[lin + 1][col] =  percepcao[lin + 1][col] + "F"
                        
                    
                elif (linha == (lin+1)) and (coluna == (col + 1)) and (item == 3):
                    #se isso ocorre significa que nesse espaço existe um ouro
                    mundo[lin][col] = mundo[lin][col] + "O"
                    percepcao[lin][col] = percepcao[lin][col] +  "R"
                    ouro = [lin,col]
                else:
                    #para qualquer outro caso, o espaco ficara em  branco
                    mundo[lin][col] =  mundo[lin][col] + " "
                    percepcao[lin][col] =  percepcao[lin][col] + " "
        i -= 1 
    le = [mundo, percepcao, Wumpus, ouro]
    return le

def imprime_mundo(l,N):
    matriz_mundo = le_mundo
    Mundo = matriz_mundo[0]
    for lin in range(N):
        print (Mundo[lin])   
    return 

def atualiza_percepcaoeagente(percebe, Mundo, agente):
    #alteraremos a nossa percepção com base no resultado que conseguiremos da função ação
    #conforme o agente escolher um novo local para se posicionar a matriz percepção substituira o -1 que estava na descrição, pelo o que está descrito no mundo
    percebe[agente[0]][agente[1]] = str(Mundo[agente[0]][agente[1]])
    
    return percebe

def imprime_percepcao(percebe, N): 
    for lin in range(N):
        print (percebe[lin])   
    return

def Acao(acao,agente, Estado,mundotxt, Mundo, N):
    #nesse primeiro bloco de funcoes colocarei a nova posicao caso o nosso agente queira se mover
         
     #no quarto devemos confirmar se ainda temos flecha e caso ainda tivermos devemos atirar a flecha no Wumpus
     #Qual a posição do Wumpus?
    posicao_Wumpus = mundotxt[2]
    #Para matarmos o Wumpus é necessario que a posicao da mira e do wumpus sejam a mesma
    miracima = int(agente[0]) - 1
    mirabaixo = int(agente[0]) + 1
    miradireita = int(agente[1]) + 1
    miraesquerda = int(agente[1]) - 1
    posição_Ouro = mundotxt[3]
    condicao = 1
    #função dedicada a pegar o ouro
    
    if ((acao =="M") and (agente[2] == ">")):
        agente[1] = agente[1] + 1
        agente[2] =  ">"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "M") and (agente[2] == "<")):
        agente[1] = agente[1] - 1
        agente[2] =  "<"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "M") and (agente[2] == "^")):
        agente[0] = agente[0] - 1
        agente[2] =  "^"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "M") and (agente[2] == "v")):
        agente[0] = agente[0] + 1
        agente[2] =  "v"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    #introduindo os parametros de choque
    elif ((acao =="M") and (agente[2] == ">") and (agente[1] == (N - 1))):
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]] + "c")
    elif ((acao == "M") and (agente[2] == "<") and (agente[1] == 1)):
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]] + "c")
    elif ((acao == "M") and (agente[2] == "^") and (agente[0]==1)):
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]] + "c")
    elif ((acao == "M") and (agente[2] == "v") and (agente[0] == (N - 1))):
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]] + "c")
        
    #nesse segundo bloco alterarei a direcao, girando o cursor em 90 graus no sentido horario do agente e manterei a posição a mesma
    elif ((acao =="D") and (agente[2] == ">")):
        agente[2] =  "v"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "D") and (agente[2] == "<")):
         agente[2] =  "^"
         Estado[3] -= 1
         print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "D") and (agente[2] == "^")):
         agente[2] =  ">"
         Estado[3] -= 1
         print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "D") and (agente[2] == "v")):
        agente[2] =  "<"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
        
    #nesse terceiro bloco alterarei a direcao, girando o cursor em 90 graus no sentido anti horario do agente e manterei a posicao a mesma
    elif ((acao =="E") and (agente[2] == ">")):
        agente[2] =  "^"
        Estado[3] -= 1
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "E") and (agente[2] == "<")):
         agente[2] =  "v"
         Estado[3] -= 1
         print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "E") and (agente[2] == "^")):
         agente[2] =  "<"
         Estado[3] -= 1
         print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "E") and (agente[2] == "v")):
        agente[2] =  ">"
        Estado[3] -= 1 
        print ("Percepcao apos a ultima acao:",Mundo[agente[0]][agente[1]])
    elif ((acao == "T") and (Estado[1] == 1) and (agente[2] == "^") and (posicao_Wumpus[0] == miracima) and (posicao_Wumpus[1] == agente[1])):
            Estado[1] = 0   
            Estado[0] = 0
            Estado[3] += 50 
            print ("Percepcao apos a ultima acao", Mundo[agente[1]][agente[0]] + "U")
         
    elif ((acao == "T") and (Estado[1]==1) and (agente[2] == "v") and (posicao_Wumpus[0] == mirabaixo) and (posicao_Wumpus[1] == agente[1])):
            Estado[1] = 0
            Estado[0] = 0
            Estado[3] += 50 
            print ("Percepcao apos a ultima acao", Mundo[agente[1]][agente[0]] + "U")
         
    elif ((acao == "T") and (Estado[1]==1) and (agente[2] == "<") and (posicao_Wumpus[0] == agente[0]) and (posicao_Wumpus[1] == miraesquerda)):
            Estado[1] = 0
            Estado[0] = 0
            Estado[3] += 50 
            print ("Percepcao apos a ultima acao",Mundo[agente[1]][agente[0]] + "U")
         
    elif ((acao == "T") and (Estado[1]==1) and (agente[2] == ">") and (posicao_Wumpus[0] == agente[0]) and (posicao_Wumpus[1] == miradireita)):
            Estado[1] = 0
            Estado[0] = 0
            Estado[3] += 50 
            print ("Percepcao apos a ultima acao", Mundo[agente[1]][agente[0]] + "U")
   #Caso você entre na mesma posicao do wumpus você perde -10000 pontos
    elif ((posicao_Wumpus[0] == agente[0]) and (posicao_Wumpus[1] == agente[1]) and (Estado[0] == 1)):
            Estado[3] -= 10000
            condicao = 0
    elif ((acao == "T") and (Estado[1]==0)):
            print ("Acabou as flechas") 
    elif ((acao == "G") and (agente[0] == posição_Ouro[0]) and  (agente[1] == posição_Ouro[1])):
            Estado[2] = 0
    #função que contabiliza os pontos se o agente sair da carvena
    elif ((acao == "S") and (agente[0] == (N - 1)) and  (agente[1] == 1) and (Estado[2] == 0) and (agente[3] =="v" or agente[3] =="<")) :       
            Estado[3] += 100
            condicao = 0
    resultado = [agente,Estado, condicao]
    
    return resultado

def criar_percebe(N):
    percebe = []
    for lin in range(N):
        linha = []
        for col in range(N):
            linha.append("?")
        percebe.append(linha)
    return percebe

def main ():
        
    entrada = "entrada.txt"

    l = mundo(entrada)
    N = int(l[0])
    mundotxt = le_mundo(l, N)
    Mundo = mundotxt[0]
    percebe = criar_percebe(N)
#nessa função eu vou definir a posição do meu agente, onde x representa a coluna e y a linha
    agente = [N-1,0,"^"]
#abaixo definirei uma lista de 4 elementos que nos informara se o monstro está vivo (1), ou não (0), se ainda possuimos flechas, indica se 
#ainda possuimos ouro para recolher e o tanto de ponto acumulado que possuimos
    Estado = [1,1,1,0]
    percepcao = atualiza_percepcaoeagente(percebe, mundotxt, agente)
#nas próximas linhas criarei
    print ("mundo do Wumpus conhecido pelo agente")
    imprime_percepcao(percepcao, N)
    #while o que vai fazer a gente sair do while é a saida do boneco ou a morte dele pelo wumpus com isso eu vou considerar que se o wumpus matar ou o agente sair, a condição
    #virará 1
    condicao = 0
    while condicao != 1:
        acao = input("Digite a acao desejada (M/T/D/E/G/S): ")
        novoagenteEstado = Acao(acao,agente, Estado,mundotxt, Mundo, N)
        agente = novoagenteEstado[0]
        Estado = novoagenteEstado[1]
        condição = novoagenteEstado[2]
        resultado = Acao(acao,agente, Estado,mundotxt, Mundo, N)
        agente = resultado[0]
        Estado = resultado[1]
        percebe = atualiza_percepcaoeagente(percebe, mundotxt, agente)
        print ("mundo do Wumpus conhecido pelo agente")
        imprime_percepcao(percebe, N)
          
    print("Mundo completo \n",mundotxt[0])
    print("Fim de jogo! Pontuação final: ",novoEstado[3])

if __name__=='__main__':
    main ()
