import pandas as pd
import numpy as np

# Define population attributes and their distributions based on educated guesses
age_groups = ["14 to 17 years", "18 to 29 years", "30 to 39 years", "40 to 49 years", 
              "50 to 59 years", "60 to 64 years", "65 to 74 years", "75 to 79 years", "80 years and older"]
age_distribution = [8, 18, 15, 14, 15, 5, 15, 5, 5]  # approximate percentages summing to 100

education_levels = ["no degree (yet)", "low", "medium", "high"]
education_distribution = [5, 20, 50, 25]

main_activities = ["full-time employee (including trainees)", 
                   "part-time employee (11 to 35 hours per week)",
                   "Employed person without details on the extent of education",
                   "Pupil including preschool",
                   "Student",
                   "housewife/househusband",
                   "Pensioner not employed",
                   "other activity"]
main_activity_distribution = [40, 15, 5, 10, 10, 5, 10, 5]

economic_statuses = ["very low", "low", "medium", "high", "very high"]
economic_status_distribution = [15, 25, 30, 20, 10]

household_types = ["young people living alone", "middle-aged singles", "older singles",
                   "young two-person households", "middle-aged two-person households", 
                   "older two-person households", "Households with at least 3 adults",
                   "Households with at least 1 child under 6 years", 
                   "Households with at least 1 child under 14 years", 
                   "Households with at least 1 child under 18 years", 
                   "Single parents"]
household_type_distribution = [10, 15, 10, 10, 15, 10, 5, 10, 5, 5, 5]

# Create a synthetic population
population_size = 10000  # Adjust as necessary
np.random.seed(42)

data = {
    "Age Group": np.random.choice(age_groups, size=population_size, p=np.array(age_distribution)/100),
    "Education Level": np.random.choice(education_levels, size=population_size, p=np.array(education_distribution)/100),
    "Main Activity": np.random.choice(main_activities, size=population_size, p=np.array(main_activity_distribution)/100),
    "Economic Status": np.random.choice(economic_statuses, size=population_size, p=np.array(economic_status_distribution)/100),
    "Household Type": np.random.choice(household_types, size=population_size, p=np.array(household_type_distribution)/100)
}

# Create a DataFrame
synthetic_population = pd.DataFrame(data)

# Display a sample to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Synthetic Population of Germany 2017", dataframe=synthetic_population)
