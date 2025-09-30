class india():

    def capital (self):
        print('new delhi')

    def language (self):
        print('hindi')

    def status (self):
        print("developing")


class Nepal():

    def capital (self):
        print('kathmandu')

    def language (self):
        print('nepali')

    def status (self):
        print("under developed")

ind_obj = india()
nep_obj = Nepal()

for country in (ind_obj, nep_obj):
    country.capital()
    country.language()
    country.status()