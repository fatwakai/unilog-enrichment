import json
from core import enricher, input_handler, output_handler
import yaml


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def main():
    config = load_config()
    source = config["source"]
    rule_path = config["rule_file"]
    input_type = config["input_type"]
    output_type = config["output_type"]

    rules = enricher.load_rules(rule_path)
    logs = input_handler.get_logs(input_type, config)

    for log in logs:
        enriched = enricher.enrich_log(log, source, rules)
        output_handler.send_log(output_type, enriched, config)


if __name__ == "__main__":
    main()
