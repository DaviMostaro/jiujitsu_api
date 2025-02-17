from ninja import ModelSchema, Schema
from .models import Alunos
from typing import Optional

class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']
        
class UpdateAlunosSchema(Schema):
    nome: Optional[str]
    email: Optional[str]
    faixa: Optional[str]
    data_nascimento: Optional[str]
        
class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_necessarias_para_proxima_faixa: int
    
class AulaRealizadaSchema(Schema):
    qtd: Optional[int] = 1
    email_aluno: str

