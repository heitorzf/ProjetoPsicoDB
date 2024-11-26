import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
import mysql.connector
import datetime
from tkinter import messagebox


conexao_banco = mysql.connector.connect(
    host  = '127.0.0.1',
    user = 'root',
    password = 'rato',
    database = 'psicologia'
)
cursor = conexao_banco.cursor()

style = Style(theme='superhero') #style pra nois estiliza nosso tkinter

def isANumber(value):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
        elif len(cpf) == 11:
            
            if status == '' or nome == '' or email == '' or data == '' or telefone == '' or endereco == '' or cpf == '':
                messagebox.showerror('Erro' , 'Campos vazios')
            else:
                if isANumber(telefone) == False:
                    messagebox.showerror('Error' , 'Telefone possui letras')
                    return
                if isANumber(cpf) == False:
                    messagebox.showerror('Error' , 'CPF possui letras')
                    return

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
    janelacadastroconsultas.title("Cadastro Consulta")
    janelacadastroconsultas.geometry("600x600")
    janelacadastroconsultas.resizable(False, False)

    
    label = tk.Label(janelacadastroconsultas, text="Cadastro Consulta", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)
    ###
    label_nomeconsulta = tk.Label(janelacadastroconsultas , text="Informe o nome do paciente: ", font=("Calibri (Corpo)", 11))
    label_nomeconsulta.pack()
    entry_nomeconsulta = tk.Entry(janelacadastroconsultas)
    entry_nomeconsulta.pack()
########################################################
    label_data = tk.Label(janelacadastroconsultas , text="Informe a data da consulta: ", font=("Calibri (Corpo)", 11))
    label_data.pack()
    entry_data = tk.Entry(janelacadastroconsultas)
    entry_data.pack()
###########################################################
    label_preco = tk.Label(janelacadastroconsultas , text="Informe o preço estabelecido da consulta: ", font=("Calibri (Corpo)", 11))
    label_preco.pack()
    entry_preco = tk.Entry(janelacadastroconsultas)
    entry_preco.pack()
###########################################################
    
############################################################
    label_pagamento = tk.Label(janelacadastroconsultas , text='Insira se ele pagou ou não: ', font=("Calibri (Corpo)", 11))
    label_pagamento.pack()
    entry_pagamento = tk.Entry(janelacadastroconsultas)
    entry_pagamento.pack()
