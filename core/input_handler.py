import json

def get_logs(input_type, config):
    if input_type == "file":
        return read_from_file(config["input"]["file_path"])
    else:
        raise NotImplementedError("Input type not supported yet")

def read_from_file(path):
    with open(path, 'r') as f:
        return [json.loads(line.strip()) for line in f if line.strip()]
