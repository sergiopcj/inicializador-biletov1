import os
import glob
import time
import datetime
from pathlib import Path
from tkinter import ttk, Text, DoubleVar, PhotoImage
from ttkbootstrap import Style
import webbrowser

def arquivo_erro(erro):
    erro = f"Data: {datetime.date.today()} - {erro}\n"
    with open("c:/inicializador/log/erro.txt", "a") as arquivo:
        arquivo.write(erro)

def fecha_bileto():
    try:
        os.popen('taskkill /f /im "Sympla Bileto.exe"')
    except OSError as e:
        arquivo_erro(f"Error: {e.strerror}")

def apaga_logs():
    logs = glob.glob('C:/Bileto/logs/*.log')
    zips = glob.glob('C:/Bileto/logs/*.gz')

    for arquivo in logs + zips:
        try:
            os.remove(arquivo)
        except OSError as e:
            arquivo_erro(f"Error: {e.strerror}")

def verifica_kbyte():
    KBYTE_MAX = 4600
    TEMPO_MAX = 1800
    dez_porc, quarenta_porc, sessenta_porc, oitenta_porc = 490, 1960, 2940, 3920
    Kbyte_indice, tempo_indice = 0, 0

    while not os.path.isfile('C:/Bileto/logs/system.log'):
        time.sleep(2)

    while Kbyte_indice < KBYTE_MAX:
        Kbyte_indice = Path('C:/Bileto/logs/system.log').stat().st_size
        time.sleep(0.1)
        tempo_indice += 1

        if Kbyte_indice <= dez_porc:
            varBarra.set(10)
        elif Kbyte_indice <= quarenta_porc:
            varBarra.set(40)
        elif Kbyte_indice <= sessenta_porc:
            varBarra.set(60)
        elif Kbyte_indice <= oitenta_porc:
            varBarra.set(80)
        elif tempo_indice >= TEMPO_MAX:
            varBarra.set(0)
            alterar_saida('Tempo Maior do que o esperado, entre em contato com o Suporte!')
            break
        else:
            botaoLogin.configure(state="normal")
            varBarra.set(100)
        janela.update()

def verifica_daruma():
    mensagem_daruma_sucesso = 'Daruma successfully detected'
    mensagem_daruma_falha = 'Daruma was not detected'

    with open("C:/Bileto/logs/system.log", "r") as arquivo_system:
        ler_arquivo = arquivo_system.read()

    if mensagem_daruma_falha in ler_arquivo:
        mensagem = 'Sistema está pronto para uso, mas NÃO foi localizado a DARUMA! \n ' \
                   'Caso seja sua impressora padrão, verifique se ela está: \n ' \
                   'Conectada no USB, Ligada e com a Luz verde acesa. \n ' \
                   'Clique em Reiniciar e o Sistema irá carregar novamente!'
    elif mensagem_daruma_sucesso in ler_arquivo:
        if verifica_impressora_selecionada() == "DARUMA":
            mensagem = 'Sistema pronto para Login!'
        else:
            mensagem = 'Sistema foi iniciado com sucesso! \n' \
                       'ATENÇÃO: Necessário configurar suas Preferências de Impressão na Bileto. \n' \
                       'Clique em Central de Ajuda!'
            link.bind("<Button-1>", lambda e: callback(
                "https://suporte-bileto-sympla.zendesk.com/hc/pt-br/articles/7762329901965-Definir-Impressora-Padr%C3%A3o-"
            ))
    alterar_saida(mensagem)

def verifica_impressora_selecionada():
    with open("C:/Bileto/conf/printer-configuration.json", "r") as arquivo_config:
        ler_arquivo = arquivo_config.read()

    impressora_ingresso_indice_1 = ler_arquivo.find('"ticketPrinterName"') + 21
    impressora_ingresso_indice_2 = ler_arquivo.find('"ticketTemplateType"') - 2

    impressora_ingresso = ler_arquivo[impressora_ingresso_indice_1:impressora_ingresso_indice_2]
    return impressora_ingresso

