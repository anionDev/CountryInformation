
from .Language import Language
from .LanguageData import LanguageData


class CacheForLanguages:
    __languages: list[Language] = None

    def get_all_languages(self) -> list[Language]:
        if self.__languages is None:
            self.__languages = LanguageData().get_all_languages()
        return self.__languages
