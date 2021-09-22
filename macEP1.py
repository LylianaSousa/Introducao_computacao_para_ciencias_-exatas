#------------------------------------------------------------------
#Nome: Lyliana Myllena Santos de Sousa
#NUSO: 11223740
## EP1: Cálculo das Notas Finais de MAC115
#------------------------------------------------------------------

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

Nalunos = int(input("Digite o numero de alunos da turma: "))
p1 = p2 = p3 = aprovados = reprovados = 0
i = 1
while i <= Nalunos:
    print ("Aluno ",i)
    freq = int(input("Digite a frequencia :"))
    p1 = int(input("Digite a nota da P1 :"))
    p2 = int(input("Digite a nota da P2 :"))
    p3 = int(input("Digite a nota da P3:"))
    Psub = int(input("Digite a nota da Psub: "))
    Ep1 = int(input("Digite a nota do EP1: "))
    Ep2 = int(input("Digite a nota do EP2: "))
    Ep3 = int(input("Digite a nota do EP3: "))
    
    if (p1<0):
        p1 = Psub
       
    elif (p2<0):
        p2 = Psub
           
    elif (p3<0):
        p3 = Psub
    
    print ("                                          ")
    P = (p1 + p2 + p3)//3
    print ("Media Provas: ",P)
    
    EP = (Ep1 + (2*Ep2) + (2*Ep3))//5
    print ("Media dos EPs: ", EP)
    
    MF = ((2*P) + EP)//3
    
    
    if (P >= 50) and (EP >= 50) and (freq >= 70):
        print ("Media final: ",MF)
        print ("Situacao: aprovado")
        aprovados += 1
        
    elif (P >= 50) and (EP >= 50) and (freq < 70):
        print ("Media final: ",MF)
        print ("Situacao: reprovado por falta")
        reprovados += 1
    
    
    elif (P <= 30) or (EP <= 30) and (freq < 70):
        print ("Media final: ",MF)
        print ("Situacao: reprovado por nota e falta")
        reprovados += 1
        
    elif (P <= 30) or (EP <= 30) :
        print ("Media final: ",MF)
        print ("Situacao: reprovado por nota")
        reprovados += 1
        
    elif (P > 30) and (P <50)  and (freq >= 70):
        print ("Media final: ",MF)
        Prec = int(input("Digite a nota da prova de recuperacao: "))
        MFRec = (MF + (2*Prec))//3
        if MFRec >= 50:
            print ("Media final apos recuperacao: ",MFRec)
            print ("Situacao:  Aprovado")
            aprovados += 1
        else:
            print ("Situacao: reprovado por nota")
            reprovados += 1
            
    elif (EP > 30) and (EP <50) and (freq >= 70):
        print ("Media final: ",MF)
        Prec = int(input("Digite a nota da prova de recuperacao: "))
        MFRec = (MF + (2*Prec))//3
        if MFRec >= 50:
            print ("Media final apos recuperacao: ",MFRec)
            print ("Situacao:  Aprovado")
            aprovados += 1
        else:
            print ("Situacao: reprovado por nota")
            reprovados += 1
    print ("***********************************************************")
    i += 1
        
print("Total de alunos aprovados: ", aprovados)
print ("TOtal de alunos reprovados: ", reprovados)

""" Quando o programa roda, ele nao apresenta nenhum tipo de problema. No
entanto, quando eu utilizo os dados do exemplo de execução, o programa 
exemplificado no paca mostra a media final do aluno, quando ele possui 
uma média final <50, como sendo a média das suas provas.
Como isso não foi explicado na descrição do exercicio, nao me atentei a
 esse detalhe e desenvolvi o programa do jeito que foi pedido.
"""