class InterfaceProfissao():
    def atividade(self):
        raise Exception('Método atividade não implementado.')


class Profissao(InterfaceProfissao):
    pass


a = InterfaceProfissao().atividade()
