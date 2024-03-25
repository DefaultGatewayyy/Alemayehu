import datetime
# Get the current datetime
def timestamp():
    now = datetime.datetime.now()

    # Format the datetime object as a string without microseconds
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted time
    print(now)
    return now