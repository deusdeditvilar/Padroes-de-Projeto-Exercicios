# -*- encoding: UTF-8 -*-


class Hoteleiro(object):

    def __init__(self):
        print('Atrás do Hotel para o casamento? --')

    def __is_available(self):
        print('O hotel está vago no dia do evento?')
        return True

    def book_hotel(self):
        if self.__is_available():
            print('Reserva registrada\n')


class Florista(object):

    def __init__(self):
        print('Decoração de flores para o evento? --')

    def set_flower_requirements(self):
        print('Girassois e rosas serão usados para decoração\n')


class Cozinheiro(object):

    def __init__(self):
        print('Comidas para o evento? --')

    def set_cuisine(self):
        print('Canapés e o jantar serão servidos\n')


class Musico(object):

    def __init__(self):
        print('Música para o evento? --')

    def set_music_type(self):
        print('Pop e Jazz serão tocados no evento\n')


class Organizador(object):

    def __init__(self):
        print('Organizador: Deixe-me falar com o pessoal\n')

    @staticmethod
    def arrange():
        hotelier = Hoteleiro()
        hotelier.book_hotel()

        florist = Florista()
        florist.set_flower_requirements()

        caterer = Cozinheiro()
        caterer.set_cuisine()

        musician = Musico()
        musician.set_music_type()


class Cliente(object):

    def __init__(self):
        print('Cliente: Festa de casamento?')

    def ask_event_manager(self):
        print('Cliente: Deixe-me contactar o organizador\n')
        em = Organizador()
        em.arrange()

    def __del__(self):
        print('Cliente: Graças ao Organizador, está tudo pronto!')

if __name__ == "__main__":
    client = Cliente()
    client.ask_event_manager()