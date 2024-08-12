import pandas as pd

# Read the Excel file (replace 'your_file.xlsx' with your actual file name)
file_path = r'C:\Users\Pavel\Documents\CV\Sally Test\Для кандидатов - база Aparta.xlsx'
df_tab1 = pd.read_excel(file_path, sheet_name='Full Base')
df_tab2 = pd.read_excel(file_path, sheet_name='с ними был колл')

# Your list of words
word_list = ['any', 'life']

# Initialize an empty result string
result = ""

# Compare each word with the content of cells in both tabs
for word in word_list:
    matches_tab1 = df_tab1[df_tab1['Company'].str.contains(word, case=False, na=False)]
    matches_tab2 = df_tab2[df_tab2['Company name'].str.contains(word, case=False, na=False)]

    if matches_tab1.empty and matches_tab2.empty:
        result += f"word {word} - no match neither with tab 'Full Base' nor tab 'с ними был колл'\n\n"
    else:
        result += f"word {word} - matches:\n"
        if not matches_tab1.empty:
            result += "  In 'Full Base' (Company, Country):\n"
            for index, row in matches_tab1.iterrows():
                result += f"    {row['Company']} ({row['Country']})\n"
        if not matches_tab2.empty:
            result += "  In 'с ними был колл' (Company name):\n"
            for index, row in matches_tab2.iterrows():
                result += f"    {row['Company name']}\n"
        result += "\n"

# Write the result to a text file
with open('result_hosts.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(result)

print("Result saved to result_hosts.txt")
