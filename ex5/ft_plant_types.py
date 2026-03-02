# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_types.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/22 18:46:39 by nilinott          #+#    #+#             #
#    Updated: 2026/02/22 18:46:40 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.__name = name
        self.__height = height
        self.__age = age

    def name(self):
        return (self.__name)

    def height(self):
        return (self.__height)

    def age(self):
        return (self.__age)


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str, bloom):
        super().__init__(name, height, age)
        self.__color = color
        self.__bloom = bloom

    def get_bloom(self):
        if (self.__bloom):
            return f"{self.name()} is blooming beautifully!\n"
        return "\n"

    def get_color(self):
        return f"{self.__color} color"

    def get_plant(self):
        return (f"{self.name()} (Flower): "
                f"{self.height()}cm, {self.age()} days, {self.get_color()}\n"
                f"{self.get_bloom()}")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.__diameter = diameter

    def produce_shade(self):
        result: int = (self.height() * self.__diameter)
        return f"{self.name()} provides {result} square meters of shade\n"

    def trunk_diameter(self):
        return f"{self.__diameter} diameter"

    def get_plant(self):
        return (
            f"{self.name()} (Vegetable): "
            f"{self.height()}cm, {self.age()} days, {self.trunk_diameter()}\n"
            f"{self.produce_shade()}")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int):
        super().__init__(name, height, age)

    def harvest_season(self):
        return "summer harvest"

    def nutritional_value(self):
        return f"{self.name()} is rich in vitamin C"

    def get_plant(self):
        return (
            f"{self.name()} (Tree): "
            f"{self.height()}cm, {self.age()} days, {self.harvest_season()}\n"
            f"{self.nutritional_value()}")


def display_plant(plants):
    i: int
    max_plant: int

    i = 0
    max_plant = len(plants)

    while (i < max_plant):
        print(f"{plants[i].get_plant()}")
        i += 1


def main() -> None:
    print("=== Garden Plant Types ===\n")
    plants = [
        Flower("Rose", 10, 20, "red", True),
        Tree("Oak", 500, 1828, 50),
        Vegetable("Tomato", 80, 90),
    ]
    display_plant(plants)


if __name__ == "__main__":
    main()
