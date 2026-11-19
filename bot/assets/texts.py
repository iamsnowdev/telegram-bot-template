from pathlib import Path
from pydantic import BaseModel, ConfigDict
import yaml


yaml_path = Path(__file__).parent / "texts.yml"


with open(yaml_path, "r", encoding="utf-8") as file:
    data = yaml.safe_load(file)


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True)


# Message texts
class Texts(FrozenModel):
    start: str


# Keyboard texts
class StartKeyboard(FrozenModel):
    btn1: str
    btn2: str


class Keyboards:
    start: StartKeyboard


class LanguageTexts(FrozenModel):
    texts: Texts
    keyboards: Keyboards


# All texts
class AllTexts(FrozenModel):
    en: LanguageTexts
    ru: LanguageTexts

    def get(self, lang: str) -> LanguageTexts:
        return getattr(self, lang, self.en)


all_texts = AllTexts.model_validate(data)