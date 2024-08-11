This README covers scripts:
- host_names_vs_two_tabs


---

# host_names_vs_two_tabs


This Python script reads data from an Excel file and searches for specific keywords within two sheets. It identifies and records all matches found in the "Company" and "Company name" columns, then saves the results in a text file.

## Features

- **Keyword Matching**: Searches for multiple keywords across two Excel sheets.
- **Detailed Reporting**: Records all matches found in both sheets, including the associated company names and countries (if applicable).
- **Text Output**: Saves the results in a `result.txt` file for easy review.

## Requirements

- Python 3.x
- pandas library

## Installation

1. Clone the repository or download the script.
2. Ensure you have Python 3.x installed.
3. Install the necessary Python packages by running:

   ```bash
   pip install pandas
   ```

## Usage

1. **Prepare Your Excel File**: Place the Excel file with your data in the specified directory.

2. **Update the File Path**: In the script, update the `file_path` variable to the path of your Excel file.

3. **Customize Keywords**: Modify the `word_list` variable to include the keywords you want to search for.

4. **Run the Script**: Execute the script to perform the keyword matching.

   ```bash
   python company_name_matcher.py
   ```

5. **View Results**: The script will generate a `result.txt` file in the current directory, containing all matches.

## Example

If the Excel file contains company names like "Haelo International" and "Luxury Stays," and the keyword list includes "Haelo" and "Luxury," the output in `result.txt` might look like:

```
word Haelo - matches:
  In 'Full Base' (Company, Country):
    Haelo International (USA)
    
word Luxury - matches:
  In 'с ними был колл' (Company name):
    Luxury Stays
```

## Customization

- **Adding More Keywords**: Extend the `word_list` in the script to include additional keywords.
- **Changing the Excel File**: Update the `file_path` variable to point to a different Excel file.

