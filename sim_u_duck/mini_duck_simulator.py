from behavior.fly import FlyWithWings, FlyNoWay, RocketPoweredFly
from behavior.quack import Quack, Squeak, Silence
from duck import ModelDuck


class Simulator:

    @staticmethod
    def run():
        duck = ModelDuck()
        fly_behaviors = [FlyWithWings, FlyNoWay, RocketPoweredFly]
        quack_behaviors = [Quack, Squeak, Silence]
        for fly, quack in zip(fly_behaviors, quack_behaviors):
            duck.set_fly_behaviour(fly)
            duck.set_quack_behaviour(quack)
            print(duck)


if __name__ == '__main__':
    Simulator.run()