
from fastapi import APIRouter

router = APIRouter()

class Aluno():
    def __init__(BaseModel):
        self.nome = str
        self.email = str
        self.curso = str
        self.github = str
        self.cidade = str
        self.interesses = str

@router.get("/me")
def get_info():
    minhas_info = {
        "nome": "Joab Raniel Rodrigues",
        "email": "joabraniel2006@gmail.com",
        "curso": "Sistemas de Informação",
        "github": "github.com/Joab-Ran",
        "cidade": "Milagres - CE",
        "interesses": ["Front-End", "Back-End", "Banco de Dados", "Arquitetura de Software"]
    }
    return minhas_info