############################################################
    label_duracao = tk.Label(janelacadastroconsultas , text='Insira a duração da consulta HH:MM:SS :', font=("Calibri (Corpo)", 11))
    label_duracao.pack()
    entry_duracao = tk.Entry(janelacadastroconsultas)
    entry_duracao.pack()
    ###########################
    label_statusconsulta = tk.Label(janelacadastroconsultas , text='Insira o status da consulta (tratamento/inativo):', font=("Calibri (Corpo)", 11))
    label_statusconsulta.pack()
    entry_statusconsulta = tk.Entry(janelacadastroconsultas)
    entry_statusconsulta.pack()

    
    def funcaobotaoconsulta():
        #global nome, pagamento, data, data_cancelamento, statusconsulta , duracao
        nome = entry_nomeconsulta.get()
        preco = entry_preco.get()
        pagamento = entry_pagamento.get() #pagamento é se foi pago
        data = entry_data.get() #nao pode ser igual
         
        statusconsulta = entry_statusconsulta.get() # nao pode ser igual 
        duracao = entry_duracao.get()
        
        if isANumber(preco):
            print('é um preco valido')
            preco = int(entry_preco.get())
          
            comando_sql = f"SELECT nome from paciente WHERE nome = '{nome}'"
            cursor.execute(comando_sql)
            resultado = cursor.fetchall()
            if len(resultado) <= 0:
                messagebox.showerror('Erro' , 'Paciente inexistente.')
            elif len(resultado) >= 1:
                comando_sql = f'SELECT idconsultas from consultas'
                cursor.execute(comando_sql)
                resultadoid = cursor.fetchall()
                if nome == '' or pagamento == '' or data == '' or statusconsulta == '' or duracao == '':
                    messagebox.showerror('Erro' , 'Campos Vazios')
                else:
                    comando_sql = f"INSERT INTO consultas ( idconsultas , status_consulta , data_cancelamento , duracao , data , pagamento , preço , nome ) values ( {resultadoid[-1][0]+1},'{statusconsulta}' , '2000-01-1 01:01:01' , '{duracao}' , '{data}' , '{pagamento}' , {preco} , '{nome}')"
                    cursor.execute(comando_sql)
                    conexao_banco.commit()
                    messagebox.showinfo('Sucesso' , 'Consulta cadastrada com sucesso!')

        elif isANumber(preco) == False:
            messagebox.showerror('Erro' , 'Não é um valor valido, digite um numero.')



        
        
    botaocadastroconsultas = tk.Button(janelacadastroconsultas , text='Cadastrar' , command= funcaobotaoconsulta)
    botaocadastroconsultas.pack(pady=10)
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
  
    def funcaobotao():
        global nome, crp, email, telefone, endereco 
        nome = entry_nomepsicologo.get()
        crp = entry_crp.get()
        email = entry_emailpsicologo.get()
        telefone = entry_telefonepsicologo.get() #nao pode ser igual
        endereco = entry_enderecopsicologo.get() 
        disponibilidade = entry_disponibilidade.get() # nao pode ser igual 
        
        #statusconvenio = entry_statusconvenio.get()
        
        comandosql =f"SELECT email from paciente where email = '{email}'"
        cursor.execute(comandosql)
        dados_tabela = cursor.fetchall()
        if isANumber(telefone) == False:
            messagebox.showerror("Erro" , "Telefone contém letras.")
        else:
            print("O número de telefone não contém letras.")
            if email == '' or telefone == '' or disponibilidade == '' or endereco == '' or nome == '':
                messagebox.showerror('Erro' , 'Campos Vazios')
            else:
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
                        messagebox.showinfo("Sucesso!", f"Psicologo, {nome} ,Cadastrado.")
    botaocadastropsicologo = tk.Button(janelacadastropsicologo , text='Cadastrar' , command= funcaobotao)
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastropsicologo , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10)                                       
                                                                                                                                                                                                                                                                                                                                                                               
