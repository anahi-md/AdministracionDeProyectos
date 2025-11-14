from pydantic import BaseModel

class Game(BaseModel):
    id: int
    equipo_local: str
    equipo_visitante: str
    marcador_local: int
    marcador_visitante: int
    estado: str