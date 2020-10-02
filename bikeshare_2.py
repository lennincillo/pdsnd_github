import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              #this 2 variables will be used to check if the user insert a correct inputs
weak = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

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

    while True:
        city = input("Which city would you like analyse? Select one of this: chicago, new york city, washington\n")
        if city.lower() in CITY_DATA:
            print("Your city was selected, excellent, continue with the next filter...\n")
            break
        else:
            print("Try again with a city from the list: chicago, new york city, washington:\n")

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Select a month for filter your data or write all for no filter:" )

        if month.lower() in months:
            print("Your selection was correctly taken, excellent, just one final step...")
            break
        else:
            print("Try again with a month or all:")

    days =['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Select a day of the week for filter your data or tip all for no filter: ")

        if day.lower() in days:
            print("Perfect, all your inputs was received successfully, here are your statistics")
            break
        else:
            print("Try again with a day of the week weak (for example monday) or select all for no filter:")

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday
    df['Hour']=df['Start Time'].dt.hour
    df['travel']= 'starting in '+ df['Start Station'] + ' & ending in ' + df['End Station']

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
         # filter by month to create the new dataframe
        df = df[df['month'] == month]


    if day != 'all':
        # filter by day of week to create the new dataframe
        week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = week.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    # display the most common month

    popular_month = df['month'].mode()[0]
    oter_month = months[popular_month]
    print('The most popular month in this city was {} \n'.format(oter_month))
    # display the most common day of week

    oter_day = df['day_of_week'].mode()[0]
    popular_day = weak[oter_day]
    print('The most popular day for travel in this city was {} \n'.format(popular_day))
    # display the most common start hour

    popular_hour = df['Hour'].mode()[0]
    print('The most popular start time in this city was {} \n'.format(popular_hour))




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')


    # display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]
    print('The most popular start station in this city was {} \n'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print('The most popular End Station in this city was {} \n'.format(popular_end_station))

    # display most frequent combination of start station and end station trip

    popular_travel= df['travel'].mode()[0]
    print('The most popular travel in this city was {} \n'.format(popular_travel))




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""



    # display total travel time
    total_time_travel = df['Trip Duration'].sum()/3600
    print('The total time of trips in this city was {} hours!\n'.format(total_time_travel))
    # display mean travel time
    mean_time_travel = df['Trip Duration'].mean()/60
    print('The mean of travels in this city was {} min\n'.format(mean_time_travel))



def user_stats(df):
    """Displays statistics on bikeshare users."""


    try:
        # Display counts of user types
        user_types = df['User Type'].value_counts()
        print('The Diferent type user in this city were:\n {} \n'.format(user_types[:2]))
    except:
        print("There is not data for user types statistic")

    try:
        # Display counts of gender
        user_genders = df['Gender'].value_counts()
        print('This are separated between: {}\n'.format(user_genders[:1]))
    except:
        print("There is not data for gender statistic")
        # Display earliest, most recent, and most common year of birth
    try:
        earliest_yb = df['Birth Year'].min()
        recent_yb = df['Birth Year'].max()
        popular_common_yb= df['Birth Year'].mode()[0]
        print('The most common Birth Year in this city was {}, being {} the most earliest and {} the most recently \n'.format(popular_common_yb,earliest_yb,recent_yb))
    except:
        print("There is not data for birthday statistic")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #here we call all the fuctions that we has made until now
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw = input('\n Would you like see some raw information? Enter yes or no.\n')
        if raw.lower() == 'yes':
            i = 0
            try:
                while True:
                    print(df.iloc[i:i+5])
                    i += 5
                    nextfive = input('\nWould you like to see next 5 rows? Enter yes or no. \n')
                    if nextfive.lower() != 'yes':
                        break
            except:
                print("There is no more data")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
