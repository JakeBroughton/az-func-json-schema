import json
import os
import copy

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def merge_settings(base, specific):
    merged = copy.deepcopy(base)
    merged["properties"]["Values"]["properties"].update(
        specific["properties"]["Values"]["properties"]
    )
    merged["properties"]["Host"]["properties"].update(
        specific["properties"]["Host"]["properties"]
    )
    return merged

# Load base settings
base_settings_path = os.path.join(os.getcwd(), 'local.settings.json')
base_settings = load_json(base_settings_path)

# List of folders to process
folders = ['node', 'python']

for folder in folders:
    specific_settings_path = os.path.join(os.getcwd(), folder, 'local.settings.dev.json')
    if os.path.exists(specific_settings_path):
        specific_settings = load_json(specific_settings_path)
        # Merge settings starting with a deep copy of base settings
        merged_settings = merge_settings(base_settings, specific_settings)
        
        # Write merged settings to a new file
        output_path = os.path.join(os.getcwd(), folder, 'local.settings.json')
        with open(output_path, 'w') as file:
            json.dump(merged_settings, file, indent=2)
        
        print(f"Merged settings written to {output_path}")
    else:
        print(f"No specific settings found for {folder}")