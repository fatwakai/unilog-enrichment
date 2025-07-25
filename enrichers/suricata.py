def enrich_suricata_log(log_data, rules):
    alert = log_data.get("alert", {}).get("signature", "").lower()
    rule = rules.get(alert, {})

    log_data["attack_type"] = rule.get("attack_type", "Unknown")
    log_data["risk_level"] = rule.get("risk_level", "unknown")
    log_data["source"] = "suricata"

    return log_data
