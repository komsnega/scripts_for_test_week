This README covers scripts:
- host_names_vs_two_tabs
- country_check
- li_porfiles_to_xls


---

# host_names_vs_two_tabs script


This Python script reads data from an Excel file and searches for specific keywords within two sheets. It identifies and records all matches found in the "Company" and "Company name" columns, then saves the results in a text file.

## Features

- **Keyword Matching**: Searches for multiple keywords across two Excel sheets.
- **Detailed Reporting**: Records all matches found in both sheets, including the associated company names and countries (if applicable).
- **Text Output**: Saves the results in a `result_hosts.txt` file for easy review.

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

5. **View Results**: The script will generate a `result_hosts.txt` file in the current directory, containing all matches.

## Example

If the Excel file contains company names like "Haelo International" and "Luxury Stays," and the keyword list includes "Haelo" and "Luxury," the output in `result_hosts.txt` might look like:

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

Here's a draft README for your script:

---

# country_check script

This Python script reads data from an Excel file, compares a list of cities against the "Country" column in the dataset, and outputs the results to a text file. The script is useful for identifying records in the dataset that match specific cities.

## Features

- **Excel Data Processing**: Reads data from an Excel file.
- **City Matching**: Compares a predefined list of cities with the "Country" column in the dataset.
- **Output**: Generates a text file containing the results of the matching process.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `pandas`

You can install the required library using pip:

```bash
pip install pandas
```

## Usage

1. **Prepare the Excel File**: 
   - Ensure that your Excel file is properly formatted and saved at the specified location. 
   - The script is currently configured to read from the file path `C:\Users\Pavel\Documents\CV\Sally Test\Для кандидатов - база Aparta.xlsx`. You can change this to your actual file path if needed.
   - The script assumes the relevant data is in a sheet named `'Full Base'`.

2. **Specify the List of Cities**:
   - The script comes with a predefined list of cities. You can modify this list within the script if needed.

3. **Run the Script**:
   - Execute the script using a Python interpreter. 
   - The script will read the Excel file, perform the matching, and write the results to `result_country.txt`.

4. **Check the Output**:
   - The output will be saved in the same directory as the script under the filename `result_country.txt`.
   - The text file will contain the list of matches or indicate if no matches were found for each city.

## Example Output

```text
Matches for Lima:
  Company: ABC Corp

City Caracas - no matches

Matches for Tokyo:
  Company: XYZ Ltd
  Company: Tokyo Enterprises
```

## Customization

- **File Path**: You can change the `file_path` variable in the script to point to a different Excel file.
- **City List**: Update the `country_list` variable with the cities you want to match against the dataset.

-------

# li_porfiles_to_xls Script

## Overview

This Python script processes a batch of text files, each containing the content of a LinkedIn profile. The script extracts the first name, last name, and position title from each profile and saves the extracted information into an Excel spreadsheet.

## Features

- **Name Extraction**: The script extracts the first name and last name from specific lines in the text file. If the line containing "Background Image" is present, the name is taken from the line immediately following it. If "Background Image" is absent, the name is extracted from the line following the one with the word "Advertise."
  
- **Position Title Extraction**: The script identifies the position title from the line following the first occurrence of the word "logo" in the file. It handles repetition in titles by checking if the title appears twice consecutively and removes the duplication.
  
- **Numerical File Processing**: Text files are processed in numerical order, starting from `1.txt` and continuing to the highest number. This ensures that profiles are handled sequentially based on the file naming convention.

## Prerequisites

- **Python 3.x**
- **Pandas**: Install with `pip install pandas`
- **XlsxWriter**: Install with `pip install XlsxWriter`

## Script Usage

### Folder Structure

The script assumes the following folder structure:

- **LinkedIn Text Files**: A folder containing the text files of LinkedIn profiles (e.g., `1.txt`, `2.txt`, etc.).
- **Output Folder**: A folder where the generated Excel file will be saved.

### Example Folder Paths
- LinkedIn Text Files: `C:\Users\Pavel\Documents\CV\Sally Test\li profiles as txts`
- Output Folder: `C:\Users\Pavel\Documents\CV\Sally Test\scripts_for_test_week`

### Running the Script

1. **Place the text files** in the designated folder.
2. **Update the `folder_path` and `output_folder` variables** in the script to reflect your folder structure.
3. **Run the script**: The script will process all text files in numerical order, extract the required information, and save it to an Excel file.

### Output

The output is an Excel file named `linkedin_profiles.xlsx`, saved in the specified output folder. It contains the following columns:

- **Name**: The first name extracted from the profile.
- **Last Name**: The last name (or any other part of the name following the first word).
- **Position**: The extracted job title.

### Example Output

| Name | Last Name | Position |
|------|-----------|----------|
| Lena | Katz      | Chief Technology Officer |
| Jia  | Wun       | Senior Special Admin & Operations Manager |

## Customization

- **Change Extraction Logic**: The script can be adjusted to look for different keywords or lines for name and position extraction.
- **Change Output Format**: You can modify the script to save the output in formats other than Excel, such as CSV.
