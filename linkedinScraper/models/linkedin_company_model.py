class LinkedinCompany:
    def __init__(self, name: str, location: str, logo: str) -> None:
        self.name = name
        self.location = location
        self.logo = logo

    def print(self) -> None:
        print("*" * 100 + "\n")
        print(f"company name: {self.name}")
        print(f"comapny location: {self.location}")
        print(f"company logo: {self.logo}")
        print("*" * 100 + "\n")
