import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import mysql.connector
import datetime
from tkinter import messagebox

conexao_banco = mysql.connector.connect(
    host  = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'psicologia'
)
cursor = conexao_banco.cursor()

style = Style(theme='superhero') #style pra nois estiliza nosso tkanisndi

def isANumber(value):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    for i in letras:
        if i in value:
            return False
    else:
        return True

def acao_cadastro_paciente(janela_cadastro):
    
    janela_cadastro.destroy()
    
    # Criar a janela de cadastro de paciente
    cadastropacientejanela = ttk.Window()
    
    cadastropacientejanela.title("Cadastro Paciente")
    cadastropacientejanela.geometry("600x600")
    cadastropacientejanela.resizable(False, False)

    # Pergunta sobre o tipo de cadastro
    label = tk.Label(cadastropacientejanela, text="Cadastro de Paciente", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_nome = tk.Label(cadastropacientejanela, text="Nome:", font=("Calibri (Corpo)", 11))
    label_nome.pack()

    entry_nome = tk.Entry(cadastropacientejanela)
    entry_nome.pack()

    label_email = tk.Label(cadastropacientejanela, text="Email:", font=("Calibri (Corpo)", 11))
    label_email.pack()

    entry_email = tk.Entry(cadastropacientejanela)
    entry_email.pack()

    label_dataNascimento = tk.Label(cadastropacientejanela, text="Data De Nascimento (AAAA-MM-DD):", font=("Calibri (Corpo)", 11))
    label_dataNascimento.pack()

    entry_dataNascimento = tk.Entry(cadastropacientejanela)
    entry_dataNascimento.pack()
    
    
    label_telefone = tk.Label(cadastropacientejanela, text="Telefone Paciente:", font=("Calibri (Corpo)", 11))
    label_telefone.pack()

    entry_telefone = tk.Entry(cadastropacientejanela)
    entry_telefone.pack()

    label_endereco = tk.Label(cadastropacientejanela, text="Endereço Paciente:", font=("Calibri (Corpo)", 11))
    label_endereco.pack()

    entry_endereco = tk.Entry(cadastropacientejanela)
    entry_endereco.pack()

    label_cpf = tk.Label(cadastropacientejanela, text="CPF Paciente :", font=("Calibri (Corpo)", 11))
    label_cpf.pack()

    entry_cpf = tk.Entry(cadastropacientejanela)
    entry_cpf.pack()

    label_status = tk.Label(cadastropacientejanela, text="STATUS Paciente :", font=("Calibri (Corpo)", 11))
    label_status.pack()

    entry_status = tk.Entry(cadastropacientejanela)
    entry_status.pack()
    #### entry e label para a tabela de convenios
    #label_statusconvenio = tk.Label(cadastropacientejanela, text="Possui convênio? Sim/Não")
    #label_statusconvenio.pack()
        
    #entry_statusconvenio = tk.Entry(cadastropacientejanela)
    #entry_statusconvenio.pack()
    ###nome convenio
    #label_nomeconvenio = tk.Label(cadastropacientejanela, text="Nome do convênio (se tiver): ")
    #label_nomeconvenio.pack()
        
    #entry_nomeconvenio = tk.Entry(cadastropacientejanela)
    #entry_nomeconvenio.pack()
    ###telefone convenio
    #label_telefoneconvenio = tk.Label(cadastropacientejanela, text="Telefone convênio:")
    #label_telefoneconvenio.pack()
        
    #entry_telefoneconvenio = tk.Entry(cadastropacientejanela)
    #entry_telefoneconvenio.pack()
    ###Cobertura convenio """ """
    dataAgora = datetime.datetime.now()
    global dataAgoraCerta
    dataAgoraCerta = dataAgora.strftime('%Y-%m-%d')
    
    def abrir_cadastro_convenio():
        cadastropacientejanela.destroy()
        cadastroconveniojanela = ttk.Window()
        cadastroconveniojanela.title("Cadastro de Convenio")
        cadastroconveniojanela.geometry("600x600")
        cadastroconveniojanela.resizable(False , False)
        # Campos para o cadastro de convênio
        label_convenio = tk.Label(cadastroconveniojanela, text="Cadastro de Convênio", font=("Calibri (Corpo)", 20))
        label_convenio.pack(pady=30)
        label_escolhaconvenio = tk.Label(cadastroconveniojanela , text="Você possui convênio")
        label_escolhaconvenio.pack()
        
        button_sim = tk.Button(cadastroconveniojanela , text='Sim', command=lambda: entryconvenio(cadastroconveniojanela))
        button_sim.pack(pady=10)

        button_nao = tk.Button(cadastroconveniojanela, text="Não", command=lambda: botaonaoadd(cadastroconveniojanela))
        button_nao.pack(pady=10)
    
    def cadastrarpacientebotaofinal():
        global nome, email, data, telefone, endereco, cpf, status
        nome = entry_nome.get()
        email = entry_email.get()
        data = entry_dataNascimento.get()
        telefone = entry_telefone.get() #nao pode ser igual
        endereco = entry_endereco.get() 
        cpf = entry_cpf.get() # nao pode ser igual 
        status = entry_status.get().capitalize()
        #statusconvenio = entry_statusconvenio.get()
        comandosql =f"SELECT cpf from paciente Where cpf = {cpf}"
        cursor.execute(comandosql)
        dados_tabela = cursor.fetchall()
        if len(cpf) < 11:
            messagebox.showerror("Erro" , "Tamanho do CPF abaixo do padrão")
        elif len(cpf) > 11:
            messagebox.showerror("Erro" , "Tamanho do CPF acima do padrão")
        if len(cpf) == 11:
            
            if len(dados_tabela) >= 1:
                messagebox.showerror("Erro", "CPF já existe")
            elif len(dados_tabela) == 0:
                comandosql =f"SELECT email from paciente Where email = '{email}'"
                cursor.execute(comandosql)
                dados_tabela = cursor.fetchall()
                if len(dados_tabela) >= 1:
                    messagebox.showerror("Erro", "Email já existe")

                elif len(dados_tabela) == 0:
                    comandosql =f"SELECT telefone from paciente Where telefone = {telefone}"
                    cursor.execute(comandosql)
                    dados_tabela = cursor.fetchall()
                    if len(dados_tabela) >= 1:
                        messagebox.showerror("Erro", "Telefone já existe")
                    elif len(dados_tabela) == 0:
                        entry_nome.delete(0 , tk.END)
                        entry_email.delete(0 , tk.END)
                        entry_dataNascimento.delete(0 , tk.END)
                        entry_telefone.delete(0 , tk.END)
                        entry_endereco.delete(0 , tk.END)
                        entry_cpf.delete(0 , tk.END)
                        entry_status.delete(0 , tk.END)
                        abrir_cadastro_convenio()
                        
    

            
    label_datacadastro = tk.Label(cadastropacientejanela, text=f"Data do Cadastro: {dataAgoraCerta}")
    label_datacadastro.pack()
    botao_cadastro  = tk.Button(cadastropacientejanela, text='Cadastrar', command=cadastrarpacientebotaofinal)
    botao_cadastro.pack(pady=50)
    def voltar_para_janela_opcoes():
        cadastropacientejanela.destroy()  # Fecha a janela de cadastro de paciente
        abrir_proxima_janela()  # Abre a janela de opções

    botao_saircadastropaciente = tk.Button(cadastropacientejanela , text='Voltar' , command=voltar_para_janela_opcoes)
    botao_saircadastropaciente.pack(pady=10)


            

        # comando 

    
    cadastropacientejanela.mainloop()

def acao_cadastro_consultas(janela_cadastro):
    def voltar_para_janela_opcoes(): #botei a outra função aqui tbm
        janelacadastroconsultas.destroy()  # Fecha a janela de cadastro de paciente
        abrir_proxima_janela()  # Abre a janela de opções
        
    janela_cadastro.destroy()
    janelacadastroconsultas = ttk.Window()
    janelacadastroconsultas.title("Cadastro Psicologo")
    janelacadastroconsultas.geometry("600x600")
    janelacadastroconsultas.resizable(False, False)

    
    label = tk.Label(janelacadastroconsultas, text="Cadastro Psicologo", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)
    ###label e entry do crp
    label_nomeconsulta = tk.Label(janelacadastroconsultas , text="Informe o nome do paciente: ")
    label_nomeconsulta.pack()
    entry_nomeconsulta = tk.Entry(janelacadastroconsultas)
    entry_nomeconsulta.pack()
########################################################
    label_data = tk.Label(janelacadastroconsultas , text="Informe a data da consulta: ")
    label_data.pack()
    entry_data = tk.Entry(janelacadastroconsultas)
    entry_data.pack()
###########################################################
    label_preco = tk.Label(janelacadastroconsultas , text="Informe o preço estabelecida da consulta: ")
    label_preco.pack()
    entry_preco = tk.Entry(janelacadastroconsultas)
    entry_preco.pack()
###########################################################
    label_data_cancelamento = tk.Label(janelacadastroconsultas , text='Disponibilidade: ')
    label_data_cancelamento.pack()
    entry_data_cancelamento = tk.Entry(janelacadastroconsultas)
    entry_data_cancelamento.pack()
############################################################
    label_pagamento = tk.Label(janelacadastroconsultas , text='Endereço do Psicologo: ')
    label_pagamento.pack()
    entry_pagamento = tk.Entry(janelacadastroconsultas)
    entry_pagamento.pack()
############################################################
    label_duracao = tk.Label(janelacadastroconsultas , text='Nome do Psicologo:')
    label_duracao.pack()
    entry_duracao = tk.Entry(janelacadastroconsultas)
    entry_duracao.pack()
    ###########################
    label_statusconsulta = tk.Label(janelacadastroconsultas , text='Nome do Psicologo:')
    label_statusconsulta.pack()
    entry_statusconsulta = tk.Entry(janelacadastroconsultas)
    entry_statusconsulta.pack()

    """ botaocadastropsicologo = tk.Button(janelacadastropsicologo , text='Cadastrar' , command= funcaobotao)
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastropsicologo , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10) """
    def funcaobotaoconsulta():
        global nome, crp, email, telefone, endereco, disponibibilidade
        nome = entry_nomeconsulta.get()
        preco = int(entry_preco.get())
        pagamento = entry_pagamento.get()
        data = entry_data.get() #nao pode ser igual
        data_cancelamento= entry_data_cancelamento.get() 
        statusconsulta = entry_statusconsulta.get() # nao pode ser igual 
        duracao = entry_duracao.get()
        
        if isANumber(preco):
            print('é um preco valido')
        elif isANumber(preco) == False:
            messagebox.showerror('Erro' , 'Não é um valor valido, digite um numero.')
        
        
    botaocadastropsicologo = tk.Button(janelacadastroconsultas , text='Cadastrar' , command= funcaobotaoconsulta)
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastroconsultas , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10) 

