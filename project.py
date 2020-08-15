from mip import *
from itertools import product


def main():
    texto = []
    with open('instancia.txt') as arq:
        texto = arq.read()

    texto = texto.split()  # quebra os dados de acordo com os espaços
    texto_num = list(map(int, texto))  # Converte os numeros de string para inteiro

    t=texto_num[0] 
    cc1=texto_num[1] 
    cc2=texto_num[2] 
    CF=texto_num[3] 
    ecp1=texto_num[4]
    ecp2=texto_num[5]
    ecc1=texto_num[6]
    ecc2=texto_num[7]
    
    demanda=[0]*t
    for i in range(0,t+1):
        if(i==t):
            horas=texto_num[i+8]
        else:
            demanda[i]=texto_num[i+8]

    print("\n-----Dados de Entrada--------")
    print("  Semanas:",t, "   CF:",CF)
    print("  Cc1:",cc1, "     Cc2:", cc2)
    print("  ep1:", ecp1, "     ep2:", ecp2)
    print("  ec1:", ecc1, "      ec2:", ecc2)
    print("  Demanda:",  demanda)
    print("  Horas/s:", horas)
    print("----------------------------")

    # cria um problema de Programação Linear Inteiro 
    # Misto vazio com configurações padrão
    m = Model(sense=MINIMIZE, solver_name=CBC) 
    #otimização é definido como Minimizar

    #Variáveis ​​de decisão são adicionadas ao modelo   
    p1 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    p2 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    c1 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    c2 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    ep1 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    ep2 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    ec1 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    ec2 = [ m.add_var(var_type=INTEGER, lb=0, ub=INF) for i in range(t) ]
    Y = [ m.add_var(var_type=BINARY) for i in range(t) ]

# [START constraints]
    for i in range (0, t):
        if(i!=0):
            #[Restrição de estoque de P1]
            m += ep1[i]  == p1[i] - demanda[i] + ep1[i-1]
            #[Restrição de estoque de P2]
            m += ep2[i]  == p2[i] - 2*p1[i] + ep2[i-1]
            #[Restrição de estoque de C1]
            m += ec1[i]  == c1[i] - 3*p1[i] - p2[i] + ec1[i-1]
            #[Restrição de estoque de C2]
            m += ec2[i] == c2[i] - 2*p2[i]  + ec2[i-1]
            #[Restrição de  compra]
            m+=c1[i]+c2[i]<=((3*demanda[i]+ 2*demanda[i]+4*demanda[i])*Y[i])    
        else:
            #[Restrição de estoque de P1]
            m += ep1[0] == p1[0]-demanda[0]
            #[Restrição de estoque de P2]
            m += ep2[0] == p2[0]-2*p1[0]
            #[Restrição de estoque de C1]
            m += ec1[0] == c1[0] - 3*p1[0] - p2[0]
            #[Restrição de estoque de C2]
            m += ec2[0] == c2[0] - 2*p2[0] 
            m+= Y[0]==1         
    for i in range (0,t):
        #[Restrição de  demanda do Produto por semana]
        m += p1[i]  >= demanda[i]
        #[Restrição de Tempo de Fabricação do produto]
        m += p1[i]+p2[i] <= horas
# [END constraints]
    
#Função objetivo
    m.objective = minimize(
                  ecp1*xsum(ep1[i] for i in range(0,t)) + 
                  ecp2*xsum(ep2[i] for i in range(0,t)) +
                  ecc1*xsum(c1[i] for i in range(0,t)) + 
                  ecc2*xsum(c2[i] for i in range(0,t)) + 
                  CF*xsum(Y[i] for i in range(0,t)))

    print(m.objective)

    m.write('model.lp')
    m.optimize()

    print('model has {} vars, {} constraints and {} nzs'.format(m.num_cols, m.num_rows, m.num_nz))

    print ("\n\n****************************************************************************************************")
    print ("                                           Solucao   ")
    print ("****************************************************************************************************\n")
    linha=[0]*t
    for i in range (t):
        linha[i]=i+1
    print('        {:^7}   {:>7}     {:>7}     {:>7}      {:>7}     {:>7}     {:>7}    {:>7}'.format(*linha))


    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")
    for i in range(0,t):
        linha[i] = p1[i].x
    print("P1  | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))

    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = ep1[i].x
    print("Ep1 | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))


    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = p2[i].x
    print("P2  | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))


    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = ep2[i].x
    print("Ep2 | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))



    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = c1[i].x
    print("C1  | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))


    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = ec1[i].x
    print("Ec1 | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))



    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = c2[i].x
    print("C2  | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))

   

    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = ec2[i].x
    print("Ec2 | ", '{:^9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}   {:>9,.2f}'.format(*linha))


    for i in range(len(demanda)+1):
        print("-----------", end="")
        if(i==(len(demanda))):
            print("-")  
    for i in range(0,t):
        linha[i] = Y[i].x
    print("Y   | ", '{:^9}   {:>9}   {:>9}   {:>9}   {:>9}   {:>9}   {:>9}   {:>9}'.format(*linha))

    


    
    
main()
    