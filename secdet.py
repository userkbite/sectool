#!/usr/bin/env python3

import requests, json
import os, time
import platform

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("clear")
        
def youtube():
    if platform.system() == "Windows":
        import webbrowser
        webbrowser.open_new_tab("https://youtube.com/nightzx")
    else:
        os.system("termux-open-url https://youtube.com/nightzx")

clear()

R = '\033[1;31m'; B = '\033[1;34m'; C = '\033[1;37m'; Y = '\033[1;33m'; G = '\033[1;32m'; RT = '\033[;0m'

code_info = C + '[' + Y + 'i' + C + '] '
code_details = C + '[' + G + '*' + C + '] '
code_result = C + '[' + G + '+' + C + '] '
code_error = C + '[' + R + '!' + C + '] '

def main():
    clear()
    
    print('\n' + code_info + '4Devs API.')
    print(f'''
{C}[{G}i{C}] Formas de operação:

[{G}1{C}] Gerar Nome.
[{G}2{C}] Gerar Endereço.
[{G}3{C}] Gerar CPF.

[{G}99{C}] Youtube.
[{G}00{C}] {R}Sair.{C}
''')

    tool = input(f'{C}[{G}+{C}] Selecione a forma de operação:{B} ')
    
    if tool == '1':
        gerar("nome")
    
    elif tool == '2':
        gerar("endereco")
        
    elif tool == '3':
        gerar("cpf")
    
    elif tool == '99':
        clear()
        youtube()
    
    elif tool == '00':
        clear()
        print(f'\n{G}by N1GHTZX !{C}\n')
    
    else:
        clear()
        print(f'{C}[{R}-{C}] Seleção inválida.')
        time.sleep(0.2)
        main()

def gerar(data=''):
    req = requests.post('https://www.4devs.com.br/ferramentas_online.php',{"acao":"gerar_pessoa","pontuacao":"S","txt_qtde":1}).content
    res = json.loads(req)
    if data != '':
        if data == 'endereco':
            print(f'\nENDEREÇO: {res["endereco"]}\nBAIRRO: {res["bairro"]}\nCIDADE: {res["cidade"]}\n')
        else:
            print(f'\n{data.upper()}: {res[data]}\n')
            
        nova = input(f'{C}[{G}+{C}] Deseja realizar uma nova operação?[{G}s{C}/{R}n{C}]: ').lower()
        if nova == 's' or nova == 'sim':
            clear()
            main()
        else:
            print(f'\n{G}by N1GHTZX !{C}\n')
            exit()
    
main()
