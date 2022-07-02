class Register():

    def register(self, name: str, age: int) -> None:
        if self.__validate_data(name, age):
            self.__store(name, age)
        else:
            print('Data Invalid')

    def __validate_data(self, name: str, age: int):
        return isinstance(name, str) and isinstance(age, int)

    def __store(self, name: str, age: int):
        print(f'{name} and {age} stored.')


reg = Register()

reg.register('Apollo', 21)
reg.register('Apollo', '21')
