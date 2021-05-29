# manipulação de arquivos
class arquivo:
    def __init__(self,nome_arq):
        self.nome_arq = nome_arq
        self.arq = open(self.nome_arq)  # arquivo deve preexistir
        self.n =- 1 # indica a quantidade de qbits da simulação
        self.vezes = -1
        self.entrada = []
        self.monta_comandos()

    ## executa comandos do arquivo
    def monta_comandos(self):
        info = self.arq.readline().split() # Armazena a primeira linha
        
        ## A primeira linha do arquivo deve seguir o modelo:
        
        #   Program n t Matrix = bool
        
        # n = a quantidade de qbits do circuito, t = número de medições
        # bool = boleano que indica se a saída será a matriz resultante do circuito
        # Por default "Matrix = False", não sendo obrigatório escrever essa parte
         
        # O arquivo pode conter linhas e espaços no início da linha em branco 
        # só pode ser escrito um comando por linha
        
        ## A última linha do arquivo deve seguir o modelo:
        
        #   medir(cbits)

        # cbits = vetor que indica a ordem da medição dos bits.
        
        if  len(info) != 0:
            # verifica se a saída será a matriz resultante
            if len(info) > 3:
                if info[-1].strip("=") == "True": 
                    self.matrix = True
                elif info[-1].strip("=") == "False":
                    self.matrix = False
                else:
                    print("Valor booleano inválido!")
            else:
                self.matrix = False
            self.n = int(info[1])
            self.vezes = int(info[2])
            self.entrada = self.arq.readlines()
            self.comandos = []  # vetor dos comandos
            self.variaveis = {} # dicionário que contém as variáveis 
            self.funcoes = []   # vetor das funções
        else:
            print("arquivo vazio ou inexistente!")

        # verifica o conteúdo de cada linha
        inclui = False
        func = False
        for linha in self.entrada:
            linha = linha.strip()
            if len(linha) > 0:    # linha de comentário
                if linha[0]!="#" and linha[0]!="{": # linha de comentário 
                    
                    # laço de repefição for
                    # modelo:
                    
                    # for var = inicio to fim{
                    #    ...
                    #}
                    
                    # var = nome da variável do laço, inicio = número inicial, fim = número final
                    if linha[:3] == "for": 
                        linha = linha.strip("{")
                        linha =  linha.split('=')
                        for_variavel = linha[0].split()[-1]
                        for_inicio = int(linha[1].split()[0])
                        for_final = int(linha[1].split()[-1])
                        bloco=[]
                        inclui = True
                   
                    # Definição de função
                    # modelo: 
                    
                    #func(nome,variaveis){
                    #   ...
                    #}
                    
                    elif linha [:4] ==  "func":
                        linha = linha.split("(")
                        nome = linha[0].split()[1] # nome da função
                        linha[1] = linha[1][:-2]
                        variaveis_func = linha[1].split(",") # vetor de variaveis da função
                        func_bloco = [] # bloco de comando da função
                        func = True
                    
                    # Declaração de variável
                    # modelo:
                    
                    # int nome = valor
                
                    # Só são aceitas variáveis inteiras
                    elif linha[:3] == "int":
                        nome,valor = linha.split('=')
                        nome,valor = nome.strip(),valor.strip()
                        nome = nome.split()
                        self.variaveis[nome[1]] = int(valor)
                     
                    # Declaração de variável
                    # modelo:
                    
                    # float nome = valor
                    
                    # Só são aceitas variáveis float
                    elif linha[:5] == "float":
                        nome,valor = linha.split('=')
                        nome,valor = nome.strip(),valor.strip()
                        nome = nome.split()
                        self.variaveis[nome[1]] = float(valor)
                    
                    # fechamento da função
                    elif linha[:] == "}" and not inclui:
                        self.funcoes.append(funcao(nome,variaveis_func,func_bloco))
                        func = False
                        
                    # fechamento do laço de repetição
                    elif linha[:] =="}":
                        for i in range(for_inicio,for_final):                    
                            if func:    
                                for comando in bloco:
                                    if for_variavel in comando:
                                        comando = comando.replace(for_variavel,i)
                                    self.func_bloco.append(comando)
                            else:
                                for comando in bloco:
                                    if for_variavel in comando:
                                        comando = comando.replace(for_variavel,str(i))
                                    self.comandos.append(comando)
                        inclui = False
                              
                    elif inclui :
                        bloco.append(linha)
                        
                    elif func:
                        func_bloco.append(linha)
                    
                    else :
                        self.comandos.append(linha)


# Criação de funções, em progresso
# Ainda não funciona para todos os casos        
# No futuro talvez seja interessante criar um arquivo próprio
class funcao:
    def __init__(self,nome,variaveis,codigo):
        self.nome = nome
        self.variaveis = variaveis
        self.codigo = codigo

            