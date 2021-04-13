def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for n in range(0,length):
             for end in permute( LIST[:n] + LIST[n+1:] ):
                 yield [ LIST[n] ] + end

for x in permute(["3","3","4"]):
    print x
