import functools
import unicodedata

def soe_id(name_field):
    """
    Generates an SOE ID from a name

    # Arguments:

    name_field, str:

        The field in the dataframe which contains the name of the person
        to generate an SOE ID for

    # Returns:

        str

    # Example

        import numpy as np
        import datahub_core.generators as gen

        df = gen.generate(
            props={
                'region': gen.choice(
                    data=['EMEA', 'LATAM', 'NAM', 'APAC'],
                    weights=[0.1, 0.1, 0.3, 0.5]),
                "country": gen.country_codes(region_field='region'),
                "contact_name": gen.person(country_field='country'),
                "soe_id": gen.soe_id(name_field="contact_name")
            },
            count=50,
            randomstate=np.random.RandomState(13031981)
        ).to_dataframe()

        print(df)`

    """
    return functools.partial(__soe_id, name_field)

def __soe_id(name_field, df=None, randomstate=None):
    parts = df[name_field].split()
    prefix = ""

    for i in range(2):
        prefix = prefix + parts[i][0]

    number = randomstate.randint(low=10000, high=99999, size=1)[0]
    prefix = unicodedata.normalize('NFKD', prefix)
    prefix = prefix.encode('ascii', 'ignore')
    prefix = prefix.decode('ascii').upper()

    result = prefix + str(number)
    return result
