



for beer in range(99, 1, -1):
    print('{} bottles of beer on the wall,{} bottles of beer ...'.format(beer, beer))
    print('If one of those bottles should happen to fall, {} bottles of beer on the wall...'.format(beer-1))

    if beer == 1:
        print('{} bottle of beer on the wall,{} bottle of beer ...'.format(beer, beer))
        print('If one of those bottles should happen to fall, {} bottles of beer on the wall...'.format('no'))
        
