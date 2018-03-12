state_abvs = ['AK', 'AZ', 'MD']
state_names = ['Alaska', 'Arizona', 'Maryland']

for abv, name in zip(state_abvs, state_names):
    print('The abbrivation of {}, is {}.'.format(name, abv))
