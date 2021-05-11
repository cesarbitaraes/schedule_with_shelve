

class Usuario:

    def __init__(self,
                 nome: str,
                 telefone: str,
                 email: str,
                 blog: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._blog = blog

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self._telefone = telefone

    @property
    def blog(self) -> str:
        return self._blog

    @blog.setter
    def blog(self, blog: str) -> None:
        self._blog = blog

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    def __repr__(self):
        return f' Nome: {self._nome}\n Telefone: {self._telefone}\n E-mail: {self._email}\n' \
               f' Blog: {self._blog}\n'
