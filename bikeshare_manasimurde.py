import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_dict = {'january': 1, 'february':2, 'march':3, 'april':4, 'may':5, 'june': 6, 'all': 7}
day_dict = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #chicago
    while 1:
        city = input('Enter city name for which you would like to explore bikeshare data: Chicago, New York, or Washington?\n').lower()
        if city=='chicago':
            city='chicago'
        if city=='new york':
            city='new york city'
        if city=='washington':
            city='washington'
        if city not in CITY_DATA:
            print('Invalid entry!')
            continue
        city = CITY_DATA[city]
        break

    # TO DO: get user input for month (all, january, february, ... , june)
   
    while 1:
        month = input('\nEnter month for which you would like to see the bikeshare data: January, February, March, April, May, June or all?\n').lower()
        if month not in month_dict.keys():
            print("\nYou have entered an incorrect month, Please choose January, February, March, April, May, June, all\n")
            continue
            month = month_dict[month]
        else:
            month = 'all'
        break
       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while 1: 
        day = input('\nEnter the day for which you would like to see the bikeshare data: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n').lower()
        if day not in day_dict.keys():
            print('\nYou have entered an incorrect day, Please choose Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all\n')
            continue
            day = day_dict[day]
        else:
            day = 'all'
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
    print("\nLoading bikshare data...")
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    val = int(df['Start Time'].dt.month.mode())
    freq_month = months[val - 1]
    print('\nThe most frequently traveled month is {}'.format(freq_month))
 
    # TO DO: display the most common day of week
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    val = int(df['Start Time'].dt.dayofweek.mode())
    freq_day = day[val]
    print('\nThe most frequently traveled day is {}'.format(freq_day))

    # TO DO: display the most common start hour
    val = int(df['Start Time'].dt.hour.mode())
    print('\nThe most frequently traveled hour is {}'.format(val))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    stn_start = df['Start Station'].mode().to_string(index = False)
    print('\nThe most popular start station is {}'.format(stn_start))

    # TO DO: display most commonly used end station
    stn_end = df['End Station'].mode().to_string(index = False)
    print('\nThe most popular end station is {}'.format(stn_end))


    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    val = df['trip'].mode().to_string(index = False)
    print('\nThe most frequent combination of start station and end station trip is {}'.format(val))
    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    mins = round(total_time/60)
    print('The total travel time is {} minutes'.format(mins))


    # TO DO: display mean travel time
    mean_time = round(df['Trip Duration'].mean())
    mins = round(mean_time/60)
    print('The mean travel time is {} minutes'.format(mins))


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    subs = (df['User Type'] == 'Subscriber').sum()
    cust = (df['User Type'] == 'Customer').sum()
    print('\nTotal number of subscribers: {}'.format(subs))
    print('\nTotal number of customers: {}'.format(cust))

    
    # TO DO: Display counts of gender
    male = (df['Gender'] == 'Male').sum()
    female = (df['Gender'] == 'Female').sum()
    print('\nTotal male users: {}'.format(male))
    print('\nTotal female users: {}'.format(female))


    # TO DO: Display earliest, most recent, and most common year of birth
    dob_e = int(df['Birth Year'].min())
    dob_r = int(df['Birth Year'].max())
    dob_c = int(df['Birth Year'].mode())
    print('\nEarliest year of birth: {}'.format(dob_e))
    print('\nMost recent year of birth: {}'.format(dob_r))
    print('\nMost common year of birth: {}'.format(dob_c))


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

def display_data(df):
   
    response_list = ['yes','no']
    display = ''
    counter = 0
    while display not in response_list:
        display = input("\nWould you like to see the raw data? Enter yes or no\n").lower()
        if display == "yes":
            print(df.head())
        elif display not in response_list:
            print("\n'Invalid entry! Please try again.\n")
            #return

    while display == 'yes':
        display = input('Do you want to see the next 5? Enter yes or no\n').lower()
        counter += 5
        if display == "yes":
             print(df[counter:counter+5])
        elif display != "yes":
             break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
