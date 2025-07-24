import unittest
from ..CountryInformation.CountryInformationCore import CountryInformationCore


class CountryInformation(unittest.TestCase):
    testfileprefix = "testfile_"

    def test_get_all_countries(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()
        # TODO

        # act
        all_countries = ci.get_all_countries()  # pylint:disable=unused-variable

        # assert
        # TODO

    def test_get_all_languages(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()
        # TODO

        # act
        all_languages = ci.get_all_languages()  # pylint:disable=unused-variable

        # assert
        # TODO

    def test_get_all_common_culture_language_combinations(self) -> None:

        # arrange
        ci: CountryInformationCore = CountryInformationCore()
        # TODO

        # act
        all_common_culture_language_combinations = ci.get_all_common_culture_language_combinations()  # pylint:disable=unused-variable

        # assert
        # TODO
