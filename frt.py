import os,time,subprocess
def msg(tipo,msg):
    if tipo == 1:
        cores = ['\33[38;5;53m','\33[38;5;54m','\33[38;5;55m','\33[38;5;56m','\33[38;5;57m']
    elif tipo == 2:
        cores = ['\33[38;5;53m','\33[38;5;54m','\33[38;5;55m','\33[38;5;56m','\33[38;5;57m']
    else:
        cores = ['\33[38;5;18m','\33[38;5;25m','\33[38;5;32m','\33[38;5;33m','\33[38;5;39m']
    linhas = msg.split('\n')
    for i, linha in enumerate(linhas):
        tamanho = len(linha)
        metade = tamanho // len(cores)
        for j, cor in enumerate(cores):
            parte = linha[j * metade : (j + 1) * metade]
            print(f'{cor}{parte}',end='')
        print()
def glob(tipo):
	msg(tipo,f"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠚⠉⣉⣭⣭⣭⣉⣉⣑⠒⠦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠓⠢⣌⡑⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⣈⠻⣏⠉⠉⠉⠉⠙⠓⠦⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠆⠙⢆⠀⠀⠀⠀⠀⠀⠙⢆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠘⡆
⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠂⠀⠀⠀⣸⢀⠇
⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠞⠁⠀⠀⠀⣰⢃⡞⠀
⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠋⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠊⠁⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⠀⣠⠾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⢀⡤⠺⡇⠀⠀⠀⠀⠀
⠀⠀⢠⠞⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠉⠀⢸⠁⠀⠀⠀⠀⠀
⠀⣰⠋⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡤⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠞⠁⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀
⢀⡇⠀⠀⠀⠀⠀⣷⣀⣀⣤⡤⠤⠴⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀
⠈⡞⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣜⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠴⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠲⢭⣗⣂⣀⣀⣀⣀⣀⣠⣤⠤⠴⠒⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢎⡤⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁⠀⠙⠲⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⣩⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⠤⣀⣀⡀⠀⠀⠀⣀⣀⣀⡤⠴⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

""")
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
    glob(00)
    print("\n      Developer: From\n      Discord: fromdev#0\n\n      Verificando Módulos...\n")
    for pacote in pacotes:
        try:
            modulo = __import__(pacote)
            globals()[pacote] = modulo
            print(f"      Módulo {pacote} já está importado")
        except ImportError:
            try:
                __import__(pacote)
                print(f"      Módulo {pacote} já está instalado")
            except Exception:
                print(f"      Módulo {pacote} está sendo instalado")
                resultado = os.system(f'pip install {pacote}')
                if resultado != 0: 
                    print(f"      Falha ao instalar o módulo {pacote}")
    os.system("clear")
    glob(00)
    print(f"\n      Developer: From\n      Discord: fromdev#0\n\n      Todos os módulos estão instalados.\n      Sistema sendo Iniciado...")

carregar_modulos(["sys","time","pytz","datetime","socket","http.client","requests"])
import socket
import http.client
import requests
import pytz
from datetime import datetime
import whois

def menu(tipo):
    if tipo == 1:
        print("      Developer: From")
        print("      Discord: fromdev#0")
        print("      MENU Principal\n")
        print("2 - Consulta")
        print("1 - Atualizações")
        print("0 - Sair")
    elif tipo == 2:
        print("      MENU Consulta\n")
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
            print(" Status:",data['status'],"\n")
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
            print(f"     + {server} {socket.gethostbyname(server)}")
        except socket.error as e:
            print(f"     × {server}")
    input("\n        Pressione Enter para voltar.\n")
    
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
    print("\n     Carregando...\n")
    response = requests.get("https://api.github.com/repos/fromofca/Frt")
    os.system("clear")
    glob(1)
    print("\n     Carregado, Aguarde alguns instantes!\n")
    while True:
        if response.status_code == 200:
            commits_url = response.json()["commits_url"].split("{")[0]
            commits_response = requests.get(commits_url)
            if commits_response.status_code == 200:
                commits = commits_response.json()
                if len(commits) > 0:
                    latest_commit_time = commits[0]["commit"]["committer"]["date"]
                    timezone = pytz.timezone('America/Sao_Paulo')
                    commit_datetime = datetime.strptime(latest_commit_time, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
                    commit_datetime = commit_datetime.astimezone(timezone)
                    formatted_time = commit_datetime.strftime("%d/%m/%Y ás %H:%M:%S")
                    os.system("clear")
                    glob(1)
                    print(" Ultima Alteração feita Em:", formatted_time)
                else:
                    os.system("clear")
                    glob(1)
        print(" Versão do Sistema: v0.25\n")
        print("     Bugs")
        print(" [29/11] Menu de sair do sistema resolvido")
        print(" [29/11] Menu de voltar das atualizações")
        print(" [29/11] Menu de Consutar IP resolvido (consulta)")
        print("\n     Alterações")
        print(" [30/11] Novas cores pro sistema")
        print(" [30/11] Novo layout pro sistema")
        print(" [29/11] Código de execução com menos delay")
        print(" [29/11] Menu de carregamento com menos delay")
        print("\n     Novidades")
        print("\n  + = Feito\n  % = Pendente\n")
        print(" + [29/11] Novo menu de Atualizações (principal)")
        print(" % Menu de Info CPF (consulta)")
        print(" % Menu de Info Minecraft (consulta)")
        at = input("\n0 - Voltar\n\n> ")
        if at == "0":
            main()
            break
        else:
            os.system("clear")
            os.system("clear")
            glob(1)
            
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
            print("Programa Finalizado.\033[0m\n")
            exit()
            break
        else:
            print(" ")
if __name__ == "__main__":
    main()
