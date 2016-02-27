import pandas

colnames = [
    'mls_number',
    'description',
    'num_bathrooms',
    'num_bedrooms',
    'building_type',
    'size_interior',
    'latitude',
    'longitude',
    'ownership_type',
    'sold',
    'days_on_market',
    'num_price_adjustments',
    'percent_change_price',
    'start_price',
    'current_price'
]

class Descriptions:
    def __init__(self, descriptions, prices):
        self.descriptions = descriptions
        self.prices = prices


def extract_descriptions(filename):
    data = pandas.read_csv(filename, names=colnames, header=0)

    descriptions = data.description.tolist()
    prices = data.current_price.tolist()

    return Descriptions(descriptions, prices)

print extract_descriptions('listings.csv')
