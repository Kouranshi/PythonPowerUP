# Passo a passo do Projeto
#Passo 1: Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip instal pyautogui

import pyautogui
import time

pyautogui.PAUSE = 0.5 #Define que a cada código, haverá um tempo de pausa para rodar o próximo código

#pyautogui.click -> Clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar uma tecla do teclado

#abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)   #Dormir por alguns segundos (3 segundos, nesse caso) antes de continuar


#Passo 2: Fazer login
pyautogui.click(x=541, y=369)
pyautogui.write("sousoumhomem@gmail.com")
pyautogui.press('tab')
pyautogui.write("12345678")
pyautogui.click(x=685, y=532)

time.sleep(3)

#Passo 3: Importar a base de dados
#pip install pandas numpy openpyxl
import pandas
tabela = pandas.read_csv('produtos.csv')

#Passo 4: Cadastrar 1 produto
#para cada linha da tabela
for linha in tabela.index:

    #clicar no 1° campo (código)
    pyautogui.click(x=509, y=257)

    #código do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    #marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    #tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    #categoria
    #str() string -> texto
    #str(1) -> 1 -> "1"
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    #preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    #obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    #enviar
    pyautogui.press('enter')

    pyautogui.scroll(5000)

#Passo 5: Repetir o processo de cadastrar até acabar a base de dados
