# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: nilinott <nilinott@student.42lyon.fr>      +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/02/22 00:44:35 by nilinott          #+#    #+#             #
#    Updated: 2026/02/22 00:44:36 by nilinott         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class SecurePlant():
    def __init__(self, name: str):
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.__name}")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {height}cm [OK]")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def n(self):
        return self.__name

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__age = age
            print(f"Age updated: {age} days [OK]\n")


def main() -> None:
    print("=== Garden Security System ===")
    p = SecurePlant("Rose")
    p.set_height(25)
    p.set_age(30)

    p.set_height(-5)
    print(f"Current plant: {p.n()} ({p.get_height()}cm, {p.get_age()} days)")


if __name__ == "__main__":
    main()
