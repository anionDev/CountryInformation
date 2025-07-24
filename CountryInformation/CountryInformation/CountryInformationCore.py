from ScriptCollection.GeneralUtilities import GeneralUtilities

version = "1.0.0"
__version__ = version


class Country:
    name_in_english: str
    abbreviation: str


class Language:
    name_in_english: str
    abbreviation: str


class CulturedLanguage:
    language: Language
    country: Country

    def get_abbreviation(self) -> str:
        return f"{self.language.abbreviation}-{self.country.abbreviation}"


class CountryInformationCore:

    @GeneralUtilities.check_arguments
    def get_all_countries(self) -> list[Country]:
        return []  # TODO

    @GeneralUtilities.check_arguments
    def get_all_languages(self) -> list[Language]:
        return []  # TODO

    @GeneralUtilities.check_arguments
    def get_all_common_culture_language_combinations(self) -> list[CulturedLanguage]:
        return []  # TODO
