
import streamlit as st
import pandas as pd 
import datetime
import re
# C:\Users\Ulisses\Desktop\Backup\1. ESTUDOS\A PARTE\PROJETOS\STREAMLIT

arquivo_dados = 'dados/clientes.csv'


# INICIO PROGRAMA :
st.title('Dottore Podologia')


login = st.text_input('Login').lower() # VERIFICAR COM ELE ******************
password = st.text_input('Password', type='password')


# LOGIN ADMIN **
if (login == 'elando' and password == 'elando'):
    st.success(f'Logged {login} account')
    
    # DEPOIS DE LOGAR - TASKS DO SIDEBAR :
    tasks = st.sidebar.selectbox('MENU', ['', 'Dados', 'Controle de Usuários'])
    

    if tasks == '':
        ''

    # DENTRO DE DADOS :
    if tasks == "Dados" :

        tasks2 = st.sidebar.selectbox('OPÇÕES', ['Marcar Consulta', 'Buscar Paciente'])
        
        
        # MARCAR CONSULTA :
        if tasks2 == 'Marcar Consulta' :
            
            st.subheader("Dados da consulta")

            with st.form('Marcar Consulta'):
                
                # CONTAINER 1 : dados pessoais
                c1 = st.container()
                a, b, c = c1.columns([4,2,2])

                nome = a.text_input('Nome').upper()
                tel = b.text_input('Telefone')
                dt_nascimento = c.date_input('Data de Nascimento'
                                            , value=datetime.date(1997,1,1)
                                            , min_value=datetime.date(1900,1,1)
                                            , max_value=datetime.date.today()
                                            , format="DD/MM/YYYY")
                dt_nascimento = dt_nascimento.strftime("%d/%m/%Y")
                email = st.text_input('Email')


                # CONTAINER 2 : dados de endereço
                c2 = st.container()
                aa, bb = c2.columns([4,4])

                logradouro = aa.text_input('Logradouro')
                nro_endereco = bb.number_input('Nº', step=1)
                bairro = aa.text_input('Bairro')
                cidade = bb.text_input('Cidade')


                # CONTAINER 3 : dados da consulta
                c3 = st.container()
                aaa, bbb = c3.columns([6,2])

                profissional = aaa.text_input('Profissional').upper()
                dt_atendimento = bbb.date_input('Data de Atendimento', format="DD/MM/YYYY")
                dt_atendimento = dt_atendimento.strftime("%d/%m/%Y")

                como_nos_encontrou = st.text_input('Como nos encontrou ?')
                obs = st.text_area('Observação')


                if st.form_submit_button('Adicionar'): 
                    lista = [nome, tel, email, dt_nascimento, logradouro, nro_endereco, bairro
                             , cidade, profissional, dt_atendimento, como_nos_encontrou, obs]
                    dados = pd.read_csv(arquivo_dados)
                    ultima_linha = dados.shape[0]
                    dados.loc[ultima_linha] = lista
                    
                    # SALVANDO OS DADOS NO BANCO:
                    dados.to_csv(arquivo_dados, index=False)
                    dados_atualizados = pd.read_csv(arquivo_dados)
                    st.write('Adicionado com sucesso !')


        # BUSCAR PACIENTE :
        elif tasks2 == 'Buscar Paciente':
            
            # FILTRO :
            
            dados = pd.read_csv(arquivo_dados, dtype=str)

            busca_tel = st.sidebar.text_input('Buscar por telefone')
            if st.sidebar.button('Buscar pelo telefone') :
                st.subheader('Ficha do Paciente')
                st.dataframe(dados[dados['tel'] == busca_tel])


            busca_nome = st.sidebar.text_input('Buscar pelo nome').upper()
            if st.sidebar.button('Buscar pelo nome'):
                st.subheader('Ficha do Paciente')
                st.dataframe(dados[dados['nome'] == busca_nome])
                

            if busca_nome == '' and busca_tel == '': 
                dados = pd.read_csv(arquivo_dados, dtype=str)
                st.subheader('Pacientes')
                st.dataframe(dados)


    elif tasks == 'Users Control' : 
        st.write('Não habilitado')

else: 
    st.text('Coloque o login e precione enter !')

