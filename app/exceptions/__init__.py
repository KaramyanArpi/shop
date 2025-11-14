class BaseApiError(Exception):
    def __init__(self, msg, code=500):
        self.message = msg
        self.status_code = code

class UserError(BaseApiError):
    def __init__(self, msg):
        super().__init__(msg, 400)

class UserAlreadyExistsError(UserError):
    def __init__(self):
        super().__init__("User with that username already exists! Please choose another username.")



class UserDoesNotExistError(UserError):
    def __init__(self):
        super().__init__("User does not exist!")
