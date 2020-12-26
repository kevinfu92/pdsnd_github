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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    all_city = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Please enter the city to analyze (Chicago, New York City, Washington)\n')
        if city.lower() in all_city:
            break

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('Please enter the month to analyze (all, january, february, ... , june)\n')
        if month.lower() == 'all' or month.lower() in months:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input('Please enter the day of week to analyze (all, monday, tuesday, ... sunday)\n')
        if day.lower() == 'all' or day.lower() in days_of_week:
            break

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
    df = pd.read_csv(CITY_DATA[city.lower()]) 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day.lower() != 'all':
        days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_of_week = days_of_week.index(day)
        df = df[df['day'] == day_of_week] 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('The most commen month is', months[df['month'].mode()[0] - 1].title())

    # display the most common day of week
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('The most common day of week is', days_of_week[df['day'].mode()[0]].title())

    # display the most common start hour
    print('The most common start hour is', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most commonly used end station is', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start/End Station'] = df['Start Station'] + ' and ' + df['End Station']
    print('The most frequent combination of start station and end station trip is', df['Start/End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is:', str(df['Trip Duration'].sum()), 'seconds.')

    # display mean travel time
    print('The mean time is:', str(df['Trip Duration'].mean()), 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in list(df):
        print(df['User Type'].value_counts(), '\n')
    # Display counts of gender
    if 'Gender' in list(df):
        print(df['Gender'].value_counts(), '\n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in list(df):
        print('The earliest year of birth of customers is', str(int(df['Birth Year'].min())))
        print('The most recent year of birth of customers is', str(int(df['Birth Year'].max())))
        print('The most common year of birth of customers is', str(int(df['Birth Year'].mode()[0])))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
