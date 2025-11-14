from fastapi import APIRouter
from Modules.Equipo3.Logic.games_logic import get_all_games

equipo3_router = APIRouter(
    prefix="/equipo3",
    tags=["Equipo 3 - Seguimiento del juego"]
)

@equipo3_router.get("/games")
def get_games():
    return get_all_games()