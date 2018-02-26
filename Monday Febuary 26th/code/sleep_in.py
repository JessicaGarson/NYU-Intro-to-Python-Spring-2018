days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def sleep_in():
    for day in days_of_the_week:
        if day == 'Saturday' or day == 'Sunday':
            print('Today is {}, I can sleep in today!'.format(day))
        else:
            print('Today is {}, I have to go to work :('.format(day))


def main():
    sleep_in()


if __name__ == '__main__':
    main()
