import datetime


def process_times_point(times):

    # sprawdzenie jaki jest dzien tygodnia
    time_now = datetime.datetime.now().replace(second=0, microsecond=0)
    day_of_week = time_now.weekday()

    # jezeli dzien jest zly to pomijamy
    if not times[day_of_week]['on']:
        return False

    # prejscie do danego dnia w czasach i sprawdzenie czy sie miescimy

    time_on_split = times[day_of_week]['time'].split(':')

    time_on = time_now.replace(hour=int(time_on_split[0]), minute=int(time_on_split[1]), second=0, microsecond=0)

    if time_on == time_now:
        return True
    else:
        return False


def process_times_between(times):

    # sprawdzenie jaki jest dzien tygodnia
    time_now = datetime.datetime.now()
    day_of_week = time_now.weekday()

    # jezeli dzien jest zly to pomijamy
    if not times[day_of_week]['on']:
        return False

    # prejscie do danego dnia w czasach i sprawdzenie czy sie miescimy

    time_off_split = times[day_of_week]['to'].split(":")
    time_on_split = times[day_of_week]['from'].split(':')

    time_off = time_now.replace(hour=int(time_off_split[0]), minute=int(time_off_split[1]), second=0,
                                microsecond=0)
    time_on = time_now.replace(hour=int(time_on_split[0]), minute=int(time_on_split[1]), second=0, microsecond=0)

    if time_on <= time_now < time_off:
        return True
    else:
        return False


#do dokonczenia
def process_times_states(times):

    percent = 0

    # sprawdzenie jaki jest dzien tygodnia
    time_now = datetime.datetime.now()
    day_of_week = time_now.weekday()

    # jezeli dzien jest zly to pomijamy
    if not times[day_of_week]['on']:
        return percent

    # prejscie do danego dnia w czasach i sprawdzenie czy sie miescimy

    for state in times[day_of_week]['states']:
        time_split = state['time'].split(":")
        time_state = time_now.replace(hour=int(time_split[0]), minute=int(time_split[1]), second=0,
                                      microsecond=0)

        if time_now < time_state:
            return percent
        else:
            percent = int(state['percent'])
    return percent



