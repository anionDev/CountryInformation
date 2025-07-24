from .Language import Language


class Country:
    common_name_in_english: str
    official_name_in_english: str
    country_code: str
    languages: list[Language]

    def __init__(self, common_name_in_english: str, official_name_in_english: str, country_code: str, languages: list[Language]):
        self.common_name_in_english = common_name_in_english
        self.official_name_in_english = official_name_in_english
        self.country_code = country_code
        self.languages = languages
