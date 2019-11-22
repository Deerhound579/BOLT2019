from colour import Color


def create_hue(tags: list): # a list of tags by store
    hueDict = {"red":0, "blue":(217/360),"green":(117/360),"purple":(291/360)}
    return list(map (lambda x : hueDict[x], tags))
def create_lumin(freq: list): # a list of freq by store
    minv, maxv = min(freq), max(freq)
    diff = maxv-minv
    return list(map (lambda x : 130-(50+(x-minv) / (diff) * 30) , freq)) 
def create_color(hue:list, lum:list): # return a list of colors in hex
    colors = []
    sat = 1
    huelumTuples = zip(hue,lum)
    for h, l in huelumTuples:
        colors.append(Color(h, sat, l))
    return list(map(lambda c: c.hex, colors))

tags = # get tag list
freqs = # get freq list

colors = create_color(create_hue(tags), create_lumin(freqs))