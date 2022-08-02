from msilib.schema import ComboBox
from multiprocessing.sharedctypes import Value
from tkinter import messagebox
from turtle import color
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

#JANELA PRINCIPAL
janela_principal = Tk()
janela_principal.title("VENDAS E LUCROS")
janela_principal.geometry("870x350")
janela_principal.resizable(False, False)

#IMAGENS
tabela_vendas = PhotoImage(file="Tabela_vendas.png")
lbl_tabela = Label(janela_principal, image=tabela_vendas)
lbl_tabela.place(x=380, y=175)
logo_shop = PhotoImage(file="logo.png")
lbl_logo = Label(janela_principal, image=logo_shop, height=86)
lbl_logo.place(x=347, y=2)

#FUNÇÃO MESES
def func_meses(*args):
    pass
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
func_meses(*mes)

"""def seleciona_mes():
    if cb_meses.get() == "janeiro":
        print(mes[0])
    elif cb_meses.get() == "fevereiro":
        print(mes[1])
    elif cb_meses.get() == "março":
        print(mes[2])
    elif cb_meses.get() == "abril":
        print(mes[3])
    elif cb_meses.get() == "maio":
        print(mes[4])
    elif cb_meses.get() == "junho":
        print(mes[5])"""

#FUNÇÃO RESULTADO
def apresenta_resultado():
    if cb_meses.get() == "":
        messagebox.showerror("MES", "Selecione um mês de início.")
    else:
        #CÁLCULO DO PERCENTUAL
        lbl_periodo['text'] = f'Levantamento entre os meses de \n {cb_meses.get()} e junho:'
        #notebooks
        if cb_meses.get() == "janeiro":
            soma_notebooks = notebooks[5] - notebooks[0]
            aumento_notebooks = soma_notebooks / notebooks[0]
            percentual_aumento_notebooks = aumento_notebooks * 100
            #celulares
            soma_celulares = celulares[5] - celulares[0]
            aumento_celulares = soma_celulares / celulares[0]
            percentual_aumento_celulares = aumento_celulares * 100
            #tvs
            soma_tvs = tvs[5] - tvs[0]
            aumento_tvs = soma_tvs / tvs[0]
            percentual_aumento_tvs = aumento_tvs * 100
            #resultados da amostragem
            #celulares
            if percentual_aumento_celulares < 0:
                lbl_resultado_cel_variacao['text'] = 'Queda de'
                lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_cel_variacao['text'] = 'Aumento de'
            lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            #notebooks
            if percentual_aumento_notebooks < 0:
                lbl_resultado_note_variacao['text'] = 'Queda de'
                lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_note_variacao['text'] = 'Aumento de'
            lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_notebooks:.2f}% nas vendas de notebooks.'
            #tvs
            if percentual_aumento_tvs < 0:
                lbl_resultado_tv_variacao['text'] = 'Queda de'
                lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_tv_variacao['text'] = 'Aumento de'
            lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_tvs:.2f}% nas vendas de TVs.'
        elif cb_meses.get() == "fevereiro":
            soma_notebooks = notebooks[5] - notebooks[1]
            aumento_notebooks = soma_notebooks / notebooks[1]
            percentual_aumento_notebooks = aumento_notebooks * 100
            #celulares
            soma_celulares = celulares[5] - celulares[1]
            aumento_celulares = soma_celulares / celulares[1]
            percentual_aumento_celulares = aumento_celulares * 100
            #tvs
            soma_tvs = tvs[5] - tvs[1]
            aumento_tvs = soma_tvs / tvs[1]
            percentual_aumento_tvs = aumento_tvs * 100
            #resultado da amostragem
            #celulares
            #celulares
            if percentual_aumento_celulares < 0:
                lbl_resultado_cel_variacao['text'] = 'Queda de'
                lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_cel_variacao['text'] = 'Aumento de'
            lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            #notebooks
            if percentual_aumento_notebooks < 0:
                lbl_resultado_note_variacao['text'] = 'Queda de'
                lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_note_variacao['text'] = 'Aumento de'
            lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_notebooks:.2f}% nas vendas de notebooks.'
            #tvs
            if percentual_aumento_tvs < 0:
                lbl_resultado_tv_variacao['text'] = 'Queda de'
                lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_tv_variacao['text'] = 'Aumento de'
            lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_tvs:.2f}% nas vendas de TVs.'
        elif cb_meses.get() == "março":
            soma_notebooks = notebooks[5] - notebooks[2]
            aumento_notebooks = soma_notebooks / notebooks[2]
            percentual_aumento_notebooks = aumento_notebooks * 100
            #celulares
            soma_celulares = celulares[5] - celulares[2]
            aumento_celulares = soma_celulares / celulares[2]
            percentual_aumento_celulares = aumento_celulares * 100
            #tvs
            soma_tvs = tvs[5] - tvs[2]
            aumento_tvs = soma_tvs / tvs[2]
            percentual_aumento_tvs = aumento_tvs * 100
            #resultado da amostragem
            #celulares
            #celulares
            if percentual_aumento_celulares < 0:
                lbl_resultado_cel_variacao['text'] = 'Queda de'
                lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_cel_variacao['text'] = 'Aumento de'
            lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            #notebooks
            if percentual_aumento_notebooks < 0:
                lbl_resultado_note_variacao['text'] = 'Queda de'
                lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_note_variacao['text'] = 'Aumento de'
            lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_notebooks:.2f}% nas vendas de notebooks.'
            #tvs
            if percentual_aumento_tvs < 0:
                lbl_resultado_tv_variacao['text'] = 'Queda de'
                lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_tv_variacao['text'] = 'Aumento de'
            lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_tvs:.2f}% nas vendas de TVs.'
        elif cb_meses.get() == "abril":
            soma_notebooks = notebooks[5] - notebooks[3]
            aumento_notebooks = soma_notebooks / notebooks[3]
            percentual_aumento_notebooks = aumento_notebooks * 100
            #celulares
            soma_celulares = celulares[5] - celulares[3]
            aumento_celulares = soma_celulares / celulares[3]
            percentual_aumento_celulares = aumento_celulares * 100
            #tvs
            soma_tvs = tvs[5] - tvs[3]
            aumento_tvs = soma_tvs / tvs[3]
            percentual_aumento_tvs = aumento_tvs * 100
            #resultado da amostragem
            #celulares
            #celulares
            if percentual_aumento_celulares < 0:
                lbl_resultado_cel_variacao['text'] = 'Queda de'
                lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_cel_variacao['text'] = 'Aumento de'
            lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            #notebooks
            if percentual_aumento_notebooks < 0:
                lbl_resultado_note_variacao['text'] = 'Queda de'
                lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_note_variacao['text'] = 'Aumento de'
            lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_notebooks:.2f}% nas vendas de notebooks.'
            #tvs
            if percentual_aumento_tvs < 0:
                lbl_resultado_tv_variacao['text'] = 'Queda de'
                lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_tv_variacao['text'] = 'Aumento de'
            lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_tvs:.2f}% nas vendas de TVs.'
        elif cb_meses.get() == "maio":
            soma_notebooks = notebooks[5] - notebooks[4]
            aumento_notebooks = soma_notebooks / notebooks[4]
            percentual_aumento_notebooks = aumento_notebooks * 100
            #celulares
            soma_celulares = celulares[5] - celulares[4]
            aumento_celulares = soma_celulares / celulares[4]
            percentual_aumento_celulares = aumento_celulares * 100
            #tvs
            soma_tvs = tvs[5] - tvs[4]
            aumento_tvs = soma_tvs / tvs[4]
            percentual_aumento_tvs = aumento_tvs * 100
            #resultado da amostragem
            #celulares
            #celulares
            if percentual_aumento_celulares < 0:
                lbl_resultado_cel_variacao['text'] = 'Queda de'
                lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_cel_variacao['text'] = 'Aumento de'
            lbl_resultado_cel_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            #notebooks
            if percentual_aumento_notebooks < 0:
                lbl_resultado_note_variacao['text'] = 'Queda de'
                lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_note_variacao['text'] = 'Aumento de'
            lbl_resultado_note_porcentagem['text'] = f'{percentual_aumento_notebooks:.2f}% nas vendas de notebooks.'
            #tvs
            if percentual_aumento_tvs < 0:
                lbl_resultado_tv_variacao['text'] = 'Queda de'
                lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_celulares:.2f}% nas vendas de celulares.'
            else:
                lbl_resultado_tv_variacao['text'] = 'Aumento de'
            lbl_resultado_tv_porcentagem['text'] = f'{percentual_aumento_tvs:.2f}% nas vendas de TVs.'

