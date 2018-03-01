# Using range() and a loop, print out the song like this:

# 99 bottles of beer on the wall, 99 bottles of beer ...
# If one of those bottles should happen to fall, 98 bottles of beer on the wall
# 98 bottles of beer on the wall, 98 bottles of beer ...
# If one of those bottles should happen to fall, 97 bottles of beer on the wall
for beer in range(99, -1, -1):
    print('{} bottles of beer on the wall,{} bottles of beer ...'.format(beer, beer))
