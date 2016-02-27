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

data = pandas.read_csv('listings.csv', names=colnames, header=0)

descriptions = data.description.tolist()
current_prices = data.current_price.tolist()

print current_prices
