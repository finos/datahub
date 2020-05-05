"""

## Usages

``` python

  import datahub_core.generators

  gen.generate(
    props={
      "country": gen.country_codes(region_field='region'),
      "ev": gen.random_range_int(high=100000, low=10000000),
      "address": gen.address(country_field='country'),
      "contact_name": gen.person(country_field='country'),
      "client_name": gen.company_namer(
        field='client_type',
        field_type='client_type',
        countrycode_field='country'
      )
    },
    count=50, filename='./tests/omc_client.json', randomstate=RS
)


```


"""
