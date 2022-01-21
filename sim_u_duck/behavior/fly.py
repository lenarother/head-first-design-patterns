from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):

    def fly(self):
        return 'I am flying'


class FlyNoWay(FlyBehavior):

    def fly(self):
        return 'I cannot fly'


class RocketPoweredFly(FlyBehavior):

    def fly(self):
        return 'I am flying with rocket'
