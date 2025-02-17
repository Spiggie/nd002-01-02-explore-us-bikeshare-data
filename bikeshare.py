import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Today, we\'re offering data for Chicago, New York City, or Washington...')
    print('For which city would you like to get some insights?')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        input_city = input('City: ')
        if input_city.lower() == 'chicago':
            city = 'chicago'
            break
        elif input_city.lower() == 'new york city':
            city = 'new york city'
            break
        elif input_city.lower() == 'washington':
            city = 'washington'
            break
        else:
            print('Sorry, but I did not understand your input. Can you please try again...?')

    print('Great choice! Here is some data analysis for {}.\n'.format(city.title()))
    
    # get user input for month (all, january, february, ... , june)
    print('For what month do you want to see the data? You can select a specific month (e.g. \'March\') or just say \'all\'.')
    while True:
        input_month = input('Month: ')
        # All
        if input_month.lower() in ['all', '0', '00']:
            month = 'all'
            break
        # January
        elif input_month.lower() in ['january', 'jan', '1', '01']:
            month = 'january'
            break
        # February
        elif input_month.lower() in ['february', 'feb', '2', '02']:
            month = 'february'
            break
        # March
        elif input_month.lower() in ['march', 'mar', '3', '03']:
            month = 'march'
            break
        # April
        elif input_month.lower() in ['april', 'apr', '4', '04']:
            month = 'april'
            break
        # May
        elif input_month.lower() in ['may', '5', '05']:
            month = 'may'
            break
        # June
        elif input_month.lower() in ['june', 'jun', '6', '06']:
            month = 'june'
            break
        else:
            print('Sorry, but I did not understand your input. Can you please try again...?')

    # Seperate message for 'all'
    if month == 'all':
        print('Wonderful! I\'ll show you the data for all months.\n')
    else:
        print('Wonderful! I\'ll show you the data for {}.\n'.format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('What week day are you interested in? Again, you can choose \'all\' if you wish.')
    while True:
        input_day = input('Week Day: ')
        # All
        if input_day.lower() in ['all', '0', '00']:
            day = 'all'
            break
        # Monday
        elif input_day.lower() in ['monday', 'mon', 'mo', '1', '01']:
            day = 'monday'
            break
        # Tuesday
        elif input_day.lower() in ['tuesday', 'tue', 'tu', '2', '02']:
            day = 'tuesday'
            break
        # Wednesday
        elif input_day.lower() in ['wednesday', 'wed', 'we', '3', '03']:
            day = 'wednesday'
            break
        # Thursday
        elif input_day.lower() in ['thursday', 'thu', 'th', '4', '04']:
            day = 'thursday'
            break
        # Friday
        elif input_day.lower() in ['friday', 'fri', 'fr', '5', '05']:
            day = 'friday'
            break
        # Saturday
        elif input_day.lower() in ['saturday', 'sat', 'sa', '6', '06']:
            day = 'saturday'
            break
        # Sunday
        elif input_day.lower() in ['sunday', 'sun', 'su', '7', '07']:
            day = 'sunday'
            break
        else:
            print('Sorry, but I did not understand your input. Can you please try again...?')

    if day == 'all':
        print('Yay, we\'re done! Here\'s the data for all week days!\n\n')
    else:
        print('Yay, we\'re done! Here\'s the data for {}s!\n\n'.format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract start hour from Start Time to create new column
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month: {}'.format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most popular day of week: {}'.format(popular_day))

    # display the most common start hour
    popular_start_hour = df['start_hour'].mode()[0]
    print('Most popular start hour: {}'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).to_frame(name='Count').reset_index().iloc[0]
    # https://stackoverflow.com/a/40872584
    most_frequent_start = most_frequent_combination['Start Station']
    most_frequent_stop = most_frequent_combination['End Station']
    most_frequent_count = most_frequent_combination['Count']
    print('Most popular trip: {} --> {} ({} times)'.format(most_frequent_start, most_frequent_stop, most_frequent_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: {}, or {} seconds.'.format(convert_seconds_to_human_readable_time(total_travel_time), total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: {}, or {} seconds.'.format(convert_seconds_to_human_readable_time(mean_travel_time), mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('There are {} different user types in total:'.format(df['User Type'].nunique()))
    for user_type, count in df['User Type'].value_counts().iteritems():
        print('** {}: {}'.format(user_type, count))

    # Display counts of gender
    if 'Gender' in df.columns:
        print('There are {} different genders in total:'.format(df['Gender'].nunique()))
        for gender, count in df['Gender'].value_counts().iteritems():
            print('** {}: {}'.format(gender, count))
    else:
        print('No gender available in given data.')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_common = df['Birth Year'].mode()[0]
        birth_year_earliest = df['Birth Year'].min()
        birth_year_most_recent = df['Birth Year'].max()
        print('Most common birth year: {}'.format(int(birth_year_common)))
        print('Earliest birth year: {}'.format(int(birth_year_earliest)))
        print('Most recent birth year: {}'.format(int(birth_year_most_recent)))
    else:
        print('No birth year available in given data.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def convert_seconds_to_human_readable_time(seconds):
    '''Converts the given seconds into a human readable string.'''
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    if d > 0:
        return '%d days %02dh%02dm%02ds' % (d, h, m, s)
    else:
        return '%2dh%02dm%02ds' % (h, m, s)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

            
if __name__ == "__main__":
	main()