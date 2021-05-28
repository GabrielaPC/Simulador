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
        info = self.arq.readline().split()
        
        if  len(info) != 0:
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
            self.comandos = []
            self.variaveis = {}
            self.funcoes = []
        else:
            print("arquivo vazio ou inexistente!")

        #print(self.entrada)
        # verifica o conteúdo de cada linha
        inclui = False
        func = False
        for linha in self.entrada:
            linha = linha.strip()
            if len(linha) > 0:    # linha de comentário
                if linha[0]!="#" and linha[0]!="{": # linha de comentário 
                    
                    if linha[:3] == "for":
                        linha = linha.strip("{")
                        linha =  linha.split('=')
                        for_variavel = linha[0].split()[-1]
                        for_inicio = int(linha[1].split()[0])
                        for_final = int(linha[1].split()[-1])
                        bloco=[]
                        inclui = True
                    
                    elif linha [:4] ==  "func":
                        linha = linha.split("(")
                        nome = linha[0].split()[1]
                        linha[1] = linha[1][:-2]
                        variaveis_func = linha[1].split(",")
                        func_bloco = []
                        func = True
                         
                    elif linha[:3] == "int":
                        nome,valor = linha.split('=')
                        nome,valor = nome.strip(),valor.strip()
                        nome = nome.split()
                        self.variaveis[nome[1]] = int(valor)
                    
                    elif linha[:] == "}" and not inclui:
                        self.funcoes.append(funcao(nome,variaveis_func,func_bloco))
                        func = False
                    
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
