#Nome: Lyliana Myllena Santos de Sousa
#NUSP: 11223740
#Codigo da disciplina: MAC 115
#Nome do professor: Flávio

#Defino primeiramente uma função fatorial para nos auxiliar na montagem da função que aproxima cos
def fatorial (m):
    f=1
    i=m
    while i>0:
        f=f*i
        i-=1
    return f

#Crio tambem uma funcao para obter os valores de uma funcao exponencial, onde v e o nosso valor e E o expoente
def exp(V,E):
    resultado = 1
    while E >= 1:
            resultado = V*resultado           
            E -= 1
    return resultado

#crio a funcao aproximaCOS que me retorna uma lista com o valor aproximado do cosseno e a ordem da aproximacao
def aproximaCOS(x,e):
    j=1
    soma=1
    controle_e = True
    while controle_e==True:
       #soma da serie infinita
       soma += (exp((-1)*(exp(x,2)),j))/(fatorial(2*j))
       #nessa parte eu colocarei a condição relacionada e, que nos mostra até que ordem vai a nossa serie de taylor
       #no enunciado do ep observamos que os valores de x inseridos na função são sempre positivos, pois o valor de k vai de zero até
       #logo antes de pi sobre dois, logo economizarei tempo nessa etapa analisando os valores de x sempre positivos, logo sem o modulo
       e1 = exp(x,(j-1)*2)/fatorial((j-1)*2)
       e2 = (exp(x,(2*j)))/fatorial(2*j)
       #definimos as variaveis acima para nos auxilixar na vizualizacao da condicao para que a soma dos quadrados continue acontecendo
       if e1 >= e and e2 < e:
           controle_e = False
       else:
           controle_e = True
           j+=1
       #transformei os dois valores obtidos em uma lista e coloquei ela como o nosso return, onde o valor de j será multiplicado por dois
       #porque o j da aproximação não é o valor da ordem da sua aproximação, e sim o valor de j multiplicado por dois, que e o verdadeiro 
       #resultado da ordem de aproximação, no entanto, só multiplicaremos o valor de j ao final
       listaaproximacos = [soma,j]
    return listaaproximacos

#utilizo a função que aproxiamcos para obter os valores das alturas dos retagulos
def integral_por_retangulos(k,e,d):
    n=1
    Integral=0
    controle_n = True
    #crio um while para aproximar os valores da integral pela somatoria da area dos quadrados, onde apartir do momento que o valor
    #de n vezes o delta utilizado for menor ou igual a k e o valor de n mais 1 vezes k for maior que k
    while controle_n == True:
        #considero a nossa cvariavel X o algumento da nossa função cosseno, que fornecerá a altura do nossso retangulo, que ao multiplicarmos por delta
        #nos fornecera a area do triangulo
        X = n*d
        a = aproximaCOS(X,e)
        # o valor de a[0] corresponde ao valor aproximado do angulo
        Integral = Integral + d*a[0]
        if (n*d<=k) and ((n+1)*d>k):
            controle_n = False
        else:
            controle_n = True
            n+=1
    #crio uam lista que fornece o valor aproximado do cos em um certo ponto, o numero de quadrados utilizados,
    #e o valor de a[1] representa a ordem da aproximacao
    listaintegral=[Integral, n,a[1]]
    return listaintegral
#crio essa funcao para com base no valor de p, encontrar o valor de d/2^m se adapta melhor as variaveis que forneceremos
def aproximacao_suficiente(k,e,d,p):
    m = 1
    controle_m = True
    while controle_m == True:
        delta1 = d/(exp(2,m))
        delta0 = d/(exp(2,(m-1)))
        I1 = integral_por_retangulos(k,e,delta1)        
        i1 = I1[0] #esse é o valor aproximado da integral pelo metodo dos retângulos
        I0 = integral_por_retangulos(k,e,delta0)
        i0 = I0[0] #esse é o valor aproximado da integral pelo metodo dos retângulos
        # etapa devo vetifica se o modulo das diferenças é menor ou igual a o p fornecido, para resolver esse resultado vou considerar que ao 
        #elevarmos ao quadrado os dois lados da desigualdade, obteremos ambos os lados positivos e isso não interferirá nos resultados obtidos, pois
        #estaremos ralizando uma mesma operação nos dois lados da desiguldade
        if exp(i0-i1,2) <= exp(p,2):
            controle_m = False
        else:
            controle_m = True
            m += 1
    areaintegral = integral_por_retangulos(k,e,delta1)
    #por fim eu utilizo a funcao integral por retangulos para definir a lista acima, que me fornece os valores da integral caulcada, do numero 
    #de retangulos e da ordem de aproximacao
    
    #Abaixo defino a lista integral e nos fornece respectivamente os valores de m (valor da potencial de dois, que ao dividir o valor de delta
    #fornecido nos diz o intervalo de comprimento do nosso controle de qualidade), o valor de delta1 que obtemos pelo controle de qualidade,
    #o valor areaintegral[0] que aproxima o valor da integral, o areaintegral[1] que fornece  numero de retangulos utilizados e o valor areaintegral[2]
    #que fornece a ordem de aproxiamacao por taylor
    integral = [m,delta1, areaintegral[0],areaintegral[1], areaintegral[2]]
    return integral

#nesse bloco de comando perguntarei ao usuário os valores das icognitas
def main ():
   print ("OLá")
   k = float(input("Digite o valor de K(limite de integracao):"))
   e = float(input("Digite o valor de e (seu erro máximo na funcao cos):"))
   d = float(input("Digite o valor de d (seu tamanho máximo de intervalo de aproximacao):"))
   p = float(input("Digite o valor de p (o erro máximo na aproximacao da integral)"))

   RESULTADOS = aproximacao_suficiente(k,e,d,p)
   print("Feito os calculos! O valor aproximado para a sua integral é de",RESULTADOS[2])
   print("Os valores que produziram essa aproximação foram:")
   print("m = ",RESULTADOS[0],", isso é intervalos de comprimento d/2^",RESULTADOS[0],";")
   print("n= ",RESULTADOS[3],", retangulos bem pequenos;")
   print("p = ",2*RESULTADOS[4],"isso e, cosseno foi aproximado ate Taylor de ordem",2* RESULTADOS[4])
 
if __name__=='__main__':
    main ()

#Conversei com um gruo da minha sala, e ambos os grupos chegaram a resultados divergente dos que foram fornecidos no exemplo de saida, onde o taylor estava 
#com uma ordem com diferencaa de -2 entre o dos alunos e do exemplo de saida, ou que os valores de n pareciam estar smepre dividido por dois em comparacao 
#com o exemplo de saida