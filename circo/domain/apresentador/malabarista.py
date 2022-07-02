from circo.interfaces.apresentador import IApresentador


class Malabarista(IApresentador):
    def apresentar_show(self):
        print('Malabarista apresentando seu show.')