def acao_cadastro_psicologo(janela_cadastro):
    def voltar_para_janela_opcoes(): #botei a outra função aqui tbm
        janelacadastropsicologo.destroy()  # Fecha a janela de cadastro de paciente
        abrir_proxima_janela()  # Abre a janela de opções
        
    janela_cadastro.destroy()
    janelacadastropsicologo = ttk.Window()
    janelacadastropsicologo.title("Cadastro Psicologo")
    janelacadastropsicologo.geometry("600x600")
    janelacadastropsicologo.resizable(False, False)

    
    label = tk.Label(janelacadastropsicologo, text="Cadastro Psicologo", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)
    ###label e entry do crp
    label_crp = tk.Label(janelacadastropsicologo , text="Informe o crp: ", font=("Calibri (Corpo)", 11))
    label_crp.pack()
    entry_crp = tk.Entry(janelacadastropsicologo)
    entry_crp.pack()
########################################################
    label_emailpsicologo = tk.Label(janelacadastropsicologo , text="Informe o email: ", font=("Calibri (Corpo)", 11))
    label_emailpsicologo.pack()
    entry_emailpsicologo = tk.Entry(janelacadastropsicologo)
    entry_emailpsicologo.pack()
###########################################################
    label_telefonepsicologo = tk.Label(janelacadastropsicologo , text="Informe o telefone de contato: ", font=("Calibri (Corpo)", 11))
    label_telefonepsicologo.pack()
    entry_telefonepsicologo = tk.Entry(janelacadastropsicologo)
    entry_telefonepsicologo.pack()
