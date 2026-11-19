from dataclasses import dataclass
from pathlib import Path
import yaml


yaml_path = Path(__file__).parent / "texts.yml"


with open(yaml_path, "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)


@dataclass(frozen=True)
class LanguageTexts:
    START: str


class Texts:
    RU = LanguageTexts(**data["RU"])
    EN = LanguageTexts(**data["EN"])

    @classmethod
    def get(cls, lang: str) -> LanguageTexts:
        return cls.RU if lang == "RU" else cls.EN