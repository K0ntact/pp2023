from .info import Info


class Student(Info):
    def __init__(self, ID: str, name: str, dob: str) -> None:
        super().__init__(ID, name)
        self.__dob = dob
        self.__gpa = 0

    def get_dob(self) -> str: return self.__dob
    def set_gpa(self, gpa: float) -> None: self.__gpa = gpa
    def get_gpa(self) -> float: return self.__gpa

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"DOB: {self.__dob}")
        print("\n")