###########################################################
    label_disponibilidade = tk.Label(janelacadastropsicologo , text='Disponibilidade: ', font=("Calibri (Corpo)", 11))
    label_disponibilidade.pack()
    entry_disponibilidade = tk.Entry(janelacadastropsicologo)
    entry_disponibilidade.pack()
############################################################
    label_enderecopsicologo = tk.Label(janelacadastropsicologo , text='Endereço do Psicologo: ', font=("Calibri (Corpo)", 11))
    label_enderecopsicologo.pack()
    entry_enderecopsicologo = tk.Entry(janelacadastropsicologo)
    entry_enderecopsicologo.pack()
############################################################
    label_nomepsicologo = tk.Label(janelacadastropsicologo , text='Nome do Psicologo:', font=("Calibri (Corpo)", 11))
    label_nomepsicologo.pack()
    entry_nomepsicologo = tk.Entry(janelacadastropsicologo)
    entry_nomepsicologo.pack()
    """ botaocadastropsicologo = tk.Button(janelacadastropsicologo , text='Cadastrar' , command= funcaobotao)
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastropsicologo , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10) """
    def funcaobotao():
        global nome, crp, email, telefone, endereco, disponibibilidade
        nome = entry_nomepsicologo.get()
        crp = entry_crp.get()
        email = entry_emailpsicologo.get()
        telefone = entry_telefonepsicologo.get() #nao pode ser igual
        endereco = entry_enderecopsicologo.get() 
        disponibilidade = entry_disponibilidade.get() # nao pode ser igual 
        
        #statusconvenio = entry_statusconvenio.get()
        
        comandosql =f"SELECT email from paciente Where email = '{email}'"
        cursor.execute(comandosql)
        dados_tabela = cursor.fetchall()
        if any(letras.isalpha() for letras in telefone):
            messagebox.showerror("Erro" , "Telefone contém letras.")
        else:
            print("O número de telefone não contém letras.")
            if len(dados_tabela) >= 1:
                messagebox.showerror("Erro", "Email já existe")

            elif len(dados_tabela) == 0:
                comandosql =f"SELECT telefone from paciente Where telefone = {telefone}"
                cursor.execute(comandosql)
                dados_tabela = cursor.fetchall()
                if len(dados_tabela) >= 1:
                    messagebox.showerror("Erro", "Telefone já existe")
                elif len(dados_tabela) == 0:
                    entry_nomepsicologo.delete(0 , tk.END)
                    entry_emailpsicologo.delete(0 , tk.END)
                    entry_disponibilidade.delete(0 , tk.END)
                    entry_telefonepsicologo.delete(0 , tk.END)
                    entry_enderecopsicologo.delete(0 , tk.END)
                    entry_crp.delete(0 , tk.END)
                    comandosql = f"INSERT INTO psicologos (crp, email, telefone_contato, disponibilidade, endereço_psicologo, nome) VALUES ('{crp}', '{email}', '{telefone}', '{disponibilidade}', '{endereco}' , '{nome}')"
                    cursor.execute(comandosql)
                    conexao_banco.commit()
                    print("Psicologo cadastrado!")
                    messagebox.showinfo("Sucesso!", "Psicologo Cadastrado.")
    botaocadastropsicologo = tk.Button(janelacadastropsicologo , text='Cadastrar' , command= funcaobotao)
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastropsicologo , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10)                                       
                            
