from abc import ABC, abstractmethod


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):

    def quack(self):
        return 'Quack!'


class Silence(QuackBehavior):

    def quack(self):
        return 'Pssst'


class Squeak(QuackBehavior):

    def quack(self):
        return 'Pip!'
