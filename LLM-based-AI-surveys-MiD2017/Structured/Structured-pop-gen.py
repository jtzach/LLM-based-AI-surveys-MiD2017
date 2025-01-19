import pandas as pd
import numpy as np

# Define the attributes and their distributions
attributes = {
    "Age Group": {
        "14 to 17 years": 4,
        "18 to 29 years": 14,
        "30 to 39 years": 12,
        "40 to 49 years": 14,
        "50 to 59 years": 16,
        "60 to 64 years": 6,
        "65 to 74 years": 10,
        "75 to 79 years": 6,
        "80 years and older": 5
    },
    "Education Level": {
        "no degree (yet)": 4,
        "low": 38,
        "medium": 38,
        "high": 20
    },
    "Main Activity": {
        "full-time employee (including trainees)": 35,
        "part-time employee (11 to 35 hours per week)": 12,
        "Employed person without details on the extent of education": 1,
        "Pupil including preschool": 6,
        "Student": 14,
        "housewife/househusband": 5,
        "Pensioner not employed": 21,
        "other activity": 7
    },
    "Household Type": {
        "young people living alone": 4,
        "middle-aged singles": 16,
        "older singles": 21,
        "young two-person households": 3,
        "middle-aged two-person households": 11,
        "older two-person households": 18,
        "Households with at least 3 adults": 7,
        "Households with at least 1 child under 6 years": 7,
        "Households with at least 1 child under 14 years": 7,
        "Households with at least 1 child under 18 years": 4,
        "Single parents": 2
    }
}

# Population size to generate
population_size = 10000

# Generate the synthetic population
synthetic_population = []

for i in range(population_size):
    person = {}
    for attr, weights in attributes.items():
        person[attr] = np.random.choice(
            list(weights.keys()), 
            p=np.array(list(weights.values())) / sum(weights.values())
        )
    synthetic_population.append(person)

# Convert to DataFrame
df_synthetic_population = pd.DataFrame(synthetic_population)

# Save to Excel
file_path = "/mnt/data/Synthetic_Population_Germany_2017.xlsx"
df_synthetic_population.to_excel(file_path, index=False)

file_path
