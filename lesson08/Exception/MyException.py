class LoginException(Exception):
    def __int__(self, *args: object) -> None:
        super().__int__(*args)

    def __str__(self) -> str:
        return super().__str__()

    def HowToDo(self):
        print('Please re-login')
        print('Contact with xxx if error exits')

