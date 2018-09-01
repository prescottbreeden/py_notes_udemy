def make_song(bottles=99, liquid_name='soda'):
    i = bottles
    while i > 0:
        if i is not 1:
            yield "{} bottles of {} on the wall.".format(i, liquid_name)
        else:
            yield "Only {} bottle of {} left!".format(i, liquid_name)
        i -= 1
    yield "No more {}!".format(liquid_name)


lyric = make_song(10, 'beer')
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
print(next(lyric))
