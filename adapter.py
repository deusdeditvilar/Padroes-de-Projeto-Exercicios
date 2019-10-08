# -*- encoding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Leao(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def rugir(self):
        pass


class LeaoAfricano(Leao):

    def rugir(self):
        print('Leao Africano')


class LeaoAsiatico(Leao):

    def rugir(self):
        print('Leao Asiatico')


class Cacador(object):

    def cacar(self, leao):
        leao.rugir()


class CachorroSelvagem(object):

    def latir(self):
        print('Cachorro selvagem')


class CachorroSelvagemAdapter(Leao):

    def __init__(self, cachorro_selvagem):
        self.__cachorro_selvagem = cachorro_selvagem

    def rugir(self):
        self.__cachorro_selvagem.latir()


if __name__ == '__main__':

    leao_africano = LeaoAfricano()
    leao_asiatico = LeaoAsiatico()
    cachorro_selvagem = CachorroSelvagem()

    cachorro_selvagem_adapter = CachorroSelvagemAdapter(cachorro_selvagem)

    cacador = Cacador()
    Cacador.cacar(leao_africano)
    Cacador.cacar(leao_asiatico)
    Cacador.cacar(cachorro_selvagem_adapter)
