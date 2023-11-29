import os

def glob(tipo):
    if tipo == 1:
        cores = [
        '\33[92m',
        '\33[92m',
        '\33[32m',
        ]
    if tipo == 2:
        cores = [
        '\033[1;50;91m',
        '\033[1;0;91m',
        '\033[0;31m',
        ]
    if tipo == 3:
        cores = [
        '\033[1;97',
        '\033[97m',
        '\033[0;37m',
        ]
    if tipo == 33:
        cores = [
        '\033[0;97m',
        '\033[97m',
        '\033[37m',
        ]
        
    reset_cor = '\033[0m'

    texto = """
                  ....::::::....
                  7??5GGGGGG5??7.
          .^^^~!!7555G######G555~^^^^^:.
          :JYYPBBBBBB#&&&&&&#BGGYJJJJJ?:
       ~77JPGG#&&&&&&#BBBBBBBGGGGPP5J??^...
       75YPGGB#@&&&&&#GGGGGGGGGGGGBPYJJ~::.
       JGGGGGG#@@@@@&#GGGGGGGGGGGGGGGGPJ!!^
      .YGGGGGG#######BGGGGGGGGGGGGGGGGGJ!!~.
    .::YGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGJ!!~::..
   .!!75GGGGGGGGGGGGGB######BGGGGGGGGGGJ!!!~~~.
   :?JJPGGGGGGGGGGGGG#&&&&&&#GGGGGGGGGPJ!!!77!:
   :??JPGGGGGGGGGGGGG#&&&&&&#GGGGGGPYYY?!!7???:
   :7775PPPGGGGGGGGGGB######BGGGGGG5J??7!!!777:
   .^~~7??YGGGGGGGGGGGGGGGGGGGGGGGB57!!!!!!~~^.
    ...!??JJJY555PGGGGGGGGGGP555YJY?7!!777!...
       ~??7!!!?YJYGGGGGGGGGG5YJJ7!!!!!!7??!
       .^:~!!!7777JJJJJJJ???7777!!!!!!!!~~^
       ...:~!!!!!7???????!!!!!!!!!!!!!!^::.
           .::~777?J?7!!!!!!!!!!777!~~^.
            ...:::~~~!!!!!!!~~^^::::...
                  ..:^!!!!!!^:..
                      ......
    """
    linhas = texto.split('\n')
    os.system("clear")
    for i, linha in enumerate(linhas):
        tamanho = len(linha)
        metade = tamanho // len(cores)
        for j, cor in enumerate(cores):
            parte = linha[j * metade : (j + 1) * metade]
            print(f'{cor}{parte}', end='')
        print()
    print("                        vBeta")
    print("                        ©️ Copyright 2023-2024")
        
import time,subprocess

