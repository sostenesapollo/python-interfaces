from circo.domain.apresentador.dancarino import Dancarino
from circo.domain.apresentador.malabarista import Malabarista
from circo.domain.apresentador.palhaco import Palhaco


def main():

    dancarinho, malabarista, palhaco = Dancarino(), Malabarista(), Palhaco()

    dancarinho.apresentar_show()
    malabarista.apresentar_show()
    palhaco.apresentar_show()


if __name__ == '__main__':
    main()
