import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list = ['January', 'February', 'March', 'April', 'May', 'June']
day_list = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()
    while city not in CITY_DATA.keys():
        print("Invalid input of City\n")
        city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower() 

    # TO DO: get user input for month (all, january, february, ... , june)
    filter = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter\n").lower()
    filter_list= ['month', 'day', 'both', 'none']
    
    while filter not in filter_list:
            print("Invalid input\n")
            filter = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter\n").lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if filter == 'month':
        month = input("\nWhich month? January, February, March, April, May, or June?\n").title()
        while month not in month_list:
            print("Invalid month input\n")
            month = input("\nWhich month? January, February, March, April, May, or June?\n").title()
        day = 0
    elif filter == 'day':
        day = input("\nWhich day? Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday?\n").title()
        while day not in day_list:
            print("Invalid day input\n")
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday?\n").title()
        month = 0
        
    elif filter == 'both':
        month = input("\nWhich month? January, February, March, April, May, or June?\n").title()
        while month not in month_list:
            print("Invalid month input\n")
            month = input("\nWhich month? January, February, March, April, May, or June?\n").title()

        day = input("\nWhich day? Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday?\n").title()
        while day not in day_list:
            print("Invalid day input\n")
            day = input("\nWhich day? Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday?\n").title()
            
    elif filter =='none':
        month =0
        day = 0
    
    print('-'*40)
    print('output {} {} {}'.format(city, month, day))
    
    if month !=0:
        month = month_list.index(month)+1

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
    df = pd.read_csv(CITY_DATA [city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Do the filter below
    # no filter is applied
    if month == 0 and day == 0:
        return df
    # only filter by day
    elif month == 0:
        df = df[df['day_of_week']==day]
    # only filter by month
    elif day == 0:
        df = df[df['month']== month]
    else:
        df = df[df['day_of_week']==day]
        df = df[df['month']== month]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('most common month: {}'.format(df['month'].mode()[0])  + '\n')

    # TO DO: display the most common day of week
    print('most common day of week: {}'.format(df['day_of_week'].mode()[0]) + '\n')

    # TO DO: display the most common start hour
    print('most most common start hour: {}'.format(df['hour'].mode()[0]) + '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station : {}'.format(df.groupby(['Start Station']).count().idxmax()[0]))
    
    # TO DO: display most commonly used end station
    print('most commonly used end station : {}'.format(df.groupby(['End Station']).count().idxmax()[0]))
    

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' ' + df['End Station']
    print('most commonly used start - end station : {}'.format(df.groupby(['Start End']).count().idxmax()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time : {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('total travel time : {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types : {}'.format(len(df['User Type'].unique())))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('counts of gender : {}'.format(len(df['Gender'].unique())))
    else:
        print('Gender information not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('counts of earliest, most recent, and most common year of birth : {}'.format(df['Birth Year'].max()))
    else:
        print('Earliest, most recent, and most common year of birth information not available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def showRawData(df):
    
    show_raw_data = input("Would you like to see the raw data? [Y/N]").lower()
    N = 5
    while show_raw_data == 'y':
        print(df[N-5:N])
        show_raw_data = input("Show more raw data? [Y/N]").lower()
        N+=5
        
    print('-'*40)

    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        showRawData(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
