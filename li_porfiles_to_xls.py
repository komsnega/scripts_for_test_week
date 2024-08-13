import os
import pandas as pd

# Folder containing your LinkedIn text files
folder_path = r'C:\Users\Pavel\Documents\CV\Sally Test\li profiles as txts'

# Initialize an empty list to store rows of data
data = []

# Get a list of text files, ensuring they are sorted numerically
txt_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.txt')], key=lambda x: int(os.path.splitext(x)[0]))

# Loop through each text file in numerical order
for filename in txt_files:
    with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        name = last_name = title = None
        
        # Loop through lines to find the name and title
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Determine where to extract the name based on keywords
            if "Background Image" in line:
                # Name is on the next line
                name_line = lines[i + 1].strip()
                name_parts = name_line.split()
                
                # First word is first name, the rest is last name
                name = name_parts[0] if len(name_parts) > 0 else ''
                last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
            
            elif "Advertise" in line and name is None:
                # Name is on the next line if "Background Image" wasn't found
                name_line = lines[i + 1].strip()
                name_parts = name_line.split()
                
                # First word is first name, the rest is last name
                name = name_parts[0] if len(name_parts) > 0 else ''
                last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''
            
            # Extract the title after the "logo" line
            elif "logo" in line.lower() and title is None:
                # Assume the title is on the next line
                title_line = lines[i + 1].strip()
                
                # Split title in half to check for repetition
                half_len = len(title_line) // 2
                if title_line[:half_len].strip() == title_line[half_len:].strip():
                    title = title_line[:half_len].strip()
                else:
                    title = title_line
            
            # Stop if we have found both name and title
            if name and title:
                break
        
        # Append data to the list
        if name and title:
            data.append({'Name': name, 'Last Name': last_name, 'Position': title})

# Convert the list to a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Last Name', 'Position'])

# Save to Excel in the specified output folder
output_folder = r'C:\Users\Pavel\Documents\CV\Sally Test\scripts_for_test_week'
output_file = os.path.join(output_folder, 'linkedin_profiles.xlsx')

# Write to Excel file
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False)

print(f"Data saved to {output_file}")
