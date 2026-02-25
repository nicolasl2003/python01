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
    def __init__(self, name: str, height: int, age: int, typep: str):
        self.__name = name
        self.__height = height
        self.__age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str, bloom, typep: str):
        super().__init__(name, height, age, typep)
        self.color = color
        self.bloom = bloom

        if (bloom == True):
            #print(f"{self.__name} is blooming beautifully!")
            return


#class Tree(Plant):
 #   def __init__(self, name: str, height: int, age: int, ):


def display_plant(plant):
    i: int
    max_plant: int

    i = 0
    max_plant = len(plant)

    while (i < max_plant):
        print()
        i += 1


def main() -> None:
    print("=== Garden Plant Types ===")
    plant = {
        Flower("Rose", 10, 20, "rouge", True, "flower")
    }
    display_plant(plant)


if __name__ == "__main__":
    main()
