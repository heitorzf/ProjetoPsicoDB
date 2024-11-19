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



def acao_cadastro_paciente(janela_cadastro):
    
    janela_cadastro.destroy()
    
    # Criar a janela de cadastro de paciente
    cadastropacientejanela = ttk.Window()
    
    cadastropacientejanela.title("Cadastro Paciente")
    cadastropacientejanela.geometry("600x600")
    cadastropacientejanela.resizable(False, False)

    # Pergunta sobre o tipo de cadastro
    label = tk.Label(cadastropacientejanela, text="Cadastro de Paciente", font=("Arial", 20))
    label.pack(pady=30)

    label_nome = tk.Label(cadastropacientejanela, text="Nome:")
    label_nome.pack()

    entry_nome = tk.Entry(cadastropacientejanela)
    entry_nome.pack()

    label_email = tk.Label(cadastropacientejanela, text="Email:")
    label_email.pack()

    entry_email = tk.Entry(cadastropacientejanela)
    entry_email.pack()

    label_dataNascimento = tk.Label(cadastropacientejanela, text="Data De Nascimento (AAAA-MM-DD):")
    label_dataNascimento.pack()

    entry_dataNascimento = tk.Entry(cadastropacientejanela)
    entry_dataNascimento.pack()
    
    
    label_telefone = tk.Label(cadastropacientejanela, text="Telefone Paciente:")
    label_telefone.pack()

    entry_telefone = tk.Entry(cadastropacientejanela)
    entry_telefone.pack()

    label_endereco = tk.Label(cadastropacientejanela, text="Endereço Paciente:")
    label_endereco.pack()

    entry_endereco = tk.Entry(cadastropacientejanela)
    entry_endereco.pack()

    label_cpf = tk.Label(cadastropacientejanela, text="CPF Paciente :")
    label_cpf.pack()

    entry_cpf = tk.Entry(cadastropacientejanela)
    entry_cpf.pack()

    label_status = tk.Label(cadastropacientejanela, text="STATUS Paciente :")
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
        label_convenio = tk.Label(cadastroconveniojanela, text="Cadastro de Convênio", font=("Arial", 20))
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

def acao_cadastro_psicologo(janela_cadastro):
    def voltar_para_janela_opcoes(): #botei a outra função aqui tbm
        janelacadastropsicologo.destroy()  # Fecha a janela de cadastro de paciente
        abrir_proxima_janela()  # Abre a janela de opções
        
    janela_cadastro.destroy()
    janelacadastropsicologo = ttk.Window()
    janelacadastropsicologo.title("Cadastro Psicologo")
    janelacadastropsicologo.geometry("600x600")
    janelacadastropsicologo.resizable(False, False)

    
    label = tk.Label(janelacadastropsicologo, text="Cadastro Psicologo", font=("Arial", 20))
    label.pack(pady=30)
    ###label e entry do crm
    label_crm = tk.Label(janelacadastropsicologo , text="Informe o crm: ")
    label_crm.pack()
    entry_crm = tk.Entry(janelacadastropsicologo)
    entry_crm.pack()
########################################################
    label_emailpsicologo = tk.Label(janelacadastropsicologo , text="Informe o email: ")
    label_emailpsicologo.pack()
    entry_emailpsicologo = tk.Entry(janelacadastropsicologo)
    entry_emailpsicologo.pack()
###########################################################
    label_telefonepsicologo = tk.Label(janelacadastropsicologo , text="Informe o telefone de contato: ")
    label_telefonepsicologo.pack()
    entry_telefonepsicologo = tk.Entry(janelacadastropsicologo)
    entry_telefonepsicologo.pack()
###########################################################
    label_disponibilidade = tk.Label(janelacadastropsicologo , text='Disponibilidade: ')
    label_disponibilidade.pack()
    entry_disponibilidade = tk.Entry(janelacadastropsicologo)
    entry_disponibilidade.pack()
