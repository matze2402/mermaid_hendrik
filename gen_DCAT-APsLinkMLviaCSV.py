import os
import csv
import yaml
from collections import OrderedDict
import ruamel.yaml


def read_yaml_file(yaml_file):
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data

# # Example usage
# yaml_file = "example.yaml"
# data = read_yaml_file(yaml_file)
# print(data)


def convert_csv_to_yaml(folder_path, yaml_prefix_file, yaml_additional_classes_file, yaml_output_file ):
    data = {}
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # Check if the file is a CSV file
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    class_uri = filename.replace('.csv','').replace(' ','_')
                    if class_uri not in data:
                        data[class_uri] = {'class_uri': class_uri, 'attributes': {}}
                    attribute = row['attribute']
                    range_str = row['target_curie'].replace(':', '_')
                    data[class_uri]['attributes'][f"dct_{attribute}"] = {
                        'slot_uri': row['curie'],
                        'range': range_str ,
                        'required': row['cardinallity'] == 'mandatory',
                        'multivalued': row['multivalued'].lower() == 'true'
                    }
    # Write the aggregated data to the YAML file
    # return data
    prefix_data = read_yaml_file(yaml_prefix_file)
    additional_classes_data = read_yaml_file(yaml_additional_classes_file)
    data_3 = {**data, **additional_classes_data}
    prefix_data.update({'classes': data_3})
    order = ['id', 'name', 'prefixes', 'imports', 'default_range', 'classes']
    ordered_dict = OrderedDict((key, prefix_data[key]) for key in order if key in prefix_data)
    yaml = ruamel.yaml.YAML()
    with open(yaml_output_file, 'w+') as file:
        yaml.dump(dict(ordered_dict), file)


# Usage

convert_csv_to_yaml('CSV_Files/',
                    'Prefixes_for_DCAT_LinkML_template.yaml',
                    'external_resources_for_DCAT_in_LinkML.yaml',
                    'DCAT_AP_via_CSV.yaml')

