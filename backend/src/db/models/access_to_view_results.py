from typing import Optional

from sqlmodel import Field, SQLModel


# THIS MODEL WILL BE USED LATER ON IN THE PROJECT
class AccessToViewResults(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    survey_id: Optional[int] = Field(
        default=None, foreign_key="survey.id", primary_key=True
    )
