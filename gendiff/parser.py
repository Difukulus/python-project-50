import json
import yaml

def parse_file(filepath):
    extension = filepath.split('.')[-1]
    with open(filepath, 'r') as file:
        if extension in ('yml', 'yaml'):
            return yaml.safe_load(file)
        elif extension == 'json':
            return json.load(file)
        else:
            raise ValueError(f"Unsupported file format: {extension}")
    