def tim(tt):
    min = (tt//60)
    ss = (tt%60)
    if min > 0:
        return f"{min}min {ss}s"
    elif ss > 0:
        return f"{ss}s"
    else:
        return "0s"

def carregar_modulos(pacotes):
    os.system("clear")
    glob(3)
    print(f"\n      Developer: From\n      Discord: fromdev#0\n\n      Verificando Módulos...\n\033[0m")
    for pacote in pacotes:
        try:
            modulo = __import__(pacote)
            globals()[pacote] = modulo
            print(f"      Módulo \033[97m{pacote}\033[37m já está importado.")
        except ImportError:
            try:
                resultado = subprocess.check_output(['pip', 'show', pacote])
                print(f"      Módulo \033[97m{pacote}\033[37m já está instalado.")
            except subprocess.CalledProcessError:
                print(f"      Módulo \033[97m{pacote}\033[37m está sendo instalado.")
                resultado = os.system(f'pip install {pacote}')
                if resultado != 0:
                    print(f"      Falha ao instalar o módulo {pacote}.")
    os.system("clear")
    glob(33)
    print(f"\n      Developer: From\n      Discord: fromdev#0\n\n      Todos os módulos estão instalados.\n      Sistema sendo Iniciado...\033[0m")
    time.sleep(1.25)
    
carregar_modulos(["time","whois","socket","http.client","requests"])
import socket,http.client,requests,whois
def menu(tipo):
    if tipo == 1:
        print("      Developer: From")
        print("      Discord: fromdev#0")
        print("      MENU: Principal\n")
        print("2 - Consulta")
        print("1 - Atualizações")
        print("0 - Sair")
    elif tipo == 2:
        print("      MENU: Consulta\n")
        print("2 - Consultar IP")
        print("1 - Consultar Site")
        print("0 - Voltar")
    else: 
        print("      MENU: Inválido")
        print("\n0 - Voltar\n\nOcorreu um erro ao tentar carregar este menu, informe ao programador do sistema.")

def consulta_info(nome):
    try:
        info = whois.whois(nome)
        if 'name' in info and info['name'] is None:
            input("\n        Domínio inválido, Pressione Enter para voltar.\n")
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
            print("\n        Carregado!\n")
            if 'name' in info and info['name'] is not None:
                try:
                    print(" Nome:", info['name'])
                except Exception as e:
                    print("Nenhum nome Encontrado")
            if 'domain_name' in info and info['domain_name'] is not None:
                try:
                    print(" Domínio:", info['domain_name'])    
                except Exception as e:
                    print(" Nenhum domínio Encontrado.")
            if 'email' in info and info['email'] is not None:
                print(" Gmail:", info['email'])
            if 'creation_date' in info and info['creation_date'] is not None:
                try:
                    print(" Registro:", info['creation_date'][0])
                except Exception as e:
                    print(" Data de Registro não Encontrado.")
            if 'expiration_date' in info and info['expiration_date'] is not None:
                try:
                    print(" Expiração:", info['expiration_date'][0])
                except Exception as e:
                    print(" Data de Expiração não Encontrado.")
            if 'updated_date' in info and info['updated_date'] is not None:
                try:
                    print(" Atualização :", info['updated_date'][0])
                except Exception as e:
                    print(" Data de Atualização não Encontrado.")
            if 'name_servers' in info and info['name_servers'] is not None:
                try:
                    print(" Servidores:\n  ", '\n   '.join(info['name_servers']))
                except Exception as e:
                    print(" Nenhum servidor Encontrado.")
            dominio_menu(info['name_servers'])
    except Exception as e:
        print("        Ocorreu um Erro:", e)
        input("        Pressione Enter para voltar.\n")

def consulta_info2(endereco):
    try:
        url = f'http://ip-api.com/json/{endereco}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query'
        response = requests.get(url)
        data = response.json()
        if data['status'] == "fail":
            print("\n        IP inválido")
            input("        Pressione Enter para voltar.\n")
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
            print("\n        Carregado!\n")
            print(" Status:",data['status'])
            print(' IP:', data['query'])
            print(' Proxy:', data['proxy'])
            print(' Host:', data['hosting'])
            print(' Domínio:', data['reverse'])
            print(' Organização:', data['org'])
            print(' Cidade:', data['city'])
            print(' Região:', data['regionName'],' (',data['region'],')')
            print(' Código Postal:', data['zip'])
            print(' Horário:', data['timezone'])
            print(' Continente:',data['continent'],' (',data['continentCode'],')')
            print(' País:', data['country'],' (',data['countryCode'],')')
            print(' Moeda:',data['currency'])
            print(' Latitude:', data['lat'])
            print(' Longitude:', data['lon'])
            endereco_menu(endereco)
    except Exception as e:
        print("        Ocorreu um Erro:", e)
        input("        Pressione Enter para voltar.\n")

def consulta_dominio(nome):
    os.system("clear")
    os.system("clear")
    glob(1)
    print("\n        Carregando...")
    consulta_info(nome)
       
def consulta_endereco(endereco):
    os.system("clear")
    os.system("clear")
    glob(1)
    print("\n        Carregando...")
    consulta_info2(endereco)
                
def dominio_menu(servidor):
    while True:
        print("\n2 - Consultar novamente")
        print("1 - Status dos servidores")
        print("0 - Voltar")
        dom = input("\n> ")
        
        if dom == "2":
            consultar_site()
            break
        elif dom == "1":
            os.system("clear")
            os.system("clear")
            glob(1)
            dominio_servidores(servidor)
            break
        elif dom == "0":
            os.system("clear")
            os.system("clear")
            break
            menu(2)
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
                
def endereco_menu(ip):
    while True:
        print("\n1 - Consultar novamente")
        print("0 - Voltar")
        enc = input("\n> ")
        
        if enc == "1":
            consultar_endereço()
            break
        elif enc == "0":
            os.system("clear")
            os.system("clear")
            break
            menu(2)
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
    
def dominio_servidores(servidor):
    while True:
        print("\n    Tipos de Conexões\n")
        print("3 - Longo [5s]")
        print("2 - Mediano [2.5s]")
        print("1 - Curto [1s]")
        print("0 - Voltar")
        dom = input("\n> ")
        
        if dom == "3":
            dom_servidores(servidor, 3)
            break
        elif dom == "2":
            dom_servidores(servidor, 2)
            break
        elif dom == "1":
            dom_servidores(servidor, 1)
            break
        elif dom == "0":
            os.system("clear")
            os.system("clear")
            menu(2)
            break
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
            
def dom_servidores(servidor, tt):
    os.system("clear")
    glob(1)
    tempo = 0
    if tt == 3:
        tempo = 5
    elif tt == 2:
        tempo = 2.5
    elif tt == 1:
        tempo = 1
    else:
        tempo = 1
    print("\n Tempo Estimado:", tim((len(servidor) * tempo)))
    print(" Total:", len(servidor))
    print(" Servidores:\n ", ', '.join(servidor), "\n")
    for server in servidor:
        try:
            socket.create_connection((server, 53), timeout=int(tempo))
            print(f"     \033[92m+ {server} \033[32mIP: {socket.gethostbyname(server)}\033[32m")
        except socket.error as e:
            print(f"     \033[91m× {server}")
    input("\033[32m\n        Pressione Enter para voltar.")
    
def consultar_site():
    os.system("clear")
    os.system("clear")
    glob(1)
    dominio = input("\n0 - Voltar\n\n   Domínio: ")
    if dominio == "0":
        menu(2)
    else:
        consulta_dominio(dominio)
    
def consultar_endereço():
    os.system("clear")
    os.system("clear")
    glob(1)
    endereco = input("\n0 - Voltar\n\n   IP: ")
    if endereco == "0":
        menu(2)
    else:
        consulta_endereco(endereco)

def atualizacoes():
    print("\n Ultima Atualização feita Em: 29/11 10:32")
    print("  √ = Feito\n  ~ = Pendente\n  × = Futuramente")
    print("\n     Novidades")
    print(" √ Novo menu de Atualizações")
    print(" ~ Menu de Info CPF (consulta)")
    print(" ~ Menu de Info Minecraft (consulta)")
    print(" × Novo Menu de Utilidades")
    at = input("\n0 - Voltar\n> ")
    if at == 0:
        main()
    else:
        os.system("clear")
        os.system("clear")
        glob(1)
        print("\n Ultima Atualização feita Em: 29/11 10:32")
        print("  √ = Feito\n  ~ = Pendente\n  × = Futuramente")
        print("\n     Novidades")
        print(" √ Novo menu de Atualizações")
        print(" ~ Menu de Info CPF (consulta)")
        print(" ~ Menu de Info Minecraft (consulta)")
        print(" × Novo Menu de Utilidades")
            
def main():
    while True:
        os.system("clear")
        os.system("clear")
        glob(1)
        menu(1)
        opcao_principal = input("\n>  ")
        if opcao_principal == "2":
            while True:
                os.system("clear")
                os.system("clear")
                glob(1)
                menu(2)
                opcao_consulta = input("\n>  ")
                if opcao_consulta == "2":
                    os.system("clear")
                    os.system("clear")
                    glob(1)
                    consultar_endereço()
                elif opcao_consulta == "1":
                    os.system("clear")
                    os.system("clear")
                    glob(1)
                    consultar_site()
                elif opcao_consulta == "0":
                    break
                else:
                    print(" ")
        elif opcao_principal == "1":
            os.system("clear")
            os.system("clear")
            glob(1)
            atualizacoes()
        elif opcao_principal == "0":
            os.system("clear")
            os.system("clear")
            glob(2)
            print("\033[0;31mPrograma Finalizado.\033[0;0m")
            break
        else:
            print(" ")
if __name__ == "__main__":
    main()
