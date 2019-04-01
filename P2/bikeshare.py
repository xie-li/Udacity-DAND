import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Select month from {},{},{},{},{} or {}:".format(*months)).strip().lower()
        if city in months or month == 'all':
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("Select month from {},{},{},{}.{},{} or {}:".format(*days)).strip().lower()
        if day in days or day == 'all':
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
    #读取城市信息
    df = pd.read_csv(CITY_DATA[city])
    #将Start Time 转换为 datetime 数据类型
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #新增列当前月份以及当前是星期几
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month is %s'%df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day of week is %s'%df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour is %s'%df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   # TO DO: display most commonly used start station
    print('\nmost commonnly userd start station is %s' % (df['Start Station'].mode()[0]))
    # TO DO: display most commonly used end station
    print('\nmost commonnly userd end station is %s' % (df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+' / '+df['End Station']
    common_combine=df['combination'].value_counts().index[0]
    print('\nmost frequent combination of start station and end station trip is %s' % (common_combine))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is %.2f hours'%(df['Trip Duration'].sum()/3600))

    # TO DO: display mean travel time
    print('mean travel time is %.2f hours'%(df['Trip Duration'].mean()/3600))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    for idx,ut in enumerate(user_type):
        print('User Type:%s,Counts:%s'%(user_type.index[idx],ut))

    # TO DO: Display counts of gender 因为user type 为 cunstomer的用户没有性别，这里没有做NaN去除
    if 'gender' in df.columns:
        gender = df['Gender'].value_counts()
        for idx,g in enumerate(gender):
            print('Gender:%s,Counts:%s'%(gender.index[idx],g))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth=df['Birth Year'].min()
        recent_birth=df['Birth Year'].max()
        common_birth=df['Birth Year'].value_counts().index[0]
        print('Earliest user year of birth: %i.'%(earliest_birth))
        print('Most recent user year of birth: %i.'%(recent_birth))
        print('Most common user year of birth: %i.'%(common_birth))


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

