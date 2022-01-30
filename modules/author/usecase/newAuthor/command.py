from pydantic import BaseModel, Field
from dataclasses import dataclass
from typing import Optional

from modules.author.domain.value_objects import Name, Age, Biography


@dataclass(frozen=True)
class NewAuthorCommand(BaseModel):
    name: Name
    age: Age
    biography: Optional[Biography]
