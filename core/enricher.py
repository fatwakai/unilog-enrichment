import json
from enrichers import opencanary, cowrie, suricata

def load_rules(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def enrich_log(log_data, source, rules):
    if source == "opencanary":
        return opencanary.enrich_opencanary_log(log_data, rules)
    elif source == "cowrie":
        return cowrie.enrich_cowrie_log(log_data, rules)
    elif source == "suricata":
        return suricata.enrich_suricata_log(log_data, rules)
    else:
        log_data["attack_type"] = "Unknown Source"
        return log_data