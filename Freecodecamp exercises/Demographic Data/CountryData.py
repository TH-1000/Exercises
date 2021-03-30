from fpdf import FPDF # a PDF constructor library
import pandas as pd

def calculate_demographic_data(file):
    # Read data from file
    df = pd.read_csv(file)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex == 'Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df.education == 'Bachelors'].shape[0]/df.shape[0])*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
   
    # Define higher and lower education to get the percentages:
    higher_education =  df[(df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate')]
    lower_education = df[(df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')]

    # Percentage with salary >50K
    higher_education_rich = round((higher_education[higher_education.salary == '>50K'].shape[0]/higher_education.shape[0])*100,1)
    lower_education_rich = round((lower_education[lower_education.salary == '>50K'].shape[0]/lower_education.shape[0])*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = (df[(df['hours-per-week'] == min_work_hours) & (df.salary == '>50K')].shape[0]/num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df.salary == '>50K']['native-country'].value_counts().idxmax(axis = 0)
    highest_earning_country_percentage = (df[df.salary == '>50K']['native-country'].value_counts().max()/df[df.salary == '>50K']['native-country'].shape[0]) * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.occupation[df.salary == '>50K'].value_counts().idxmax(axis = 0)
    
    result = f'''
Number of each race:\n{race_count}
Average age of men: {average_age_men}
Percentage with Bachelors degrees: {percentage_bachelors}%
Percentage with higher education that earn >50K: {higher_education_rich}%
Percentage without higher education that earn >50K: {lower_education_rich}%
Min work time: {min_work_hours} hours/week
Percentage of rich among those who work fewest hours: {rich_percentage}%
Country with highest percentage of rich: {highest_earning_country}
Highest percentage of rich people in country: {highest_earning_country_percentage}%
Top occupations in India: {top_IN_occupation}
    '''
    
    # Construct a PDF and export result
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0,10,result, border = 1)
    pdf.output('adult_data.pdf', 'F')
    
    print(result)
    return result
  

calculate_demographic_data('adult_data.csv')
