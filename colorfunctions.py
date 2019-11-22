from colour import Color


def create_hue(tags: list): # a list of tags by store
    hueDict = {"Food and Dining":0, "Entertainment":(217/360),"Shopping":(117/360),"Home":(291/360)}
    return list(map (lambda x : hueDict[x], tags))
def create_lumin(freq: list): # a list of freq by store
    minv, maxv = min(freq), max(freq)
    diff = maxv-minv
    return list(map (lambda x : (130-(50+(x-minv) / (diff) * 30))/100 , freq))
def create_color(hue:list, lum:list): # return a list of colors in hex
    colors = []
    sat = 1
    huelumTuples = zip(hue,lum)
    for h, l in huelumTuples:
        colors.append(Color(hsl=(h, sat, l)))
    return list(map(lambda c: c.hex, colors))
