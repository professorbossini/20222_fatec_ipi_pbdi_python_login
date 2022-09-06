import psycopg
class Usuario:
    def __init__ (self, login, senha):
        self.login = login
        self.senha = senha

#definição do método: ele recebe um objeto do tipo Usuario
def existe (usuario):
    #abre a conexão
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20222_pbdi_login",
        user="postgres",
        password="postgres"
    ) as conexao:
        #obtém um cursor
        with conexao.cursor() as cursor:
            #executa o comando
            cursor.execute(
                'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
                (f'{usuario.login}', f'{usuario.senha}')    
            )
            #obter o resultado
            result = cursor.fetchone()
            # if result != None:
            #     return True
            # return False
            # return True if result != None else False
            return result != None

#0 - Sair
#1 - Login
#2 - Logoff
def menu():
    texto = "0-Sair\n1-Login\n2-Logoff\n"
    usuario = None
    op = int(input(texto))
    while op != 0:
        if op == 1:
            login = input('Digite seu login\n')
            senha = input('Digite a sua senha\n')
            usuario = Usuario(login, senha)
            # reescrever esse if usando o operador ternário
            if existe(usuario):
                print("Usuário OK!!!")
            else:
                print("Usuário NOK!!!")
        elif op == 2:
            usuario = None
            print ("Logoff realizado com sucesso!!!")
        op = int(input(texto))
    else:
        print ("Até mais")

menu()
