# Define possible responses and their probabilities for each question
responses = {
    "I like to walk in everyday life.": {
        "strongly agree": 30,
        "agree": 40,
        "disagree": 20,
        "strongly disagree": 10
    },
    "I enjoy cycling in everyday life.": {
        "strongly agree": 25,
        "agree": 35,
        "disagree": 25,
        "strongly disagree": 15
    },
    "I enjoy driving my car in everyday life.": {
        "strongly agree": 40,
        "agree": 30,
        "disagree": 20,
        "strongly disagree": 10
    },
    "I like to travel by bus and train in everyday life.": {
        "strongly agree": 20,
        "agree": 40,
        "disagree": 30,
        "strongly disagree": 10
    },
    "Number of trips with at least one overnight stay in the last three months": {
        "no trip": 50,
        "1 trip": 20,
        "2 trips": 15,
        "3 trips": 10,
        "4 trips and more": 5
    }
}

# Assign responses to each individual in the synthetic population
for question, weights in responses.items():
    df_synthetic_population[question] = np.random.choice(
        list(weights.keys()),
        size=population_size,
        p=np.array(list(weights.values())) / sum(weights.values())
    )

# Save the updated dataset to a new Excel file
updated_file_path = "/mnt/data/Synthetic_Population_Germany_2017_with_Responses.xlsx"
df_synthetic_population.to_excel(updated_file_path, index=False)

updated_file_path
