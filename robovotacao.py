#  Robô de votação
#  A cada 50 votos ele abre uma nova aba e faz mais 50 votos.
#  A cada 5 abas ele abre uma nova guia.
#  Faz todo o processo e no total abre mais 5 guias.
#  Depois o robô para completamente e tem que ativar manualmente novamente.
#

#  Esse


import time
import pyautogui as py
import pyperclip


py.PAUSE = 0.7
py.FAILSAFE = True
pyperclip.copy('https://chat.openai.com/chat')  # aqui vai o site
n = 0
i = 0
j = 0

time.sleep(7)
py.press('tab')
py.press('enter')
py.press('tab')
py.press('tab')
py.press('tab')
py.press('enter')  # entrou no participante
time.sleep(2)
py.press('tab')
py.press('enter')  # votou no participante
time.sleep(3)
py.press('tab')
py.press('tab')
py.press('tab')
py.press('enter')  # votar novamente
time.sleep(5)
while j < 5:
    while i < 5:
        while n < 50:
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # entrou no participante
            time.sleep(0.7)
            py.press('tab')
            py.press('enter')  # votou no participante
            time.sleep(3)
            n += 1
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # votar novamente
            time.sleep(3)
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # entrou no participante
            time.sleep(0.7)
            py.press('tab')
            py.press('enter')  # votou no participante
            time.sleep(3)
            n += 1
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # votar novamente
            time.sleep(3)
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # entrou no participante
            time.sleep(0.7)
            py.press('tab')
            py.press('enter')  # votou no participante
            time.sleep(3)
            n += 1
            py.press('tab')
            py.press('tab')
            py.press('tab')
            py.press('enter')  # votar novamente
            time.sleep(2)
            py.press('f5')
            time.sleep(3)
            py.press('tab')
            py.press('enter')

        #  abrir uma nova aba 5 vezes
        i += 1
        n = 0
        py.hotkey('ctrl', 't')
        time.sleep(10)
        py.hotkey('ctrl', 'v')
        py.press('enter')
        time.sleep(7)

    #  abrir uma nova janela 5 vezes
    j += 1
    i = 0
    py.hotkey('ctrl', 'n')
    time.sleep(10)
    py.hotkey('ctrl', 'v')
    py.press('enter')
    time.sleep(10)
    py.press('tab')
    py.press('enter')
    py.press('tab')
    py.press('tab')
    py.press('enter')  # entrou no participante
    time.sleep(2)
    py.press('tab')
    py.press('enter')  # votou no participante
    time.sleep(3)
    py.press('tab')
    py.press('tab')
    py.press('tab')
    py.press('enter')  # votar novamente
