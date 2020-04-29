def convert_seconds(sec):
    m, s = divmod(sec, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    return ('%dd %02d:%02d:%02d' % (d, h, m, s))
