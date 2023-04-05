import pandas as pd
from sklearn.preprocessing import LabelEncoder



df = pd.read_csv("stud.csv")


le = LabelEncoder()
df['gender', 'race_ethnicity','parental_level_of_education', 'lunch', 'test_preparation_course'] = le.fit_transform()

print(df.head())