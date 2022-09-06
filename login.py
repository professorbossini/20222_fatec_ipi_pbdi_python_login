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
                usuario.login,
                usuario.senha
            )
    