############################################################
    label_enderecopsicologo = tk.Label(janelacadastropsicologo , text='Endereço do Psicologo: ')
    label_enderecopsicologo.pack()
    entry_enderecopsicologo = tk.Entry(janelacadastropsicologo)
    entry_enderecopsicologo.pack()
############################################################
    label_nomepsicologo = tk.Label(janelacadastropsicologo , text='Nome do Psicologo:')
    label_nomepsicologo.pack()
    entry_nomepsicologo = tk.Entry(janelacadastropsicologo)
    entry_nomepsicologo.pack()
    botaocadastropsicologo = tk.Button(janelacadastropsicologo , text='Cadastrar')
    botaocadastropsicologo.pack(pady=10)
    botaovoltar = tk.Button(janelacadastropsicologo , text='Voltar', command=voltar_para_janela_opcoes )
    botaovoltar.pack(pady=10)

def acao_excluir():
    pass 

def acao_pesquisar():
    pass  

def acao_atualizacao():
    pass  
#

def entryconvenio(janela):
    label_nome = tk.Label(janela, text='Nome do Convênio:')
    label_nome.pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    label_telefone = tk.Label(janela, text='Telefone:')
    label_telefone.pack()
    entry_telefone = tk.Entry(janela)
    entry_telefone.pack()

    label_cobertura = tk.Label(janela, text='Cobertura:')
    label_cobertura.pack()
    entry_cobertura = tk.Entry(janela)
    entry_cobertura.pack()

    label_status = tk.Label(janela, text='Status do Convênio:')
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

    label = tk.Label(janela_opcoes, text="O que deseja fazer?", font=("Arial", 20))
    label.pack(pady=30)

    btn_cadastro = tk.Button(janela_opcoes, text="Cadastro", width=20, height=2, command=lambda: cadastro(janela_opcoes))
    btn_cadastro.pack(pady=10)

    btn_excluir = tk.Button(janela_opcoes, text="Excluir", width=20, height=2, command=acao_excluir)
    btn_excluir.pack(pady=10)

    btn_pesquisar = tk.Button(janela_opcoes, text="Pesquisar", width=20, height=2, command=acao_pesquisar)
    btn_pesquisar.pack(pady=10)

    btn_atualizacao = tk.Button(janela_opcoes, text="Atualização", width=20, height=2, command=acao_atualizacao)
    btn_atualizacao.pack(pady=10)

    janela_opcoes.mainloop()

def cadastro(janela_opcoes):
    janela_opcoes.destroy()
    
    # Criar a janela de cadastro
    janela_cadastro = ttk.Window()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("600x600")
    janela_cadastro.resizable(False, False)

    # Pergunta sobre o tipo de cadastro
    label = tk.Label(janela_cadastro, text="Selecione o tipo de Cadastro", font=("Arial", 20))
    label.pack(pady=30)

    btn_cadastro_paciente = tk.Button(janela_cadastro, text="Cadastro de Paciente", width=30, height=7, command=lambda: acao_cadastro_paciente(janela_cadastro))
    btn_cadastro_paciente.pack(pady=10)

    btn_cadastro_psicologo = tk.Button(janela_cadastro, text="Cadastro de Psicólogo", width=30, height=7, command=lambda : acao_cadastro_psicologo(janela_cadastro))
    btn_cadastro_psicologo.pack(pady=10)

    janela_cadastro.mainloop()

#janela de boas-vindas
janela_bem_vindo = ttk.Window()
janela_bem_vindo.title("Bem-vindo!")
janela_bem_vindo.geometry("1200x720")
janela_bem_vindo.resizable(False, False) 

label_bem_vindo = tk.Label(janela_bem_vindo, text="Bem-vindo!", font=("Arial", 24))
label_bem_vindo.pack(pady=200)

btn_continuar = tk.Button(janela_bem_vindo, text="Continuar", width=20, height=2, command=abrir_proxima_janela)
btn_continuar.pack(pady=10)

# Inicia a janela de boas-vindas
janela_bem_vindo.mainloop()