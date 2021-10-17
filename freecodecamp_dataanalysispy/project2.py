import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("freecodecamp_dataanalysispy/project2.csv")
    # print(df)
    # print(df.head(5))
    # print(df.head())

    for i in df.head():
      print(i)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_list = df["race"].unique()
    # print(race_list)
    # print(type(race_list))
    race_count = df["race"].value_counts()
    race_count.index = race_list
    # print(type(race_count))

    # What is the average age of men?
    total_men = df.loc[df.sex=="Male"].sex.count()
    # print(total_men)
    total_age_men = df.loc[df.sex == "Male"].age.sum()
    # print(total_age_men)
    average_age_men = round(total_age_men/total_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    # print(df.education)
    total_ = df.education.count()
    # print(total_)
    total_bachelor_deg = df.loc[df.education == "Bachelors"].education.count()
    # print(total_bachelor_deg)
    percentage_bachelors = round(total_bachelor_deg*100/total_,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # print(df["salary"])
    adv = df.loc[(df.education=="Bachelors")|(df.education=="Masters")|(df.education=="Doctorate")]
    total_adv = adv.education.count()
    # print(total_adv)
    total_adv_rich = adv.loc[adv.salary == ">50K"].salary.count()
    # print(total_adv_rich)
    not_adv = df.loc[(df.education!="Bachelors")&(df.education!="Masters")&(df.education!="Doctorate")]
    total_not_adv = not_adv.education.count()
    # print(total_not_adv)
    total_not_adv_rich = not_adv.loc[not_adv.salary == ">50K"].salary.count()
    # print(total_not_adv_rich)

    # percentage with salary >50K
    higher_education_rich = round(total_adv_rich*100/total_adv,1)
    lower_education_rich = round(total_not_adv_rich*100/total_not_adv,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"]==min_work_hours].count()
    num_min_workers = num_min_workers["hours-per-week"]
    num_min_workers_rich = df.loc[(df["hours-per-week"]==min_work_hours)&(df.salary == ">50K")].count()
    num_min_workers_rich = num_min_workers_rich["hours-per-week"]

    rich_percentage = round(num_min_workers_rich*100/num_min_workers,1)

    # What country has the highest percentage of people that earn >50K?
    country_total = df.groupby("native-country").count()
    # print(country_total)
    country_rich = df.loc[df.salary == ">50K"].groupby("native-country").count()
    # print(country_rich)

    country_max = country_rich*100/country_total
    # print(country_max)
    # print(country_max.index.name)
    country_max = country_max.sort_values(by=["salary"])
    # print(country_max)

    highest_earning_country = country_max.loc[country_max.salary == country_max.salary.max()].index[0]
    highest_earning_country_percentage = round(country_max.salary.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation_list = df.loc[(df["native-country"] == "India")&(df.salary == ">50K")].groupby("occupation").count().sort_values(by=["salary"])
    print(top_IN_occupation_list)
    top_IN_occupation = top_IN_occupation_list.loc[top_IN_occupation_list.salary == top_IN_occupation_list.age.max()].index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()