def enrich_cowrie_log(log_data, rules):
    eventid = log_data.get("eventid", "").lower()
    rule = rules.get(eventid, {})

    log_data["attack_type"] = rule.get("attack_type", "Unknown")
    log_data["risk_level"] = rule.get("risk_level", "unknown")
    log_data["source"] = "cowrie"

    return log_data
