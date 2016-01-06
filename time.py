def convert_time_to_military(time):
    split_time = time.split(":")

    if "PM" in split_time[-1]:
        hour = int(split_time[0]) + 12
        military_time = [str(hour), split_time[1], split_time[2][:2]]
        print "{}:{}:{}".format(military_time[0], military_time[1], military_time[2])

convert_time_to_military("07:05:45PM")
