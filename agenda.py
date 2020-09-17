
def adicionar(lista): 
    nome = input("Digite o nome: ")
    tel =  input("Digite o número: ")   
    if nome == "" or tel == "":
        print("O campo nome ou telefone está vazio.Por favor preencha novamente.")
        adicionar(lista)
    else:
        contato = "Nome:"+nome +"   Número:"+ tel  
        lista.append(contato)
        lista.sort()
        print("\nContato inserido com sucesso!")  
    
    
def consultar(lista):
    if lista != [] :
        nome2 = input("Informe o nome do contato: ")
        tamanho = len(lista)
        for i in range(tamanho):
            if nome2 in lista[i]:
                print("\nContato encontrado!")
                print(lista[i])  
            elif not nome2 in lista[i]:
                print("Não encontramos esse nome")
                
    else:
        print("Sua agenda está vazia!")
        
        
def excluir(lista):
    if lista!= []:
        tamanho = len(lista)
        for i in range(tamanho):
            print(i, "-",lista[i])
        
        deleta = int(input("\nEscolha o índice do contato que deseja excluir: "))
        if deleta > tamanho:
            print("Índice inválido")
        else:
            lista.pop(deleta)
            print("\nContato excluido com sucesso!")
    else:
        print("\nSua agenda está vazia!")


def listar(lista):  
    if lista != []:
        tamanho = len(lista)
        for i in range(tamanho):
            print(i, "-",lista[i])
        print("\n")
    else:
        print("\nSua agenda está vazia!")
       

def zerar(lista):
    lista.clear()
    print("\nAgenda zerada com sucesso!")
    print("\n")


def principal():   
     lista = []
     while True:
        print("#--------------------------------------------#")
        print("#     A G E N D A  D E  C O N T A T O        #")
        print("#--------------------------------------------#")
        print("# OPÇÕES                                     #")
        print("# 1 – CADASTRAR NOME                         #")
        print("# 2 – CONSULTAR NOME                         #")
        print("# 3 – EXCLUIR NOME                           #")
        print("# 4 – LISTAR TODOS NOMES                     #")
        print("# 5 – ZERAR AGENDA                           #")
        print("# 6 – SAIR                                   #")
        print("#--------------------------------------------#")
        opcao = input("DIGITE A OPÇÃO DESEJADA (1 A 6): ")
        
        
        if (opcao == "1"):
            adicionar(lista)
            
        elif(opcao == "2"):
            consultar(lista)
            
        elif(opcao == "3"):
            excluir(lista)
            
        elif(opcao == "4"):
            listar(lista)
            
        elif(opcao == "5"):
            zerar(lista)        
            
        elif(opcao == "6"):
            print("\nPrograma finalizado")
            break
            
        else:
            print("Opção inválida")
          
principal()