# The content of this file is generated.
from .Country import Country
from .LanguageUtilities import LanguageUtilities
from .LanguageCodeConversionUtilities import LanguageCodeConversionUtilities


class CountryData:
    def get_all_countries(self) -> list[Country]:
        result:list[Country] = []
        language_utilities: LanguageUtilities = LanguageUtilities(None)

        languages_for_AF: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("prs"): language_utilities.get_language_from_code_iso639_3("prs")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("pus"): language_utilities.get_language_from_code_iso639_3("pus")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tuk"): language_utilities.get_language_from_code_iso639_3("tuk")
        result.append(Country("Afghanistan", "Islamic Republic of Afghanistan", "AF", languages_for_AF))
        
        languages_for_AL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sqi"): language_utilities.get_language_from_code_iso639_3("sqi")
        result.append(Country("Albania", "Republic of Albania", "AL", languages_for_AL))
        
        languages_for_DZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Algeria", "People's Democratic Republic of Algeria", "DZ", languages_for_DZ))
        
        languages_for_AD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("cat"): language_utilities.get_language_from_code_iso639_3("cat")
        result.append(Country("Andorra", "Principality of Andorra", "AD", languages_for_AD))
        
        languages_for_AO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("Angola", "Republic of Angola", "AO", languages_for_AO))
        
        languages_for_AG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Antigua and Barbuda", "Antigua and Barbuda", "AG", languages_for_AG))
        
        languages_for_AR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("grn"): language_utilities.get_language_from_code_iso639_3("grn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Argentina", "Argentine Republic", "AR", languages_for_AR))
        
        languages_for_AM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hye"): language_utilities.get_language_from_code_iso639_3("hye")
        result.append(Country("Armenia", "Republic of Armenia", "AM", languages_for_AM))
        
        languages_for_AU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Australia", "Commonwealth of Australia", "AU", languages_for_AU))
        
        languages_for_AT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bar"): language_utilities.get_language_from_code_iso639_3("bar")
        result.append(Country("Austria", "Republic of Austria", "AT", languages_for_AT))
        
        languages_for_AZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("aze"): language_utilities.get_language_from_code_iso639_3("aze")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        result.append(Country("Azerbaijan", "Republic of Azerbaijan", "AZ", languages_for_AZ))
        
        languages_for_BS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Bahamas", "Commonwealth of the Bahamas", "BS", languages_for_BS))
        
        languages_for_BH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Bahrain", "Kingdom of Bahrain", "BH", languages_for_BH))
        
        languages_for_BD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ben"): language_utilities.get_language_from_code_iso639_3("ben")
        result.append(Country("Bangladesh", "People's Republic of Bangladesh", "BD", languages_for_BD))
        
        languages_for_BB: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Barbados", "Barbados", "BB", languages_for_BB))
        
        languages_for_BY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bel"): language_utilities.get_language_from_code_iso639_3("bel")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        result.append(Country("Belarus", "Republic of Belarus", "BY", languages_for_BY))
        
        languages_for_BE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("deu"): language_utilities.get_language_from_code_iso639_3("deu")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nld"): language_utilities.get_language_from_code_iso639_3("nld")
        result.append(Country("Belgium", "Kingdom of Belgium", "BE", languages_for_BE))
        
        languages_for_BZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bjz"): language_utilities.get_language_from_code_iso639_3("bjz")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Belize", "Belize", "BZ", languages_for_BZ))
        
        languages_for_BJ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Benin", "Republic of Benin", "BJ", languages_for_BJ))
        
        languages_for_BT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("dzo"): language_utilities.get_language_from_code_iso639_3("dzo")
        result.append(Country("Bhutan", "Kingdom of Bhutan", "BT", languages_for_BT))
        
        languages_for_BO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("aym"): language_utilities.get_language_from_code_iso639_3("aym")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("grn"): language_utilities.get_language_from_code_iso639_3("grn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("que"): language_utilities.get_language_from_code_iso639_3("que")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Bolivia", "Plurinational State of Bolivia", "BO", languages_for_BO))
        
        languages_for_BA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bos"): language_utilities.get_language_from_code_iso639_3("bos")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hrv"): language_utilities.get_language_from_code_iso639_3("hrv")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("srp"): language_utilities.get_language_from_code_iso639_3("srp")
        result.append(Country("Bosnia and Herzegovina", "Bosnia and Herzegovina", "BA", languages_for_BA))
        
        languages_for_BW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tsn"): language_utilities.get_language_from_code_iso639_3("tsn")
        result.append(Country("Botswana", "Republic of Botswana", "BW", languages_for_BW))
        
        languages_for_BR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("Brazil", "Federative Republic of Brazil", "BR", languages_for_BR))
        
        languages_for_BN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("msa"): language_utilities.get_language_from_code_iso639_3("msa")
        result.append(Country("Brunei", "Nation of Brunei, Abode of Peace", "BN", languages_for_BN))
        
        languages_for_BG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bul"): language_utilities.get_language_from_code_iso639_3("bul")
        result.append(Country("Bulgaria", "Republic of Bulgaria", "BG", languages_for_BG))
        
        languages_for_BF: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Burkina Faso", "Burkina Faso", "BF", languages_for_BF))
        
        languages_for_BI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("run"): language_utilities.get_language_from_code_iso639_3("run")
        result.append(Country("Burundi", "Republic of Burundi", "BI", languages_for_BI))
        
        languages_for_KH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("khm"): language_utilities.get_language_from_code_iso639_3("khm")
        result.append(Country("Cambodia", "Kingdom of Cambodia", "KH", languages_for_KH))
        
        languages_for_CM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Cameroon", "Republic of Cameroon", "CM", languages_for_CM))
        
        languages_for_CA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Canada", "Canada", "CA", languages_for_CA))
        
        languages_for_CV: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("Cape Verde", "Republic of Cabo Verde", "CV", languages_for_CV))
        
        languages_for_CF: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sag"): language_utilities.get_language_from_code_iso639_3("sag")
        result.append(Country("Central African Republic", "Central African Republic", "CF", languages_for_CF))
        
        languages_for_TD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Chad", "Republic of Chad", "TD", languages_for_TD))
        
        languages_for_CL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Chile", "Republic of Chile", "CL", languages_for_CL))
        
        languages_for_CN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("zho"): language_utilities.get_language_from_code_iso639_3("zho")
        result.append(Country("China", "People's Republic of China", "CN", languages_for_CN))
        
        languages_for_CO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Colombia", "Republic of Colombia", "CO", languages_for_CO))
        
        languages_for_KM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("zdj"): language_utilities.get_language_from_code_iso639_3("zdj")
        result.append(Country("Comoros", "Union of the Comoros", "KM", languages_for_KM))
        
        languages_for_CG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kon"): language_utilities.get_language_from_code_iso639_3("kon")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lin"): language_utilities.get_language_from_code_iso639_3("lin")
        result.append(Country("Congo", "Republic of the Congo", "CG", languages_for_CG))
        
        languages_for_CR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Costa Rica", "Republic of Costa Rica", "CR", languages_for_CR))
        
        languages_for_HR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hrv"): language_utilities.get_language_from_code_iso639_3("hrv")
        result.append(Country("Croatia", "Republic of Croatia", "HR", languages_for_HR))
        
        languages_for_CU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Cuba", "Republic of Cuba", "CU", languages_for_CU))
        
        languages_for_CY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ell"): language_utilities.get_language_from_code_iso639_3("ell")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tur"): language_utilities.get_language_from_code_iso639_3("tur")
        result.append(Country("Cyprus", "Republic of Cyprus", "CY", languages_for_CY))
        
        languages_for_CZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ces"): language_utilities.get_language_from_code_iso639_3("ces")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("slk"): language_utilities.get_language_from_code_iso639_3("slk")
        result.append(Country("Czechia", "Czech Republic", "CZ", languages_for_CZ))
        
        languages_for_CD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kon"): language_utilities.get_language_from_code_iso639_3("kon")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lin"): language_utilities.get_language_from_code_iso639_3("lin")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lua"): language_utilities.get_language_from_code_iso639_3("lua")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swa"): language_utilities.get_language_from_code_iso639_3("swa")
        result.append(Country("DR Congo", "Democratic Republic of the Congo", "CD", languages_for_CD))
        
        languages_for_DK: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("dan"): language_utilities.get_language_from_code_iso639_3("dan")
        result.append(Country("Denmark", "Kingdom of Denmark", "DK", languages_for_DK))
        
        languages_for_DJ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Djibouti", "Republic of Djibouti", "DJ", languages_for_DJ))
        
        languages_for_DM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Dominica", "Commonwealth of Dominica", "DM", languages_for_DM))
        
        languages_for_DO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Dominican Republic", "Dominican Republic", "DO", languages_for_DO))
        
        languages_for_EC: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Ecuador", "Republic of Ecuador", "EC", languages_for_EC))
        
        languages_for_EG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Egypt", "Arab Republic of Egypt", "EG", languages_for_EG))
        
        languages_for_SV: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("El Salvador", "Republic of El Salvador", "SV", languages_for_SV))
        
        languages_for_GQ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Equatorial Guinea", "Republic of Equatorial Guinea", "GQ", languages_for_GQ))
        
        languages_for_ER: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tir"): language_utilities.get_language_from_code_iso639_3("tir")
        result.append(Country("Eritrea", "State of Eritrea", "ER", languages_for_ER))
        
        languages_for_EE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("est"): language_utilities.get_language_from_code_iso639_3("est")
        result.append(Country("Estonia", "Republic of Estonia", "EE", languages_for_EE))
        
        languages_for_SZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ssw"): language_utilities.get_language_from_code_iso639_3("ssw")
        result.append(Country("Eswatini", "Kingdom of Eswatini", "SZ", languages_for_SZ))
        
        languages_for_ET: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("amh"): language_utilities.get_language_from_code_iso639_3("amh")
        result.append(Country("Ethiopia", "Federal Democratic Republic of Ethiopia", "ET", languages_for_ET))
        
        languages_for_FJ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fij"): language_utilities.get_language_from_code_iso639_3("fij")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hif"): language_utilities.get_language_from_code_iso639_3("hif")
        result.append(Country("Fiji", "Republic of Fiji", "FJ", languages_for_FJ))
        
        languages_for_FI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fin"): language_utilities.get_language_from_code_iso639_3("fin")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swe"): language_utilities.get_language_from_code_iso639_3("swe")
        result.append(Country("Finland", "Republic of Finland", "FI", languages_for_FI))
        
        languages_for_FR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("France", "French Republic", "FR", languages_for_FR))
        
        languages_for_GA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Gabon", "Gabonese Republic", "GA", languages_for_GA))
        
        languages_for_GM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Gambia", "Republic of the Gambia", "GM", languages_for_GM))
        
        languages_for_GE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kat"): language_utilities.get_language_from_code_iso639_3("kat")
        result.append(Country("Georgia", "Georgia", "GE", languages_for_GE))
        
        languages_for_DE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("deu"): language_utilities.get_language_from_code_iso639_3("deu")
        result.append(Country("Germany", "Federal Republic of Germany", "DE", languages_for_DE))
        
        languages_for_GH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Ghana", "Republic of Ghana", "GH", languages_for_GH))
        
        languages_for_GR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ell"): language_utilities.get_language_from_code_iso639_3("ell")
        result.append(Country("Greece", "Hellenic Republic", "GR", languages_for_GR))
        
        languages_for_GD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Grenada", "Grenada", "GD", languages_for_GD))
        
        languages_for_GT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Guatemala", "Republic of Guatemala", "GT", languages_for_GT))
        
        languages_for_GN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Guinea", "Republic of Guinea", "GN", languages_for_GN))
        
        languages_for_GW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("pov"): language_utilities.get_language_from_code_iso639_3("pov")
        result.append(Country("Guinea-Bissau", "Republic of Guinea-Bissau", "GW", languages_for_GW))
        
        languages_for_GY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Guyana", "Co-operative Republic of Guyana", "GY", languages_for_GY))
        
        languages_for_HT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hat"): language_utilities.get_language_from_code_iso639_3("hat")
        result.append(Country("Haiti", "Republic of Haiti", "HT", languages_for_HT))
        
        languages_for_HN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Honduras", "Republic of Honduras", "HN", languages_for_HN))
        
        languages_for_HU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hun"): language_utilities.get_language_from_code_iso639_3("hun")
        result.append(Country("Hungary", "Hungary", "HU", languages_for_HU))
        
        languages_for_IS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("isl"): language_utilities.get_language_from_code_iso639_3("isl")
        result.append(Country("Iceland", "Iceland", "IS", languages_for_IS))
        
        languages_for_IN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hin"): language_utilities.get_language_from_code_iso639_3("hin")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tam"): language_utilities.get_language_from_code_iso639_3("tam")
        result.append(Country("India", "Republic of India", "IN", languages_for_IN))
        
        languages_for_ID: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ind"): language_utilities.get_language_from_code_iso639_3("ind")
        result.append(Country("Indonesia", "Republic of Indonesia", "ID", languages_for_ID))
        
        languages_for_IR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fas"): language_utilities.get_language_from_code_iso639_3("fas")
        result.append(Country("Iran", "Islamic Republic of Iran", "IR", languages_for_IR))
        
        languages_for_IQ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("arc"): language_utilities.get_language_from_code_iso639_3("arc")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ckb"): language_utilities.get_language_from_code_iso639_3("ckb")
        result.append(Country("Iraq", "Republic of Iraq", "IQ", languages_for_IQ))
        
        languages_for_IE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("gle"): language_utilities.get_language_from_code_iso639_3("gle")
        result.append(Country("Ireland", "Republic of Ireland", "IE", languages_for_IE))
        
        languages_for_IL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("heb"): language_utilities.get_language_from_code_iso639_3("heb")
        result.append(Country("Israel", "State of Israel", "IL", languages_for_IL))
        
        languages_for_IT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ita"): language_utilities.get_language_from_code_iso639_3("ita")
        result.append(Country("Italy", "Italian Republic", "IT", languages_for_IT))
        
        languages_for_CI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Ivory Coast", "Republic of Côte d'Ivoire", "CI", languages_for_CI))
        
        languages_for_JM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("jam"): language_utilities.get_language_from_code_iso639_3("jam")
        result.append(Country("Jamaica", "Jamaica", "JM", languages_for_JM))
        
        languages_for_JP: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("jpn"): language_utilities.get_language_from_code_iso639_3("jpn")
        result.append(Country("Japan", "Japan", "JP", languages_for_JP))
        
        languages_for_JO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Jordan", "Hashemite Kingdom of Jordan", "JO", languages_for_JO))
        
        languages_for_KZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kaz"): language_utilities.get_language_from_code_iso639_3("kaz")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        result.append(Country("Kazakhstan", "Republic of Kazakhstan", "KZ", languages_for_KZ))
        
        languages_for_KE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swa"): language_utilities.get_language_from_code_iso639_3("swa")
        result.append(Country("Kenya", "Republic of Kenya", "KE", languages_for_KE))
        
        languages_for_KI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("gil"): language_utilities.get_language_from_code_iso639_3("gil")
        result.append(Country("Kiribati", "Independent and Sovereign Republic of Kiribati", "KI", languages_for_KI))
        
        languages_for_KW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Kuwait", "State of Kuwait", "KW", languages_for_KW))
        
        languages_for_KG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kir"): language_utilities.get_language_from_code_iso639_3("kir")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        result.append(Country("Kyrgyzstan", "Kyrgyz Republic", "KG", languages_for_KG))
        
        languages_for_LA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lao"): language_utilities.get_language_from_code_iso639_3("lao")
        result.append(Country("Laos", "Lao People's Democratic Republic", "LA", languages_for_LA))
        
        languages_for_LV: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lav"): language_utilities.get_language_from_code_iso639_3("lav")
        result.append(Country("Latvia", "Republic of Latvia", "LV", languages_for_LV))
        
        languages_for_LB: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Lebanon", "Lebanese Republic", "LB", languages_for_LB))
        
        languages_for_LS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sot"): language_utilities.get_language_from_code_iso639_3("sot")
        result.append(Country("Lesotho", "Kingdom of Lesotho", "LS", languages_for_LS))
        
        languages_for_LR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Liberia", "Republic of Liberia", "LR", languages_for_LR))
        
        languages_for_LY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Libya", "State of Libya", "LY", languages_for_LY))
        
        languages_for_LI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("deu"): language_utilities.get_language_from_code_iso639_3("deu")
        result.append(Country("Liechtenstein", "Principality of Liechtenstein", "LI", languages_for_LI))
        
        languages_for_LT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lit"): language_utilities.get_language_from_code_iso639_3("lit")
        result.append(Country("Lithuania", "Republic of Lithuania", "LT", languages_for_LT))
        
        languages_for_LU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("deu"): language_utilities.get_language_from_code_iso639_3("deu")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ltz"): language_utilities.get_language_from_code_iso639_3("ltz")
        result.append(Country("Luxembourg", "Grand Duchy of Luxembourg", "LU", languages_for_LU))
        
        languages_for_MG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mlg"): language_utilities.get_language_from_code_iso639_3("mlg")
        result.append(Country("Madagascar", "Republic of Madagascar", "MG", languages_for_MG))
        
        languages_for_MW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nya"): language_utilities.get_language_from_code_iso639_3("nya")
        result.append(Country("Malawi", "Republic of Malawi", "MW", languages_for_MW))
        
        languages_for_MY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("msa"): language_utilities.get_language_from_code_iso639_3("msa")
        result.append(Country("Malaysia", "Malaysia", "MY", languages_for_MY))
        
        languages_for_MV: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("div"): language_utilities.get_language_from_code_iso639_3("div")
        result.append(Country("Maldives", "Republic of the Maldives", "MV", languages_for_MV))
        
        languages_for_ML: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Mali", "Republic of Mali", "ML", languages_for_ML))
        
        languages_for_MT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mlt"): language_utilities.get_language_from_code_iso639_3("mlt")
        result.append(Country("Malta", "Republic of Malta", "MT", languages_for_MT))
        
        languages_for_MH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mah"): language_utilities.get_language_from_code_iso639_3("mah")
        result.append(Country("Marshall Islands", "Republic of the Marshall Islands", "MH", languages_for_MH))
        
        languages_for_MR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Mauritania", "Islamic Republic of Mauritania", "MR", languages_for_MR))
        
        languages_for_MU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mfe"): language_utilities.get_language_from_code_iso639_3("mfe")
        result.append(Country("Mauritius", "Republic of Mauritius", "MU", languages_for_MU))
        
        languages_for_MX: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Mexico", "United Mexican States", "MX", languages_for_MX))
        
        languages_for_FM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Micronesia", "Federated States of Micronesia", "FM", languages_for_FM))
        
        languages_for_MD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ron"): language_utilities.get_language_from_code_iso639_3("ron")
        result.append(Country("Moldova", "Republic of Moldova", "MD", languages_for_MD))
        
        languages_for_MC: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Monaco", "Principality of Monaco", "MC", languages_for_MC))
        
        languages_for_MN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mon"): language_utilities.get_language_from_code_iso639_3("mon")
        result.append(Country("Mongolia", "Mongolia", "MN", languages_for_MN))
        
        languages_for_ME: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("cnr"): language_utilities.get_language_from_code_iso639_3("cnr")
        result.append(Country("Montenegro", "Montenegro", "ME", languages_for_ME))
        
        languages_for_MA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ber"): language_utilities.get_language_from_code_iso639_3("ber")
        result.append(Country("Morocco", "Kingdom of Morocco", "MA", languages_for_MA))
        
        languages_for_MZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("Mozambique", "Republic of Mozambique", "MZ", languages_for_MZ))
        
        languages_for_MM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mya"): language_utilities.get_language_from_code_iso639_3("mya")
        result.append(Country("Myanmar", "Republic of the Union of Myanmar", "MM", languages_for_MM))
        
        languages_for_NA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("afr"): language_utilities.get_language_from_code_iso639_3("afr")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("deu"): language_utilities.get_language_from_code_iso639_3("deu")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("her"): language_utilities.get_language_from_code_iso639_3("her")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hgm"): language_utilities.get_language_from_code_iso639_3("hgm")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kwn"): language_utilities.get_language_from_code_iso639_3("kwn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("loz"): language_utilities.get_language_from_code_iso639_3("loz")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ndo"): language_utilities.get_language_from_code_iso639_3("ndo")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tsn"): language_utilities.get_language_from_code_iso639_3("tsn")
        result.append(Country("Namibia", "Republic of Namibia", "NA", languages_for_NA))
        
        languages_for_NR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nau"): language_utilities.get_language_from_code_iso639_3("nau")
        result.append(Country("Nauru", "Republic of Nauru", "NR", languages_for_NR))
        
        languages_for_NP: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nep"): language_utilities.get_language_from_code_iso639_3("nep")
        result.append(Country("Nepal", "Federal Democratic Republic of Nepal", "NP", languages_for_NP))
        
        languages_for_NL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nld"): language_utilities.get_language_from_code_iso639_3("nld")
        result.append(Country("Netherlands", "Kingdom of the Netherlands", "NL", languages_for_NL))
        
        languages_for_NZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mri"): language_utilities.get_language_from_code_iso639_3("mri")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nzs"): language_utilities.get_language_from_code_iso639_3("nzs")
        result.append(Country("New Zealand", "New Zealand", "NZ", languages_for_NZ))
        
        languages_for_NI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Nicaragua", "Republic of Nicaragua", "NI", languages_for_NI))
        
        languages_for_NE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Niger", "Republic of Niger", "NE", languages_for_NE))
        
        languages_for_NG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Nigeria", "Federal Republic of Nigeria", "NG", languages_for_NG))
        
        languages_for_KP: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kor"): language_utilities.get_language_from_code_iso639_3("kor")
        result.append(Country("North Korea", "Democratic People's Republic of Korea", "KP", languages_for_KP))
        
        languages_for_MK: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("mkd"): language_utilities.get_language_from_code_iso639_3("mkd")
        result.append(Country("North Macedonia", "Republic of North Macedonia", "MK", languages_for_MK))
        
        languages_for_NO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nno"): language_utilities.get_language_from_code_iso639_3("nno")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nob"): language_utilities.get_language_from_code_iso639_3("nob")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("smi"): language_utilities.get_language_from_code_iso639_3("smi")
        result.append(Country("Norway", "Kingdom of Norway", "NO", languages_for_NO))
        
        languages_for_OM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Oman", "Sultanate of Oman", "OM", languages_for_OM))
        
        languages_for_PK: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("urd"): language_utilities.get_language_from_code_iso639_3("urd")
        result.append(Country("Pakistan", "Islamic Republic of Pakistan", "PK", languages_for_PK))
        
        languages_for_PW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("pau"): language_utilities.get_language_from_code_iso639_3("pau")
        result.append(Country("Palau", "Republic of Palau", "PW", languages_for_PW))
        
        languages_for_PA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Panama", "Republic of Panama", "PA", languages_for_PA))
        
        languages_for_PG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("hmo"): language_utilities.get_language_from_code_iso639_3("hmo")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tpi"): language_utilities.get_language_from_code_iso639_3("tpi")
        result.append(Country("Papua New Guinea", "Independent State of Papua New Guinea", "PG", languages_for_PG))
        
        languages_for_PY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("grn"): language_utilities.get_language_from_code_iso639_3("grn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Paraguay", "Republic of Paraguay", "PY", languages_for_PY))
        
        languages_for_PE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("aym"): language_utilities.get_language_from_code_iso639_3("aym")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("que"): language_utilities.get_language_from_code_iso639_3("que")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Peru", "Republic of Peru", "PE", languages_for_PE))
        
        languages_for_PH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fil"): language_utilities.get_language_from_code_iso639_3("fil")
        result.append(Country("Philippines", "Republic of the Philippines", "PH", languages_for_PH))
        
        languages_for_PL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("pol"): language_utilities.get_language_from_code_iso639_3("pol")
        result.append(Country("Poland", "Republic of Poland", "PL", languages_for_PL))
        
        languages_for_PT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("Portugal", "Portuguese Republic", "PT", languages_for_PT))
        
        languages_for_QA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Qatar", "State of Qatar", "QA", languages_for_QA))
        
        languages_for_RO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ron"): language_utilities.get_language_from_code_iso639_3("ron")
        result.append(Country("Romania", "Romania", "RO", languages_for_RO))
        
        languages_for_RU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        result.append(Country("Russia", "Russian Federation", "RU", languages_for_RU))
        
        languages_for_RW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kin"): language_utilities.get_language_from_code_iso639_3("kin")
        result.append(Country("Rwanda", "Republic of Rwanda", "RW", languages_for_RW))
        
        languages_for_KN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Saint Kitts and Nevis", "Federation of Saint Christopher and Nevis", "KN", languages_for_KN))
        
        languages_for_LC: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Saint Lucia", "Saint Lucia", "LC", languages_for_LC))
        
        languages_for_VC: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Saint Vincent and the Grenadines", "Saint Vincent and the Grenadines", "VC", languages_for_VC))
        
        languages_for_WS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("smo"): language_utilities.get_language_from_code_iso639_3("smo")
        result.append(Country("Samoa", "Independent State of Samoa", "WS", languages_for_WS))
        
        languages_for_SM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ita"): language_utilities.get_language_from_code_iso639_3("ita")
        result.append(Country("San Marino", "Most Serene Republic of San Marino", "SM", languages_for_SM))
        
        languages_for_SA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Saudi Arabia", "Kingdom of Saudi Arabia", "SA", languages_for_SA))
        
        languages_for_SN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Senegal", "Republic of Senegal", "SN", languages_for_SN))
        
        languages_for_RS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("srp"): language_utilities.get_language_from_code_iso639_3("srp")
        result.append(Country("Serbia", "Republic of Serbia", "RS", languages_for_RS))
        
        languages_for_SC: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("crs"): language_utilities.get_language_from_code_iso639_3("crs")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Seychelles", "Republic of Seychelles", "SC", languages_for_SC))
        
        languages_for_SL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Sierra Leone", "Republic of Sierra Leone", "SL", languages_for_SL))
        
        languages_for_SG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("msa"): language_utilities.get_language_from_code_iso639_3("msa")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tam"): language_utilities.get_language_from_code_iso639_3("tam")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("zho"): language_utilities.get_language_from_code_iso639_3("zho")
        result.append(Country("Singapore", "Republic of Singapore", "SG", languages_for_SG))
        
        languages_for_SK: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("slk"): language_utilities.get_language_from_code_iso639_3("slk")
        result.append(Country("Slovakia", "Slovak Republic", "SK", languages_for_SK))
        
        languages_for_SI: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("slv"): language_utilities.get_language_from_code_iso639_3("slv")
        result.append(Country("Slovenia", "Republic of Slovenia", "SI", languages_for_SI))
        
        languages_for_SB: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Solomon Islands", "Solomon Islands", "SB", languages_for_SB))
        
        languages_for_SO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("som"): language_utilities.get_language_from_code_iso639_3("som")
        result.append(Country("Somalia", "Federal Republic of Somalia", "SO", languages_for_SO))
        
        languages_for_ZA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("afr"): language_utilities.get_language_from_code_iso639_3("afr")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nbl"): language_utilities.get_language_from_code_iso639_3("nbl")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nso"): language_utilities.get_language_from_code_iso639_3("nso")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sot"): language_utilities.get_language_from_code_iso639_3("sot")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ssw"): language_utilities.get_language_from_code_iso639_3("ssw")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tsn"): language_utilities.get_language_from_code_iso639_3("tsn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tso"): language_utilities.get_language_from_code_iso639_3("tso")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ven"): language_utilities.get_language_from_code_iso639_3("ven")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("xho"): language_utilities.get_language_from_code_iso639_3("xho")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("zul"): language_utilities.get_language_from_code_iso639_3("zul")
        result.append(Country("South Africa", "Republic of South Africa", "ZA", languages_for_ZA))
        
        languages_for_KR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kor"): language_utilities.get_language_from_code_iso639_3("kor")
        result.append(Country("South Korea", "Republic of Korea", "KR", languages_for_KR))
        
        languages_for_SS: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("South Sudan", "Republic of South Sudan", "SS", languages_for_SS))
        
        languages_for_ES: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Spain", "Kingdom of Spain", "ES", languages_for_ES))
        
        languages_for_LK: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sin"): language_utilities.get_language_from_code_iso639_3("sin")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tam"): language_utilities.get_language_from_code_iso639_3("tam")
        result.append(Country("Sri Lanka", "Democratic Socialist Republic of Sri Lanka", "LK", languages_for_LK))
        
        languages_for_SD: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Sudan", "Republic of the Sudan", "SD", languages_for_SD))
        
        languages_for_SR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nld"): language_utilities.get_language_from_code_iso639_3("nld")
        result.append(Country("Suriname", "Republic of Suriname", "SR", languages_for_SR))
        
        languages_for_SE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swe"): language_utilities.get_language_from_code_iso639_3("swe")
        result.append(Country("Sweden", "Kingdom of Sweden", "SE", languages_for_SE))
        
        languages_for_CH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("gsw"): language_utilities.get_language_from_code_iso639_3("gsw")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ita"): language_utilities.get_language_from_code_iso639_3("ita")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("roh"): language_utilities.get_language_from_code_iso639_3("roh")
        result.append(Country("Switzerland", "Swiss Confederation", "CH", languages_for_CH))
        
        languages_for_SY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Syria", "Syrian Arab Republic", "SY", languages_for_SY))
        
        languages_for_ST: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        result.append(Country("São Tomé and Príncipe", "Democratic Republic of São Tomé and Príncipe", "ST", languages_for_ST))
        
        languages_for_TJ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tgk"): language_utilities.get_language_from_code_iso639_3("tgk")
        result.append(Country("Tajikistan", "Republic of Tajikistan", "TJ", languages_for_TJ))
        
        languages_for_TZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swa"): language_utilities.get_language_from_code_iso639_3("swa")
        result.append(Country("Tanzania", "United Republic of Tanzania", "TZ", languages_for_TZ))
        
        languages_for_TH: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tha"): language_utilities.get_language_from_code_iso639_3("tha")
        result.append(Country("Thailand", "Kingdom of Thailand", "TH", languages_for_TH))
        
        languages_for_TL: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("por"): language_utilities.get_language_from_code_iso639_3("por")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tet"): language_utilities.get_language_from_code_iso639_3("tet")
        result.append(Country("Timor-Leste", "Democratic Republic of Timor-Leste", "TL", languages_for_TL))
        
        languages_for_TG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Togo", "Togolese Republic", "TG", languages_for_TG))
        
        languages_for_TO: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ton"): language_utilities.get_language_from_code_iso639_3("ton")
        result.append(Country("Tonga", "Kingdom of Tonga", "TO", languages_for_TO))
        
        languages_for_TT: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Trinidad and Tobago", "Republic of Trinidad and Tobago", "TT", languages_for_TT))
        
        languages_for_TN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Tunisia", "Tunisian Republic", "TN", languages_for_TN))
        
        languages_for_TM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tuk"): language_utilities.get_language_from_code_iso639_3("tuk")
        result.append(Country("Turkmenistan", "Turkmenistan", "TM", languages_for_TM))
        
        languages_for_TV: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tvl"): language_utilities.get_language_from_code_iso639_3("tvl")
        result.append(Country("Tuvalu", "Tuvalu", "TV", languages_for_TV))
        
        languages_for_TR: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tur"): language_utilities.get_language_from_code_iso639_3("tur")
        result.append(Country("Türkiye", "Republic of Türkiye", "TR", languages_for_TR))
        
        languages_for_UG: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("swa"): language_utilities.get_language_from_code_iso639_3("swa")
        result.append(Country("Uganda", "Republic of Uganda", "UG", languages_for_UG))
        
        languages_for_UA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ukr"): language_utilities.get_language_from_code_iso639_3("ukr")
        result.append(Country("Ukraine", "Ukraine", "UA", languages_for_UA))
        
        languages_for_AE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("United Arab Emirates", "United Arab Emirates", "AE", languages_for_AE))
        
        languages_for_GB: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("United Kingdom", "United Kingdom of Great Britain and Northern Ireland", "GB", languages_for_GB))
        
        languages_for_US: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("United States", "United States of America", "US", languages_for_US))
        
        languages_for_UY: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Uruguay", "Oriental Republic of Uruguay", "UY", languages_for_UY))
        
        languages_for_UZ: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("rus"): language_utilities.get_language_from_code_iso639_3("rus")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("uzb"): language_utilities.get_language_from_code_iso639_3("uzb")
        result.append(Country("Uzbekistan", "Republic of Uzbekistan", "UZ", languages_for_UZ))
        
        languages_for_VU: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bis"): language_utilities.get_language_from_code_iso639_3("bis")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("fra"): language_utilities.get_language_from_code_iso639_3("fra")
        result.append(Country("Vanuatu", "Republic of Vanuatu", "VU", languages_for_VU))
        
        languages_for_VA: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ita"): language_utilities.get_language_from_code_iso639_3("ita")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("lat"): language_utilities.get_language_from_code_iso639_3("lat")
        result.append(Country("Vatican City", "Vatican City State", "VA", languages_for_VA))
        
        languages_for_VE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("spa"): language_utilities.get_language_from_code_iso639_3("spa")
        result.append(Country("Venezuela", "Bolivarian Republic of Venezuela", "VE", languages_for_VE))
        
        languages_for_VN: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("vie"): language_utilities.get_language_from_code_iso639_3("vie")
        result.append(Country("Vietnam", "Socialist Republic of Vietnam", "VN", languages_for_VN))
        
        languages_for_YE: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ara"): language_utilities.get_language_from_code_iso639_3("ara")
        result.append(Country("Yemen", "Republic of Yemen", "YE", languages_for_YE))
        
        languages_for_ZM: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        result.append(Country("Zambia", "Republic of Zambia", "ZM", languages_for_ZM))
        
        languages_for_ZW: list[Country] = []
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("bwg"): language_utilities.get_language_from_code_iso639_3("bwg")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("eng"): language_utilities.get_language_from_code_iso639_3("eng")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("kck"): language_utilities.get_language_from_code_iso639_3("kck")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("khi"): language_utilities.get_language_from_code_iso639_3("khi")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ndc"): language_utilities.get_language_from_code_iso639_3("ndc")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nde"): language_utilities.get_language_from_code_iso639_3("nde")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("nya"): language_utilities.get_language_from_code_iso639_3("nya")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sna"): language_utilities.get_language_from_code_iso639_3("sna")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("sot"): language_utilities.get_language_from_code_iso639_3("sot")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("toi"): language_utilities.get_language_from_code_iso639_3("toi")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tsn"): language_utilities.get_language_from_code_iso639_3("tsn")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("tso"): language_utilities.get_language_from_code_iso639_3("tso")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("ven"): language_utilities.get_language_from_code_iso639_3("ven")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("xho"): language_utilities.get_language_from_code_iso639_3("xho")
        if LanguageCodeConversionUtilities().iso639_3_code_is_supported("zib"): language_utilities.get_language_from_code_iso639_3("zib")
        result.append(Country("Zimbabwe", "Republic of Zimbabwe", "ZW", languages_for_ZW))
        

        return result
