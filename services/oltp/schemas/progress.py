from uuid import UUID

from pydantic import BaseModel


class FilmProgress(BaseModel):
    user_id: UUID
    film_id: UUID
    progress: int
