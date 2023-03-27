class Info:
    def __init__(self, ID: str, name: str) -> None:
        self._id = ID
        self._name = name

    def get_name(self) -> str: return self._name
    def get_ID(self) -> str: return self._id

    def display_info(self) -> None:
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
