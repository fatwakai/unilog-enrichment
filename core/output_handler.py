import json
import requests

def send_log(output_type, log_data, config):
    if output_type == "console":
        print(json.dumps(log_data, indent=2))
    elif output_type == "elasticsearch":
        url = config["output"]["elastic_url"] + "/" + config["output"]["index_name"] + "/_doc"
        requests.post(url, json=log_data)
    else:
        raise NotImplementedError("Output type not supported yet")
