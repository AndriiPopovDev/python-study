def describe_city(name, country='ukraine'):
    print(f"{name.title()} is in {country.title()}.")

describe_city('kyiv')
describe_city('charkiv', 'ukraine')
describe_city('washinghton', 'usa')