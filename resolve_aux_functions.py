def timecodeToInt(timestamp):
    ret = ""
    for i in timestamp.split(':'):
        ret += i
    return int(ret)