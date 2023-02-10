__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    days = seconds//86400
    hours = (seconds - days*86400)//3600
    minuets =(seconds - days*86400 - hours*3600)//60
    sec = seconds%60
    time = [days, hours, minuets, sec]
    smth = ["d", "h", "m", "s"]
    time_str = ""
    i = 0
    while time[i] == 0 and i<len(time)-1:
        i += 1
    while i < len(time):
        if time[i]<10:
            time_str += "0" + str(time[i]) + smth[i]
        else:
            time_str += str(time[i]) + smth[i]
        i += 1
    return time_str







