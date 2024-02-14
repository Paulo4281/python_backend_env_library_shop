from typing import TypedDict

class UserAuthDTO(TypedDict):
    mail: str
    password: str

class UserAuthResponseDTO(TypedDict):
    name: str
    mail: str
    age: int
    message: str
class UserDTO(TypedDict):
    name: str
    mail: str
    password: str
    age: int

class UserResponseDTO(TypedDict):
    id_: str
    name: str
    mail: str
    age: int
    created_at: str