def acao_excluir_paciente(janela_excluir):
    def voltar_para_janela_opcoes(): #botei a outra função aqui tbm
        janela_excluir.destroy()  # Fecha a janela de cadastro de paciente
        abrir_proxima_janela()  # Abre a janela de opções

    label_titulo = tk.Label(janela_excluir, text="Selecione qual tipo de Registro deseja Excluir", font=("Calibri (Corpo)", 11))
    label_titulo.pack(pady=30)

    
    pass
                       
                        
def acao_excluir():
    pass 

def acao_pesquisar():
    pass  

def acao_atualizacao():
    pass  
#

def entryconvenio(janela):
    label_nome = tk.Label(janela, text='Nome do Convênio:', font=("Calibri (Corpo)", 11))
    label_nome.pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    label_telefone = tk.Label(janela, text='Telefone:', font=("Calibri (Corpo)", 11))
    label_telefone.pack()
    entry_telefone = tk.Entry(janela)
    entry_telefone.pack()

    label_cobertura = tk.Label(janela, text='Cobertura:', font=("Calibri (Corpo)", 11))
    label_cobertura.pack()
    entry_cobertura = tk.Entry(janela)
    entry_cobertura.pack()

    label_status = tk.Label(janela, text='Status do Convênio:', font=("Calibri (Corpo)", 11))
    label_status.pack()
    entry_status = tk.Entry(janela)
    entry_status.pack()

    buttoncad = tk.Button(janela , text='Cadastrar', command=lambda: cadastroconvenio(janela, entry_nome.get(), entry_telefone.get(), entry_cobertura.get(), entry_status.get()))
    buttoncad.pack(pady=10)

