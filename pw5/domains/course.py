from .info import Info
import math


class Course(Info):
    def __init__(self, ID: str, name: str, credit: int) -> None:
        super().__init__(ID, name)
        self.__credit = credit
        self.__marks = []

    def get_credit(self) -> int: return self.__credit
    def get_marks(self) -> list: return self.__marks

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Credits: {self.__credit}")
        print("\n")

    def display_marks(self, std_list: list) -> None:
        for std in std_list:
            std_pos = std_list.index(std)
            print(f"{std.get_name()}: {self.__marks[std_pos]}")

    def set_marks(self, std_list: list) -> None:
        for std in std_list:
            f_mark = float(input(f"Set the score for student {std.get_name()}: "))
            i_mark = math.floor(f_mark)
            self.__marks.append(i_mark)

    def set_marks_now(self, mark: int) -> None:
        self.__marks.append(mark)

    # TEST
    # def set_marks_TEST(self, mk_lst: list) -> None:
    #     self.__marks = mk_lst
