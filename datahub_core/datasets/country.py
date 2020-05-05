class Country:
    """
    Country Datatype

    # Attributes:

        {
            short_name: str
            alpha2_code: str
            alpha3_code: str
            locale: str
            currency: str
            region: str
            country_id: str
        }

    """

    short_name: str
    alpha2_code: str
    alpha3_code: str
    locale: str
    currency: str
    region: str
    country_id: str

    def __init__(self, shortName, alpha2_code, alpha3_code, locale, currency, region, country_id):
        self.short_name = shortName
        self.alpha2_code = alpha2_code
        self.alpha3_code = alpha3_code
        self.locale = locale
        self.region = region
        self.currency = currency
        self.country_id = country_id
