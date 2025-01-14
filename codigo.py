import pyautogui
import time

#pyautogui.click -> clicar
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever

pyautogui.PAUSE = 0.5

# Passo1: abrir site da empresa
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#    sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#pausar por 3 segundos
time.sleep(3)

# Passo2: Fazer login
pyautogui.click(x=844, y=362)
pyautogui.write("ghoscopdev@gmail.com")

pyautogui.press("tab")
pyautogui.write("auladepython1")
pyautogui.click(x=949, y=519)

# passo3: pegar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")

time.sleep(2)

# passo4: cadastrar 1 produto
for i in tabela.index:
    pyautogui.click(x=749, y=252)

    #codigo
    codigo = tabela.loc[i , "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[i , "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[i , "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    #categoria
    categoria = tabela.loc[i , "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    #preco_unitario
    preco_unitario = tabela.loc[i , "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[i , "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[i , "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter")

    #numero positivo = scroll para cima
    #numero negativo = scroll para baixo

    pyautogui.scroll(1000)


# passo5: repetir o passo 4 ate achar todos os produtos