#COMBOBOX MESES
cb_meses = ttk.Combobox(janela_principal, value=mes)
cb_meses.place(x=360, y=100)

#BOTÃO SELECIONAR
btn_selecionar = Button(janela_principal, text='Selecionar', command=apresenta_resultado)
btn_selecionar.place(x=360, y=130)

#LISTAGENS DOS PRODUTOS
def func_celular(*args):
    pass
celulares = [442, 234, 282, 242, 263, 350]
func_celular(celulares)

def func_notebook(*args):
    pass
notebooks = [117, 251, 260, 274, 180, 215]
func_notebook(notebooks)

def func_tv(*args):
    pass
tvs = [176, 159, 200, 145, 111, 173]
func_tv(tvs)

#FUNÇÃO MATPLOTLIB
def gera_grafico():
    if cb_meses.get() == "":
        messagebox.showerror("MES", "Selecione um mês de início.")
        plt.show(False)

    plt.figure(figsize=(7,5))
    plt.style.use('ggplot')

    plt.title('Vendas no primeiro semestre')
    plt.xlabel('Meses estudados')
    plt.ylabel('Valores obtidos')

    if cb_meses.get() == "janeiro":
        plt.plot((mes[0], mes[1], mes[2], mes[3], mes[4], mes[5]), (notebooks[0], notebooks[1], notebooks[2], notebooks[3], notebooks[4], notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[0], mes[1], mes[2], mes[3], mes[4], mes[5]), (celulares[0], celulares[1], celulares[2], celulares[3], celulares[4], celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[0], mes[1], mes[2], mes[3], mes[4], mes[5]), (tvs[0], tvs[1], tvs[2], tvs[3], tvs[4], tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')

    if cb_meses.get() == "fevereiro":
        plt.plot((mes[1], mes[2], mes[3], mes[4], mes[5]), (notebooks[1], notebooks[2], notebooks[3], notebooks[4], notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[1], mes[2], mes[3], mes[4], mes[5]), (celulares[1], celulares[2], celulares[3], celulares[4], celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[1], mes[2], mes[3], mes[4], mes[5]), (tvs[1], tvs[2], tvs[3], tvs[4], tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')
    
    if cb_meses.get() == "março":
        plt.plot((mes[2], mes[3], mes[4], mes[5]), (notebooks[2], notebooks[3], notebooks[4], notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[2], mes[3], mes[4], mes[5]), (celulares[0], celulares[1], celulares[2], celulares[3], celulares[4], celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[2], mes[3], mes[4], mes[5]), (tvs[0], tvs[1], tvs[2], tvs[3], tvs[4], tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')
    
    if cb_meses.get() == "abril":
        plt.plot((mes[3], mes[4], mes[5]), (notebooks[3], notebooks[4], notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[3], mes[4], mes[5]), (celulares[3], celulares[4], celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[3], mes[4], mes[5]), (tvs[3], tvs[4], tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')

    if cb_meses.get() == "maio":
        plt.plot((mes[4], mes[5]), (notebooks[4], notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[4], mes[5]), (celulares[4], celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[4], mes[5]), (tvs[4], tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')
    
    if cb_meses.get() == "junho":
        plt.plot((mes[5]), (notebooks[5]), label='notebooks', linewidth=5)
        plt.plot((mes[5]), (celulares[5]), label='celulares', linewidth=5)
        plt.plot((mes[5]), (tvs[5]), label='televisores', linewidth=5)
        plt.legend(fontsize=14, frameon=True, framealpha=0.5, facecolor='white')

    plt.show()

#BOTÃO GERA GRÁFICO
btn_grafico = Button(janela_principal, text="Gráfico", width=8, command=gera_grafico)
btn_grafico.place(x=435, y=130)

#RESULTADOS DA PESQUISA
#período abrangido
lbl_periodo = Label(janela_principal, font="Arial 10 bold", text="")
lbl_periodo.place(x=110, y=120)
#celulares
lbl_resultado_cel_variacao = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)
lbl_resultado_cel_variacao.place(x=70, y=170)
"""lbl_resultado_cel_queda = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)"""

lbl_resultado_cel_porcentagem = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=26, height=2, anchor=W)
lbl_resultado_cel_porcentagem.place(x=155, y=170)

#notebooks
lbl_resultado_note_variacao = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)
lbl_resultado_note_variacao.place(x=70, y=210)
"""lbl_resultado_note_queda = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)"""

lbl_resultado_note_porcentagem = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=26, height=2, anchor=W)
lbl_resultado_note_porcentagem.place(x=155, y=210)

#tvs
lbl_resultado_tv_variacao = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)
lbl_resultado_tv_variacao.place(x=70, y=250)
"""lbl_resultado_tv_queda = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=10, height=2, anchor=E)"""

lbl_resultado_tv_porcentagem = Label(janela_principal, text="", font="Arial 10 bold", bg="dark gray", width=26, height=2, anchor=W)
lbl_resultado_tv_porcentagem.place(x=155, y=250)

#-------------
#ASSINATURA
lbl_assinatura = Label(janela_principal, text="Desenvolvido por Marco Moraes", font="Arial 11 italic bold", bd=15)
lbl_assinatura.place(x=320, y=300)

janela_principal.mainloop()