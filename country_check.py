import pandas as pd

# Read the Excel file (replace 'your_file.xlsx' with your actual file name)
file_path = r'C:\Users\Pavel\Documents\CV\Sally Test\Для кандидатов - база.xlsx'
df = pd.read_excel(file_path, sheet_name='Full Base')

# Your list of countries
country_list = ['Toronto', 'Montreal', 'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg', 'Mississauga', 'Vancouver', 'Brampton', 'Hamilton']

# Initialize an empty result string
result = ""

# Compare each country with the content of the "Country" column
for country in country_list:
    matches = df[df['Country'].str.contains(country, case=False, na=False)]

    if matches.empty:
        result += f"City {country} - no matches\n\n"
    else:
        result += f"Matches for {country}:\n"
        for index, row in matches.iterrows():
            result += f"  Company: {row['Company']}\n"
        result += "\n"

# Write the result to a text file
with open('result_country.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(result)

print("Result saved to result_country.txt")