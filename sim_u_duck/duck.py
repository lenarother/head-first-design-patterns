from abc import ABC

from behavior.fly import FlyWithWings, FlyNoWay
from behavior.quack import Quack, Silence, Squeak


class Duck(ABC):

    def __init__(self, fly_behavior=FlyWithWings, quack_behavior=Quack):
        self.fly_behavior = fly_behavior()
        self.quack_behavior = quack_behavior()

    def __repr__(self):
        return (
            f'{self.swim()}\n'
            f'{self.perform_quack()}\n'
            f'{self.perform_fly()}\n'
        )

    def set_fly_behaviour(self, fly_behaviour):
        self.fly_behavior = fly_behaviour()

    def perform_fly(self):
        return self.fly_behavior.fly()

    def set_quack_behaviour(self, quack_behaviour):
        self.quack_behavior = quack_behaviour()

    def perform_quack(self):
        return self.quack_behavior.quack()

    @staticmethod
    def swim():
        return 'All ducks can swim!'


class MallardDuck(Duck):
    pass


class DecoyDuck(Duck):

    def __init__(self, fly_behavior=FlyNoWay, quack_behavior=Silence):
        super().__init__(fly_behavior, quack_behavior)


class RubberDuck(Duck):

    def __init__(self, fly_behavior=FlyNoWay, quack_behavior=Squeak):
        super().__init__(fly_behavior, quack_behavior)


class ModelDuck(Duck):
    pass
