import shelve

from usuario import Usuario


class DBManager:

    def __init__(self):
        self.bd_name = "local_db"

    def existe_usuario(self, busca: str) -> bool:
        db = shelve.open(self.bd_name)
        try:
            if busca in db.keys():
                return True
            return False
        finally:
            db.close()

    def cadastra_usuario(self, usuario: Usuario) -> None:
        db = shelve.open(self.bd_name)
        try:
            db[usuario.email] = usuario
            print(f'Usuário cadastrado com sucesso: \n{usuario}')
        finally:
            db.close()

    def busca_usuario(self, busca: str) -> None:
        db = shelve.open(self.bd_name)
        try:
            existing = db[busca]
            print(existing)
        except KeyError as e:
            print(f'O usuário informado não existe na Agenda.')
        finally:
            db.close()

    def atualiza_usuario(self, busca: str, dados: dict) -> None:
        db = shelve.open(self.bd_name)
        try:
            usuario = db[busca]
            for dado in dados.keys():
                if dados.get(dado) != '':
                    setattr(usuario, dado, dados.get(dado))
            del db[busca]
            db[usuario.email] = usuario
            print("Usuário atualizado com sucesso: ")
            print(usuario)
        finally:
            db.close()

    def remove_usuario(self, busca: str) -> None:
        db = shelve.open(self.bd_name)
        try:
            if busca in db.keys():
                del db[busca]
                print(f'Usuário de e-mail {busca} removido com sucesso.')
            else:
                print("Usuário informado não existe na Agenda.")
        finally:
            db.close()
