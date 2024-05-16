import os
import pandas as pd

# Path to the directory containing the CSV files (relative to the repository root)
csv_directory = "./CSV_Files"

# Initialize the dictionary to store CSV file data
dict_of_csv_files = {}

# Iterate through each file in the specified directory
for filename in os.listdir(csv_directory):
    if filename.endswith(".csv"):
        file_key = filename.replace(" ", ":").replace(".csv", "")
        
        # Read the CSV file into a pandas DataFrame
        csv_path = os.path.join(csv_directory, filename)
        csv_file = pd.read_csv(csv_path, delimiter=',')
        csv_dict = csv_file.T.to_dict(orient='list')
        
        # Initialize the structure for file_data
        file_data = {'arrow': {"mandatory": [], "recommended": [], "optional": []},
                     'regular': {"mandatory": [], "recommended": [], "optional": []}}
            
        # Process each row in the CSV file
        for key, values in csv_dict.items():
            attr_type = values[2]
            arrow_type = values[4] == "-"
            regular_type = values[3] == "-"
            attr_desc = f"{values[1]} {values[5]} [{attr_type.replace('mandatory', '1').replace('recommended', '0').replace('optional', '1')}...{'*' if values[6] else '1'}]"

            if arrow_type:
                file_data['arrow'][attr_type].append(attr_desc)
            elif regular_type:
                file_data['regular'][attr_type].append(attr_desc)
        
        dict_of_csv_files[file_key] = file_data

# Prepare the data for Mermaid diagrams
mermaid_data = "```mermaid\nclassDiagram\n"
dict_of_csv_files_for_mermaid = {}

for class_name, attributes in dict_of_csv_files.items():
    class_block = f'class `{class_name}` {{\n'
    for category, attrs in attributes['regular'].items():
        class_block += f'  # {category}\n'
        for attr in attrs:
            class_block += f'  {attr.replace(":", "#58;")}\n'
    class_block += '}\n'
    mermaid_data += class_block
    dict_of_csv_files_for_mermaid[class_name] = class_block

# Generate arrow relationships for Mermaid
for class_name, attributes in dict_of_csv_files.items():
    arrow_relationships = ""
    for category, attrs in attributes['arrow'].items():
        for attr in attrs:
            source_class = f'`{class_name}`'
            target_class = f'`{attr.split()[1]}`'
            attribute_name = attr.split()[0].replace(':', '#58;')
            relationship_type = attr.split()[2].replace('[', '"').replace(']', '"').replace('...', '..')
            arrow_relationships += f'{source_class} --> {relationship_type} {target_class} : {attribute_name}\n'
    mermaid_data += arrow_relationships

mermaid_data += "```\n"

# Append Mermaid formatted data to README.md
readme_path = 'README.md'
with open(readme_path, 'a') as readme_file:
    readme_file.write('\n## Generated Mermaid Diagram\n')
    readme_file.write(mermaid_data)
