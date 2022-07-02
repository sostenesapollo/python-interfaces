from circo.interfaces.apresentador import IApresentador


class Palhaco(IApresentador):
    def apresentar_show(self):
        print('Palhaço apresentando seu show.')
