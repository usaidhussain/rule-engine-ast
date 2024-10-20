import json

def load_sample_data(file_path='sample_data.json'):
    """Load sample data from a JSON file."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_data_by_id(data, data_id):
    """Get data entry by ID."""
    for entry in data:
        if entry['id'] == data_id:
            return entry
    return None