import time
import pandas as pd
import numpy as np
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv',
              'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'chicago.csv' }
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
    while True:
           city = input("\nWhich city would you like to see the data for Chicago, New York City,  or Washington ?\n").lower()
           if city not in ('New York City', 'Chicago', 'Washington','new york city','chicago','washington'):
                print('Invalid input . Try again.')
                continue
           else:
                break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
          month=input('\nWhich month would you like to see the data for  January, February, March, April, May, June or "all" if you dont want to filter ?\n').lower() 
          if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all','january','february','march','april','may','june','All'):
               print('Invalid input. Retry.')
               continue
          else:
               break
              
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('\nWhich day of week would you like to see the data for  Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday or "all" to apply no day filter ?\n').lower()
        if day not in ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','all','sunday','monday','tuesday','wednesday','thursday','friday','saturday','All'):
               print('Invalid input. Try again.')
               continue
        else:
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
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
    # TO DO: display the most common month
    Popular_Month = df['month'].mode()[0]
    print('Most Common Month: ', Popular_Month)
    # TO DO: display the most common day of week
    Popular_Week=df['day_of_week'].mode()[0]
    print('Most Common Day: ',Popular_Week)
    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    Popular_Hour = df['Hour'].mode()[0]
    print('Most Common Hour: ', Popular_Hour)
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    start = df['Start Station'].mode()[0]
    print('Most Commonly used start station: ', start)
    # TO DO: display most commonly used end station
    end = df['End Station'].mode()[0]
    print('Most Commonly used end station: ', end)
    # TO DO: display most frequent combination of start station and end station trip
    df['Combined'] = df['Start Station'] + 'and' + df['End Station']
    print('Most frequent combination of start station and end station:  ', df['Combined'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    travel_time=df['Trip Duration'].sum()
    print('total travel time:  ', travel_time)
    
    # TO DO: display mean travel time
    travel_mean=df['Trip Duration'].mean()
    print('mean travel time:  ', travel_mean)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    types_of_user=df.groupby('User Type')['User Type'].count()
    print('counts of user types: ',types_of_user)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_of_gender=df.groupby('Gender')['Gender'].count()
        print('counts of gender: ',count_of_gender)
    else:
        print('No information about gender')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest = df['Birth Year'].min()
      print('\nEarliest Year:\n', earliest)
    except:
      print("No data avaliable for this month.")
    try:
      recent=df['Birth Year'].max()
      print('Most Recent Year: ', recent)
    except:
      print('No data avaliable for this month')
    
    
    try:
        frequent=df['Birth Year'].mode()[0]
        print('most common year of birth: ',frequent)
    except:
        print('No data avaliable for this month')
    
        
   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Display the raw data to the user and the number of data that they want to see"""
    while True:
        choice = input('do you want to see raw data ? press "y" for yes and "n" for no\n')
        number = 0
        if choice in ('y','n'):
            break
        else:
            print('invalid input.try again')
            continue
    while True:         
        if choice.lower() != 'n':
            print(df.iloc[number : number + 5])
            number += 5
            choice = input('\ndo you want to see more raw data? press "y" for yes and "n" for no\n')
        else:
            break 
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()