def botaonaoadd(janela_cadastro):
    comandosql =f"INSERT INTO paciente (data_nascimento , email , status , telefone , endereco , cpf , nome , data_cadastro) values ('{data}' , '{email}' , '{status}',{telefone},'{endereco}',{cpf}, '{nome}' , '{dataAgoraCerta}')"
    cursor.execute(comandosql)
    conexao_banco.commit()
    comandosql = f"INSERT INTO convenio (nome_convenio, telefone, cobertura, statusconvenio) values ('null', 'null', 'null', 'não possui')"
    cursor.execute(comandosql)
    conexao_banco.commit()
    print("Paciente cadastrado com sucesso!")
    acao_cadastro_paciente(janela_cadastro)
                   
def cadastropaciente(janela_cadastro):
    comandosql =f"INSERT INTO paciente (data_nascimento , email , status , telefone , endereco , cpf , nome , data_cadastro) values ('{data}' , '{email}' , '{status}',{telefone},'{endereco}',{cpf}, '{nome}' , '{dataAgoraCerta}')"
    cursor.execute(comandosql)
    conexao_banco.commit()
    
    print("Paciente cadastrado com sucesso!")
    acao_cadastro_paciente(janela_cadastro)

def cadastroconvenio(janela, nome_convenio, telefone, cobertura, statusconvenio):
    comandosql = f"INSERT INTO convenio (nome_convenio, telefone, cobertura, statusconvenio) values ('{nome_convenio}', '{telefone}', '{cobertura}', '{statusconvenio}')"
    cursor.execute(comandosql)
    conexao_banco.commit()
    print("Convênio cadastrado com sucesso!")
    ambos(janela)
    


def ambos(janela):
    cadastropaciente(janela)
    acao_cadastro_paciente(janela)


