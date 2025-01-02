from src.api.models.base import Base


class Subtitle(Base):
    subtitle: str

    def validate_for_answer(self) -> None:
        pass

    def validate_for_draft(self) -> None:
        pass

    def validate_structure_against(self, other) -> None:
        if not isinstance(other, Subtitle) or self.subtitle != other.subtitle:
            raise ValueError("Invalid subtitle!")
