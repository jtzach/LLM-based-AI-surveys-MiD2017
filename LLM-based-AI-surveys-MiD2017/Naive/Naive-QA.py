# Define response distributions for the questions

# Responses for agreement statements
agreement_responses = ["strongly agree", "agree", "disagree", "strongly disagree"]
agreement_distribution = [25, 40, 25, 10]  # approximate percentages

# Responses for number of trips
trip_responses = ["no trip", "1 trip", "2 trips", "3 trips", "4 trips and more"]
trip_distribution = [40, 25, 20, 10, 5]  # approximate percentages

# Assign responses to each person in the synthetic population
synthetic_population["Agree with Walking"] = np.random.choice(agreement_responses, size=population_size, p=np.array(agreement_distribution)/100)
synthetic_population["Agree with Cycling"] = np.random.choice(agreement_responses, size=population_size, p=np.array(agreement_distribution)/100)
synthetic_population["Agree with Driving"] = np.random.choice(agreement_responses, size=population_size, p=np.array(agreement_distribution)/100)
synthetic_population["Agree with Bus and Train"] = np.random.choice(agreement_responses, size=population_size, p=np.array(agreement_distribution)/100)
synthetic_population["Number of Trips"] = np.random.choice(trip_responses, size=population_size, p=np.array(trip_distribution)/100)

# Display the updated dataset to the user
tools.display_dataframe_to_user(name="Synthetic Population with Survey Responses", dataframe=synthetic_population)