def acao_excluir(janela_opcoes):
    janela_opcoes.destroy()
    

    janela_excluir = ttk.Window()
    janela_excluir.title("Excluir Registro")
    janela_excluir.geometry("600x600")
    janela_excluir.resizable(False, False)

    label = tk.Label(janela_excluir, text="Selecione o que deseja Excluir", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    btn_excluir_paciente = tk.Button(janela_excluir, text="Excluir Paciente", width=30, height=7, 
                                    command=lambda: excluir_paciente(janela_excluir), font=("Calibri (Corpo)", 11))
    btn_excluir_paciente.pack(pady=10)

    btn_excluir_psicologo = tk.Button(janela_excluir, text="Excluir Psicólogo", width=30, height=7,
                                     command=lambda: excluir_psicologo(janela_excluir), font=("Calibri (Corpo)", 11))
    btn_excluir_psicologo.pack(pady=10)

    btn_excluir_consulta = tk.Button(janela_excluir, text="Excluir Consulta", width=30, height=7,
                                    command=lambda: excluir_consulta(janela_excluir), font=("Calibri (Corpo)", 11))
    btn_excluir_consulta.pack(pady=10)

    btn_voltar = tk.Button(janela_excluir, text="Voltar", command=lambda: voltar_menu(janela_excluir), font=("Calibri (Corpo)", 11))
    btn_voltar.pack(pady=10)

def voltar_menu(janela_atual):
    janela_atual.destroy()
    abrir_proxima_janela()

def excluir_paciente(janela_excluir):
    janela_excluir.destroy()
    
    # cria a janela
    janela_excluir_paciente = ttk.Window()
    janela_excluir_paciente.title("Excluir Paciente")
    janela_excluir_paciente.geometry("600x600")
    janela_excluir_paciente.resizable(False, False)

    label = tk.Label(janela_excluir_paciente, text="Excluir Paciente", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    # input do cpf
    label_cpf = tk.Label(janela_excluir_paciente, text="CPF do Paciente:", font=("Calibri (Corpo)", 11))
    label_cpf.pack()
    entry_cpf = tk.Entry(janela_excluir_paciente)
    entry_cpf.pack()

    # input do idconveio
    label_convenio = tk.Label(janela_excluir_paciente, text="ID do Convênio:", font=("Calibri (Corpo)", 11))
    label_convenio.pack()
    entry_convenio = tk.Entry(janela_excluir_paciente)
    entry_convenio.pack()

    def confirmar_exclusao():
        cpf = entry_cpf.get()
        id_convenio = entry_convenio.get()
        
        # valida cpf
        if len(cpf) != 11:
            messagebox.showerror("Erro", "CPF inválido! Deve conter 11 dígitos.")
            return
            
        if not cpf.isdigit():
            messagebox.showerror("Erro", "CPF deve conter apenas números!")
            return

        # Valida o idconvenio
        if not id_convenio.isdigit():
            messagebox.showerror("Erro", "ID do convênio deve ser um número!")
            return
            
        # Checa se o paciente existe e pega o nome
        comandosql = f"SELECT nome FROM paciente WHERE cpf = '{cpf}'"
        cursor.execute(comandosql)
        resultado = cursor.fetchone()
        
        if not resultado:
            messagebox.showerror("Erro", "Paciente não encontrado!")
            return
            
        # Vai checar se o convenio realmente existe
        comandosql = f"SELECT idconvenio FROM convenio WHERE idconvenio = {id_convenio}"
        cursor.execute(comandosql)
        resultado_convenio = cursor.fetchone()
        
        if not resultado_convenio:
            messagebox.showerror("Erro", "Convênio não encontrado ou não pertence a este paciente!")
            return
            
        nome_paciente = resultado[0]
        confirma = messagebox.askyesno("Confirmar Exclusão", 
                                     f"Tem certeza que deseja excluir o paciente {nome_paciente}, suas consultas e seu convênio?")
        
        if confirma:
            try:
                cursor.execute("START TRANSACTION")
                
                # Primeiro exclui as consultas do paciente
                comandosql = f"DELETE FROM consultas WHERE nome = '{nome_paciente}'"
                cursor.execute(comandosql)
                
                # Depois exclui o convênio
                comandosql = f"DELETE FROM convenio WHERE idconvenio = {id_convenio}"
                cursor.execute(comandosql)
                
                # Por último exclui o paciente
                comandosql = f"DELETE FROM paciente WHERE cpf = '{cpf}'"
                cursor.execute(comandosql)
                
                conexao_banco.commit()
                
                messagebox.showinfo("Sucesso", "Paciente, consultas e convênio excluídos com sucesso!")
                entry_cpf.delete(0, tk.END)
                entry_convenio.delete(0, tk.END)
                
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao excluir registros: {err}")
                conexao_banco.rollback()

    btn_confirmar = tk.Button(janela_excluir_paciente, text="Confirmar Exclusão", command=confirmar_exclusao)
    btn_confirmar.pack(pady=20)

    btn_voltar = tk.Button(janela_excluir_paciente, text="Voltar", command=lambda: voltar_menu(janela_excluir_paciente))
    btn_voltar.pack(pady=10)
    
def excluir_psicologo(janela_excluir):
    janela_excluir.destroy()
    
    janela_excluir_psicologo = ttk.Window()
    janela_excluir_psicologo.title("Excluir Psicólogo")
    janela_excluir_psicologo.geometry("600x600")
    janela_excluir_psicologo.resizable(False, False)

    label = tk.Label(janela_excluir_psicologo, text="Excluir Psicólogo", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_crp = tk.Label(janela_excluir_psicologo, text="CRP do Psicólogo:", font=("Calibri (Corpo)", 11))
    label_crp.pack()
    entry_crp = tk.Entry(janela_excluir_psicologo)
    entry_crp.pack()

    def confirmar_exclusao():
        crp = entry_crp.get()
        
        if not crp:
            messagebox.showerror("Erro", "Por favor, insira o CRP!")
            return
            
        
        comandosql = f"SELECT nome FROM psicologos WHERE crp = '{crp}'"
        cursor.execute(comandosql)
        resultado = cursor.fetchone() #é usada para recuperar a próxima linha de um conjunto de resultados de uma consulta e retornar uma única sequência
        
        if not resultado:
            messagebox.showerror("Erro", "Psicólogo não encontrado!")
            return
            
        # Ask for confirmation
        nome_psicologo = resultado[0]
        confirma = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o psicólogo {nome_psicologo}?")
        
        if confirma:
            try:
                comandosql = f"DELETE FROM psicologos WHERE crp = '{crp}'"
                cursor.execute(comandosql)
                conexao_banco.commit()
                
                messagebox.showinfo("Sucesso", "Psicólogo excluído com sucesso!")
                entry_crp.delete(0, tk.END)
                
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao excluir psicólogo: {err}")
                conexao_banco.rollback()

    btn_confirmar = tk.Button(janela_excluir_psicologo, text="Confirmar Exclusão", command=confirmar_exclusao)
    btn_confirmar.pack(pady=20)

    btn_voltar = tk.Button(janela_excluir_psicologo, text="Voltar", command=lambda: voltar_menu(janela_excluir_psicologo))
    btn_voltar.pack(pady=10)

def excluir_consulta(janela_excluir):
    janela_excluir.destroy()
    
    janela_excluir_consulta = ttk.Window()
    janela_excluir_consulta.title("Excluir Consulta")
    janela_excluir_consulta.geometry("600x600")
    janela_excluir_consulta.resizable(False, False)

    label = tk.Label(janela_excluir_consulta, text="Excluir Consulta", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_id = tk.Label(janela_excluir_consulta, text="ID da Consulta:", font=("Calibri (Corpo)", 11))
    label_id.pack()
    entry_id = tk.Entry(janela_excluir_consulta)
    entry_id.pack()

    def confirmar_exclusao():
        id_consulta = entry_id.get()
        
        if not id_consulta.isdigit():
            messagebox.showerror("Erro", "ID da consulta deve ser um número!")
            return
        comandosql = f"SELECT data FROM consultas WHERE idconsultas = {id_consulta}"
        cursor.execute(comandosql)
        resultado = cursor.fetchone()
        
        if not resultado:
            messagebox.showerror("Erro", "Consulta não encontrada!")
            return
        
        data_consulta = resultado[0]
        confirma = messagebox.askyesno("Confirmar Exclusão",  f"Tem certeza que deseja excluir a consulta do dia {data_consulta}?")
        
        if confirma:
            try:
                comandosql = f"DELETE FROM consultas WHERE id_consulta = {id_consulta}"
                cursor.execute(comandosql)
                conexao_banco.commit()
                
                messagebox.showinfo("Sucesso", "Consulta excluída com sucesso!")
                entry_id.delete(0, tk.END)
                
            except mysql.connector.Error as err:
                messagebox.showerror("Erro", f"Erro ao excluir consulta: {err}")
                conexao_banco.rollback()

    btn_confirmar = tk.Button(janela_excluir_consulta, text="Confirmar Exclusão", 
                             command=confirmar_exclusao)
    btn_confirmar.pack(pady=20)

    btn_voltar = tk.Button(janela_excluir_consulta, text="Voltar", 
                          command=lambda: voltar_menu(janela_excluir_consulta))
    btn_voltar.pack(pady=10)
     

def acao_pesquisar(janela_opcoes):
    janela_opcoes.destroy()

    janela_pesquisar = ttk.Window()
    janela_pesquisar.title("Pesquisar Registro")
    janela_pesquisar.geometry("600x600")
    janela_pesquisar.resizable(False, False)

    label = tk.Label(janela_pesquisar, text="Selecione o que deseja Pesquisar", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    btn_pesquisar_paciente = tk.Button(janela_pesquisar, text="Pesquisar Paciente", width=30, height=7, 
command=lambda: pesquisar_paciente(janela_pesquisar), font=("Calibri (Corpo)", 11))
    btn_pesquisar_paciente.pack(pady=10)

    btn_pesquisar_psicologo = tk.Button(janela_pesquisar, text="Pesquisar Psicólogo", width=30, height=7,command=lambda: pesquisar_psicologo(janela_pesquisar), font=("Calibri (Corpo)", 11))
    btn_pesquisar_psicologo.pack(pady=10)

    btn_pesquisar_consulta = tk.Button(janela_pesquisar, text="Pesquisar Consulta", width=30, height=7,command=lambda: pesquisar_consulta(janela_pesquisar), font=("Calibri (Corpo)", 11))
    btn_pesquisar_consulta.pack(pady=10)
    
    btn_voltar = tk.Button(janela_pesquisar, text="Voltar", command=lambda: voltar_menu(janela_pesquisar), font=("Calibri (Corpo)", 11))
    btn_voltar.pack(pady=10)

def pesquisar_paciente(janela_pesquisar):
    janela_pesquisar.destroy()
    
    janela_pesquisa_paciente = ttk.Window()
    janela_pesquisa_paciente.title("Pesquisar Paciente")
    janela_pesquisa_paciente.geometry("600x600")
    janela_pesquisa_paciente.resizable(False, False)

    label = tk.Label(janela_pesquisa_paciente, text="Pesquisar Paciente", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_cpf = tk.Label(janela_pesquisa_paciente, text="CPF do Paciente:", font=("Calibri (Corpo)", 11))
    label_cpf.pack()
    entry_cpf = tk.Entry(janela_pesquisa_paciente)
    entry_cpf.pack()

    def realizar_pesquisa():
        cpf = entry_cpf.get()
        
        if len(cpf) != 11:
            messagebox.showerror("Erro", "CPF inválido! Deve conter 11 dígitos.")
        else:
            if not cpf.isdigit():
                messagebox.showerror("Erro", "CPF deve conter apenas números!")
            else:
                comandosql = f"""
                    SELECT p.idpaciente, p.data_nascimento, p.email, p.data_cadastro, p.status, p.telefone, p.endereco, p.cpf, p.nome,c.nome_convenio, c.telefone as tel_convenio, c.cobertura, c.statusconvenio FROM paciente p LEFT JOIN convenio c ON c.idconvenio = p.idpaciente WHERE p.cpf = '{cpf}'
                """
                cursor.execute(comandosql)
                resultado = cursor.fetchone()
            
        if not resultado:
            messagebox.showerror("Erro", "Paciente não encontrado!")
            return
            
        # Criar uma nova janela para mostrar os resultados
        resultado_window = ttk.Window()
        resultado_window.title("Resultado da Pesquisa")
        resultado_window.geometry("400x500")
        
        # Mostrar os dados do paciente na ordem especificada
        tk.Label(resultado_window, text="Dados do Paciente", font=("Calibri (Corpo)", 16)).pack(pady=10)
        tk.Label(resultado_window, text=f"ID Paciente: {resultado[0]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Data de Nascimento: {resultado[1]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Email: {resultado[2]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Data de Cadastro: {resultado[3]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Status: {resultado[4]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Telefone: {resultado[5]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Endereço: {resultado[6]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"CPF: {resultado[7]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Nome: {resultado[8]}", font=("Calibri (Corpo)", 11)).pack()
        
        # Mostrar dados do convênio se existir
        if resultado[9]:  # Se há dados do convênio
            tk.Label(resultado_window, text="\nDados do Convênio", font=("Calibri (Corpo)", 16)).pack(pady=10)
            tk.Label(resultado_window, text=f"Nome do Convênio: {resultado[9]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Telefone do Convênio: {resultado[10]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Cobertura: {resultado[11]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Status do Convênio: {resultado[12]}", font=("Calibri (Corpo)", 11)).pack()

    btn_pesquisar = tk.Button(janela_pesquisa_paciente, text="Pesquisar", command=realizar_pesquisa)
    btn_pesquisar.pack(pady=20)

    btn_voltar = tk.Button(janela_pesquisa_paciente, text="Voltar", command=lambda: voltar_menu(janela_pesquisa_paciente))
    btn_voltar.pack(pady=10)
def pesquisar_psicologo(janela_pesquisar):
    janela_pesquisar.destroy()
    
    janela_pesquisa_psicologo = ttk.Window()
    janela_pesquisa_psicologo.title("Pesquisar Psicólogo")
    janela_pesquisa_psicologo.geometry("600x600")
    janela_pesquisa_psicologo.resizable(False, False)

    label = tk.Label(janela_pesquisa_psicologo, text="Pesquisar Psicólogo", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_crp = tk.Label(janela_pesquisa_psicologo, text="CRP do Psicólogo:", font=("Calibri (Corpo)", 11))
    label_crp.pack()
    entry_crp = tk.Entry(janela_pesquisa_psicologo)
    entry_crp.pack()

    def realizar_pesquisa():
        crp = entry_crp.get()
        
        if not crp:
            messagebox.showerror("Erro", "Por favor, insira o CRP!")
            return
            
        comandosql = f"SELECT * FROM psicologos WHERE crp = '{crp}'"
        cursor.execute(comandosql)
        resultado = cursor.fetchone()
        
        if not resultado:
            messagebox.showerror("Erro", "Psicólogo não encontrado!")
            return
            
        # Criar uma nova janela para mostrar os resultados
        resultado_window = ttk.Window()
        resultado_window.title("Resultado da Pesquisa")
        resultado_window.geometry("400x300")
        
        tk.Label(resultado_window, text="Dados do Psicólogo", font=("Calibri (Corpo)", 16)).pack(pady=10)
        tk.Label(resultado_window, text=f"Nome: {resultado[5]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"CRP: {resultado[0]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Email: {resultado[1]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Telefone: {resultado[2]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Disponibilidade: {resultado[3]}", font=("Calibri (Corpo)", 11)).pack()
        tk.Label(resultado_window, text=f"Endereço: {resultado[4]}", font=("Calibri (Corpo)", 11)).pack()

    btn_pesquisar = tk.Button(janela_pesquisa_psicologo, text="Pesquisar", command=realizar_pesquisa)
    btn_pesquisar.pack(pady=20)

    btn_voltar = tk.Button(janela_pesquisa_psicologo, text="Voltar", command=lambda: voltar_menu(janela_pesquisa_psicologo))
    btn_voltar.pack(pady=10)
def pesquisar_consulta(janela_pesquisar):
    janela_pesquisar.destroy()
    
    janela_pesquisa_consulta = tk.Tk()
    janela_pesquisa_consulta.title("Pesquisar Consulta")
    janela_pesquisa_consulta.geometry("600x600")
    janela_pesquisa_consulta.resizable(False, False)

    label = tk.Label(janela_pesquisa_consulta, text="Pesquisar Consulta", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    label_nome = tk.Label(janela_pesquisa_consulta, text="Nome do Paciente:", font=("Calibri (Corpo)", 11))
    label_nome.pack()
    entry_nome = tk.Entry(janela_pesquisa_consulta)
    entry_nome.pack()

    def realizar_pesquisa():
        nome = entry_nome.get()
        
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira o nome do paciente!")
            return
            
        comandosql = f"SELECT * FROM consultas WHERE nome = '{nome}'"
        cursor.execute(comandosql)
        resultados = cursor.fetchall()
        
        if not resultados:
            messagebox.showerror("Erro", "Nenhuma consulta encontrada para este paciente!")
            return
        
        # Criar uma nova janela para mostrar os resultados
        resultado_window = tk.Tk()
        resultado_window.title("Resultado da Pesquisa")
        resultado_window.geometry("600x600")
        
        tk.Label(resultado_window, text=f"Consultas de {nome}", font=("Calibri (Corpo)", 16)).pack(pady=10)
        
        for consulta in resultados:
            tk.Label(resultado_window, text=f"ID: {consulta[0]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Status: {consulta[1]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Data: {consulta[4]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Duração: {consulta[3]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Pagamento: {consulta[5]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text=f"Preço: R${consulta[6]}", font=("Calibri (Corpo)", 11)).pack()
            tk.Label(resultado_window, text="-" * 60, font=("Calibri (Corpo)", 11)).pack()

    btn_pesquisar = tk.Button(janela_pesquisa_consulta, text="Pesquisar", command=realizar_pesquisa)
    btn_pesquisar.pack(pady=20)

    btn_voltar = tk.Button(janela_pesquisa_consulta, text="Voltar", command=lambda: voltar_menu(janela_pesquisa_consulta))
    btn_voltar.pack(pady=10)

def acao_atualizacao(janela_opcoes):
    janela_opcoes.destroy()

    janela_atualizacao = ttk.Window()
    janela_atualizacao.title("Atualizar Registro")
    janela_atualizacao.geometry("600x600")
    janela_atualizacao.resizable(False, False)

    label = tk.Label(janela_atualizacao, text="Selecione o que deseja Atualizar", font=("Calibri (Corpo)", 20))
    label.pack(pady=30)

    def atualizar_status_convenio():
        janela = ttk.Window()
        janela.title("Atualizar Status do Convênio")
        janela.geometry("400x300")

        tk.Label(janela, text="ID do Convênio:", font=("Calibri (Corpo)", 11)).pack()
        entry_id_convenio = tk.Entry(janela)
        entry_id_convenio.pack()

        tk.Label(janela, text="Novo Status (Ativo/Inativo):", font=("Calibri (Corpo)", 11)).pack()
        entry_status_convenio = tk.Entry(janela)
        entry_status_convenio.pack()

        def confirmar_atualizacao():
            id_convenio = entry_id_convenio.get()
            status = entry_status_convenio.get().strip().capitalize()
            if id_convenio == '' or status == '':
                messagebox.showerror('Erro' , 'Campos Vazios')
                return
            if not id_convenio.isdigit():
                messagebox.showerror("Erro", "ID do Convênio deve ser numérico.")
                return

            if status not in ["Ativo", "Inativo"]:
                messagebox.showerror("Erro", "Status inválido. Use 'Ativo' ou 'Inativo'.")
                return

            comandosql = f"UPDATE convenio SET statusconvenio = '{status}' WHERE idconvenio = {id_convenio}"
            cursor.execute(comandosql)
            conexao_banco.commit()

            if cursor.rowcount > 0: #cursor.rowcount > 0, significa que a consult afetou ou encontrou pelo menos uma linha por exemplo um convênio foi encontrado e atualizado no sql
                messagebox.showinfo("Sucesso", "Status do Convênio atualizado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum convênio encontrado com o ID fornecido.")

        btn_confirmar = tk.Button(janela, text="Atualizar", command=confirmar_atualizacao)
        btn_confirmar.pack(pady=10)

    def atualizar_status_paciente():
        janela = ttk.Window()
        janela.title("Atualizar Status do Paciente")
        janela.geometry("400x300")

        tk.Label(janela, text="CPF do Paciente:", font=("Calibri (Corpo)", 11)).pack()
        entry_cpf_paciente = tk.Entry(janela)
        entry_cpf_paciente.pack()

        tk.Label(janela, text="Novo Status (Ativo/Inativo):", font=("Calibri (Corpo)", 11)).pack()
        entry_status_paciente = tk.Entry(janela)
        entry_status_paciente.pack()

        def confirmar_atualizacao():
            cpf = entry_cpf_paciente.get()
            status = entry_status_paciente.get().strip()
            if cpf == '' or status == '':
                messagebox.showerror('Erro' , 'Campos Vazios!')
                return
            if not cpf.isdigit() or len(cpf) != 11:
                messagebox.showerror("Erro", "CPF inválido. Deve conter 11 dígitos numéricos.")
                return

            if status not in ["Ativo", "Inativo"]:
                messagebox.showerror("Erro", "Status inválido. Use 'Ativo' ou 'Inativo'.")
                return

            comandosql = f"UPDATE paciente SET status = '{status}' WHERE cpf = '{cpf}'"
            cursor.execute(comandosql)
            conexao_banco.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", "Status do Paciente atualizado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum paciente encontrado com o CPF fornecido.")

        btn_confirmar = tk.Button(janela, text="Atualizar", command=confirmar_atualizacao)
        btn_confirmar.pack(pady=10)

    def atualizar_data_cancelamento():
        janela = ttk.Window()
        janela.title("Atualizar Data de Cancelamento")
        janela.geometry("400x300")

        tk.Label(janela, text="ID da Consulta:", font=("Calibri (Corpo)", 11)).pack()
        entry_id_consulta = tk.Entry(janela)
        entry_id_consulta.pack()

        tk.Label(janela, text="Nova Data de Cancelamento (AAAA-MM-DD HH:MM:SS):", font=("Calibri (Corpo)", 11)).pack()
        entry_data_cancelamento = tk.Entry(janela)
        entry_data_cancelamento.pack()

        def confirmar_atualizacao():
            id_consulta = entry_id_consulta.get()
            data_cancelamento = entry_data_cancelamento.get()
            if data_cancelamento == '' or id_consulta == '':
                messagebox.showerror('Erro' , 'Campos Vazios')
                return
            if not id_consulta.isdigit():
                messagebox.showerror("Erro", "ID da Consulta deve ser numérico.")
                return

            comandosql = f"UPDATE consultas SET data_cancelamento = '{data_cancelamento}' WHERE idconsultas = {id_consulta}"
            cursor.execute(comandosql)
            conexao_banco.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", "Data de Cancelamento atualizada com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhuma consulta encontrada com o ID fornecido.")

        btn_confirmar = tk.Button(janela, text="Atualizar", command=confirmar_atualizacao)
        btn_confirmar.pack(pady=10)

    def atualizar_disponibilidade_psicologo():
        janela = ttk.Window()
        janela.title("Atualizar Disponibilidade do Psicólogo")
        janela.geometry("400x300")

        tk.Label(janela, text="CRP do Psicólogo:", font=("Calibri (Corpo)", 11)).pack()
        entry_crp_psicologo = tk.Entry(janela)
        entry_crp_psicologo.pack()

        tk.Label(janela, text="Nova Disponibilidade (Sim/Não):", font=("Calibri (Corpo)", 11)).pack()
        entry_disponibilidade = tk.Entry(janela)
        entry_disponibilidade.pack()

        def confirmar_atualizacao():
            crp = entry_crp_psicologo.get()
            disponibilidade = entry_disponibilidade.get().strip().capitalize()

            if not crp:
                messagebox.showerror("Erro", "CRP não pode estar vazio.")
                return

            if disponibilidade not in ["Sim", "Não"]:
                messagebox.showerror("Erro", "Disponibilidade inválida. Use 'Sim' ou 'Não'.")
                return

            comandosql = f"UPDATE psicologos SET disponibilidade = '{disponibilidade}' WHERE crp = '{crp}'"
            cursor.execute(comandosql)
            conexao_banco.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", "Disponibilidade do Psicólogo atualizada com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum psicólogo encontrado com o CRP fornecido.")

        btn_confirmar = tk.Button(janela, text="Atualizar", command=confirmar_atualizacao)
        btn_confirmar.pack(pady=10)

    # Botões para cada funcionalidade
    btn_convenio = tk.Button(janela_atualizacao, text="Atualizar Status do Convênio", command=atualizar_status_convenio , width=30 , height=5)
    btn_convenio.pack(pady=10)

    btn_paciente = tk.Button(janela_atualizacao, text="Atualizar Status do Paciente", command=atualizar_status_paciente , width=30 , height=5)
    btn_paciente.pack(pady=10)

    btn_consulta = tk.Button(janela_atualizacao, text="Atualizar Data de Cancelamento", command=atualizar_data_cancelamento , width=30 , height=5)
    btn_consulta.pack(pady=10)

    btn_psicologo = tk.Button(janela_atualizacao, text="Atualizar Disponibilidade do Psicólogo", command=atualizar_disponibilidade_psicologo , width=30 , height=5)
    btn_psicologo.pack(pady=10)

    btn_voltar = tk.Button(janela_atualizacao, text="Voltar", command=lambda: voltar_menu(janela_atualizacao))
    btn_voltar.pack(pady=10)

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
    comandosql = f"INSERT INTO convenio (nome_convenio, telefone, cobertura, statusconvenio) values ('null', 'null', '0', 'não possui')"
    cursor.execute(comandosql)
    conexao_banco.commit()
    messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso!")
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
    messagebox.showinfo("Sucesso", "Convênio cadastrado com sucesso!")
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

    btn_excluir = tk.Button(janela_opcoes, text="Excluir", width=20, height=4, command=lambda : acao_excluir(janela_opcoes))
    btn_excluir.pack(pady=15)

    btn_pesquisar = tk.Button(janela_opcoes, text="Pesquisar", width=20, height=4, command=lambda : acao_pesquisar(janela_opcoes))
    btn_pesquisar.pack(pady=15)

    btn_atualizacao = tk.Button(janela_opcoes, text="Atualização", width=20, height=4, command=lambda : acao_atualizacao(janela_opcoes))
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

    btn_cadastro_consulta = tk.Button(janela_cadastro, text="Cadastro Consultas", width=30, height=7, command=lambda : acao_cadastro_consultas(janela_cadastro))
    btn_cadastro_consulta.pack(pady=10)

    janela_cadastro.mainloop()



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