def abrir_proxima_janela():
    janela_bem_vindo.withdraw()  # Esconde a janela de boas-vindas
    
    # Cria a segunda janela
    janela_opcoes = ttk.Window()
    janela_opcoes.title("Menu")
    janela_opcoes.geometry("600x600")
    janela_opcoes.resizable(False, False)  # Impede redimensionamento

    label = tk.Label(janela_opcoes, text="O que deseja fazer?", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    btn_cadastro = tk.Button(janela_opcoes, text="Cadastro", width=20, height=4, command=lambda: cadastro(janela_opcoes))
    btn_cadastro.pack(pady=15)

    btn_excluir = tk.Button(janela_opcoes, text="Excluir", width=20, height=4, command=acao_excluir)
    btn_excluir.pack(pady=15)

    btn_pesquisar = tk.Button(janela_opcoes, text="Pesquisar", width=20, height=4, command=acao_pesquisar)
    btn_pesquisar.pack(pady=15)

    btn_atualizacao = tk.Button(janela_opcoes, text="Atualização", width=20, height=4, command=acao_atualizacao)
    btn_atualizacao.pack(pady=15)

    janela_opcoes.mainloop()

def cadastro(janela_opcoes):
    janela_opcoes.destroy()
    
    # Criar a janela de cadastro
    janela_cadastro = ttk.Window()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("600x600")
    janela_cadastro.resizable(False, False)

    # Pergunta sobre o tipo de cadastro
    label = tk.Label(janela_cadastro, text="Selecione o tipo de Cadastro", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    btn_cadastro_paciente = tk.Button(janela_cadastro, text="Cadastro de Paciente", width=30, height=7, command=lambda: acao_cadastro_paciente(janela_cadastro))
    btn_cadastro_paciente.pack(pady=10)

    btn_cadastro_psicologo = tk.Button(janela_cadastro, text="Cadastro de Psicólogo", width=30, height=7, command=lambda : acao_cadastro_psicologo(janela_cadastro))
    btn_cadastro_psicologo.pack(pady=10)

    btn_cadastro_consulta = tk.Button(janela_cadastro, text="Cadastro Consultas", width=30, height=7, command=lambda : acao_cadastro_psicologo(janela_cadastro))
    btn_cadastro_consulta.pack(pady=10)

    janela_cadastro.mainloop()

"""def janela_excluir():
    janela_opcoes.destroy()
    
    janela_excluir = ttk.Window()
    
    janela_excluir.title("Excluir Paciente")
    janela_excluir.geometry("600x600")
    janela_excluir.resizable(False, False)
    
    label = tk.Label(janela_excluir, text="Selecione o que deseja Excluir: ", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    btn_excluir_paciente = tk.Button(janela_excluir, text="Excluir Paciente", width=30, height=7, command=lambda: acao_excluir_paciente(janela_excluir))
    btn_excluir_paciente.pack(pady=10)

    btn_excluir_psicologo = tk.Button(janela_excluir, text="Excluir Psicólogo", width=30, height=7, command=lambda : acao_excluir_psicologo(janela_excluir))
    btn_excluir_psicologo.pack(pady=10)

    btn_excluir_consulta = tk.Button(janela_excluir, text="Excluir Consulta", width=30, height=7, command=lambda : acao_excluir_consulta(janela_excluir))
    btn_excluir_consulta.pack(pady=10)

    janela_excluir.mainloop()"""

#janela de boas-vindas
janela_bem_vindo = ttk.Window()
janela_bem_vindo.title("Bem-vindo!")
janela_bem_vindo.geometry("600x600")
janela_bem_vindo.resizable(False, False) 

label_bem_vindo = tk.Label(janela_bem_vindo, text="Bem-vindo!", font=("Calibri (Corpo)", 24))
label_bem_vindo.pack(pady=100)

btn_continuar = tk.Button(janela_bem_vindo, text="Continuar", width=20, height=3, command=abrir_proxima_janela)
btn_continuar.pack(pady=10)

# Inicia a janela de boas-vindas
janela_bem_vindo.mainloop()