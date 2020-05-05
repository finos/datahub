import datahub_core.generators.object_decorators as od

def test_decorators_on_object():
    entity = TestEntity()

    print(entity)
    print(f'count={entity.count}')
    print(f'number={entity.number}')
    print(f'region={entity.region}')


@od.synthetic_attributes()
class TestEntity:
    number: int
    count: int
    region: str

    @od.counter()
    def set_count(self, value):
        self.count = value

    @od.random_range_int(low=0, high=1000)
    def set_number(self, value):
        self.number = value

    @od.choice(values=['NAM', 'EMEA'], weights=[0.8, 0.2])
    def set_region(self, value):
        self.region = value
