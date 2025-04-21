import streamlit as st

#função criada para validar os dados

@st.dialog('Alert')
def login_validation(usr, passw):
     if usr == '' or passw == '':
        st.error("Preencha todos os campos por favor!")
     else:
        st.success("Login Concluído.")

# utilizei o comando with para abrir os input dos formulários.

with st.form("Fazer Login"):
     st.title("Fazer Login")
     st.divider()
     username = st.text_input("E-mail")
     password = st.text_input("Senha", type="password")

#variáveis que foram criadas para armazenar os dados dos botões

     login_btn = st.form_submit_button(label="Login", type="primary", use_container_width=True)
     google_btn = st.form_submit_button(label="Fazer login com o google", type="secondary", use_container_width=True, icon=":material/mail:")

     save_dados = st.checkbox("Salvar dados")
     recuperate_dados = st.html('<a href="https://google.com/">Esqueceu a senha?</a>')
     create_btn = st.form_submit_button(label="Crie uma conta", type="secondary", use_container_width=True)

#chamando a função login_validation
     if login_btn:
          login_validation(username, password)






