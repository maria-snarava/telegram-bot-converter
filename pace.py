def main():
    try:
        kilometers_per_hour = float(input("Enter value in kilometers per hour: "))
        first_run = Run(kilometers_per_hour)

        print(f"{first_run.speed} kilometers per hour is equal to {first_run.pace} pace!")
    except:
        print('Cannot print the result! Your variables are not numbers.')


class Run:
    def __init__(self, speed):
        self.speed = speed
        self.pace_minutes = 0
        self.pace_seconds = 0
        self.pace = self.calculate_pace()

    # calculating pace from speed
    def calculate_pace(self):
        self.pace_minutes = int(60 // self.speed)
        self.pace_seconds = int((60 / self.speed) % 1 * 60)

        return self._format_time()

    # format time from float to mm:ss format
    def _format_time(self):
        result = ''
        pace_time = [self.pace_minutes, self.pace_seconds]
        for el in pace_time:
            if el < 10:  # use and/or/not for && || !
                el = "0" + str(el)
            else:  # use elif for 'else if'
                el = str(el)

            if result:
                result += ':' + el
            else:
                result += el

        return result


# run main function
if __name__ == '__main__':
    main()

