for beer in range(99, 0, -1):
    if beer >= 1:
        print('{} bottles of beer on the wall,{} bottles of beer ...'.format(beer, beer))
        print('If one of those bottles should happen to fall, {} bottles of beer on the wall...'.format(beer-1))

    else:
        print('{} bottle of beer on the wall,{} bottle of beer ...'.format(beer, beer))
        print('If one of those bottles should happen to fall, {} bottles of beer on the wall...'.format('no'))
