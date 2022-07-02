from circo.interfaces.apresentador import IApresentador


class Dancarino(IApresentador):
    def apresentar_show(self):
        print('Dançarino apresentando seu show.')
