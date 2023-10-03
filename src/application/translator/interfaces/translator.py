from typing import Protocol

from src.application.translator.models.dto import TranslationResultDTO


class ITranslator(Protocol):

    async def translate(self, text: str, target_land: str) -> TranslationResultDTO:
        raise NotImplemented