def callback(url):
    webbrowser.open_new_tab(url)

def inciar_sistema():
    botaoIniciar.configure(text='Reiniciar')
    alterar_saida('Carregando...')
    janela.update()
    fecha_bileto()
    time.sleep(2)
    apaga_logs()
    try:
        script_ps = 'C:/Bileto/Sympla Bileto.exe'
        os.popen(script_ps)
    except OSError as e:
        arquivo_erro(f"Error: {e.strerror}")
    time.sleep(5)
    verifica_kbyte()
    verifica_daruma()

def abrir_chat():
    try:
        script_ps = 'start "" chrome --start-fullscreen --app=https://bit.ly/suporte-sympla'
        os.popen(script_ps)
    except OSError as e:
        arquivo_erro(f"Error: {e.strerror}")

    mensagem = 'O horário de atendimento do suporte está disponível na central de ajuda!'
    link.bind("<Button-1>",
              lambda e: callback(
                  "https://suporte-bileto-sympla.zendesk.com/hc/pt-br/articles/7957483768077-Hor%C3%A1rio-de-atendimento"
              ))

    alterar_saida(mensagem)

def abrir_bileto():
    try:
        script_ps = 'start "" chrome --start-fullscreen --app=https://boxoffice.bileto.sympla.com.br'
        os.popen(script_ps)
    except OSError as e:
        arquivo_erro(f"Error: {e.strerror}")
    mensagem = 'Iniciando tela de login... Boas vendas!'
    varBarra.set(0)
    alterar_saida(mensagem)

def alterar_saida(texto_saida):
    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', texto_saida)
    saida.configure(state='disabled')

style = Style(theme='cerculean')
janela = style.master
janela.iconbitmap(default="img/icone.ico")
janela.title('Iniciador Sympla Bileto')

frame_geral = ttk.Frame(janela)
frame_geral.configure(takefocus=False, height=400, width=500)
frame_geral.pack(anchor="center", fill="both", expand="yes", side="top")
frame_geral.grid_propagate(0)

link = ttk.Label(frame_geral, text="Central De Ajuda", font=('Helveticabold', 11), cursor="hand2")
link.configure(foreground="blue")
link.bind("<Button-1>", lambda e: callback("https://suporte-bileto-sympla.zendesk.com/hc/pt-br"))
link.place(anchor="nw", relx=0.70, rely=0.00)

img_logo = PhotoImage(file="img/LogoSymplaBileto.png")
label_img = ttk.Label(frame_geral, image=img_logo)
label_img.place(anchor="nw", relx=0.06, rely=0.05)

botaoIniciar = ttk.Button(frame_geral, command=inciar_sistema)
botaoIniciar.configure(compound="none", takefocus=False, text="Iniciar")
botaoIniciar.place(anchor="nw", relheight=0.10, relwidth=0.20, relx=0.07, rely=0.30)

botaoLogin = ttk.Button(frame_geral, command=abrir_bileto)
botaoLogin.configure(text="Login", state="disabled")
botaoLogin.place(anchor="nw", relheight=0.10, relwidth=0.20, relx=0.40, rely=0.30)

botaoChat = ttk.Button(frame_geral)
botaoChat.configure(text="Chat-Suporte", command=abrir_chat, state="normal")
botaoChat.place(anchor="nw", relheight=0.10, relwidth=0.20, relx=0.72, rely=0.30)

saida = Text(frame_geral)
_text_ = 'Seja Bem-Vindo a Bileto! \n' \
         'Clique em "iniciar" e avisaremos quando o sistema estiver pronto.'
saida.insert("0.0", _text_)
saida.configure(font="TkDefaultFont", state="disabled")
saida.place(anchor="nw", relheight=0.40, relwidth=0.85, relx=0.07, rely=0.45)

varBarra = DoubleVar()
varBarra.set(0)
bar = ttk.Progressbar(frame_geral, variable=varBarra, maximum=100)
bar.place(anchor="nw", relheight=0.10, relwidth=0.85, relx=0.07, rely=0.85)

janela.mainloop()
