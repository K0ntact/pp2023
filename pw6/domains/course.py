from .info import Info


class Course(Info):
    def __init__(self, ID: str, name: str, credit: int) -> None:
        super().__init__(ID, name)
        self.__credit = credit
        self.__marks = []

    def get_credit(self) -> int: return self.__credit
    def get_marks(self) -> list: return self.__marks

    def set_marks(self, mark: int) -> None:
        self.__marks.append(mark)

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Credits: {self.__credit}")
        print("\n")

    def display_marks(self, std_list: list) -> None:
        for std in std_list:
            std_pos = std_list.index(std)
            print(f"{std.get_name()}: {self.__marks[std_pos]}")

    def set_marks_now(self, mark: list) -> None:
        """
        Set marks from existing list
        :param mark: Array with marks
        :return:
        """
        self.__marks = mark
