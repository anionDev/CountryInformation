import unittest
from ..CountryInformation.CountryInformationCore import CountryInformationCore


class CountryInformation(unittest.TestCase):

    def test_get_all_countries(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()

        # act
        all_countries = ci.get_all_countries()

        # assert
        assert 0 < len(all_countries)
        # TODO add more assertions

    def test_get_all_languages(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()

        # act
        all_languages = ci.get_all_languages()

        # assert
        assert 0 < len(all_languages)
        # TODO add more assertions

    def test_get_all_common_culture_language_combinations(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()
        # TODO

        # act
        all_common_culture_language_combinations = ci.get_all_common_culture_language_combinations()

        # assert
        assert 0 < len(all_common_culture_language_combinations)
        # TODO add more assertions
