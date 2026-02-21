# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_growth.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/21 18:00:30 by nilinott          #+#    #+#             #
#    Updated: 2026/02/21 18:00:31 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant():
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 1

    def age_up(self):
        self.age += 1

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def grow_plant(plants, max_plant: int):
    i: int = 0
    j: int = 1
    while (i < max_plant):
        while (j < 7):
            plants[i].grow()
            plants[i].age_up()
            j += 1
        j = 0
        i += 1


def aff_plant(plants, max_plant: int):
    i: int = 0
    while (i < max_plant):
        print(plants[i].get_info())
        i += 1


def main() -> None:
    i: int = 0
    max_plant: int = 0
    result: int = 0

    plants = [
        Plant("Rose", 25, 30),
    ]
    initial_plant = [plant.height for plant in plants]
    max_plant = len(plants)
    print("=== Day 1 ===")
    aff_plant(plants, max_plant)

    grow_plant(plants, max_plant)

    print("=== Day 7 ===")
    aff_plant(plants, max_plant)
    result = plants[i].height - initial_plant[i]
    print(f"Growth this week: +{result}cm")


if __name__ == "__main__":
    main()
