from datetime import datetime
def main():
    time = input("What time is it? ")
    if 7.0 <= convert(time) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(time) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(time) <= 8.0:
        print("dinner time")
    else:
        return            



def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes_to_hours = int(minutes)/60
    return hours + minutes_to_hours

if __name__ == "__main__":
    main()
