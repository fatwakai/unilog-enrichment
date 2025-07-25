def enrich_opencanary_log(log_data, rules):
    logtype = log_data.get("logtype", "").lower()
    rule = rules.get(logtype, {})

    log_data["attack_type"] = rule.get("attack_type", "Unknown")
    log_data["risk_level"] = rule.get("risk_level", "unknown")
    log_data["source"] = "opencanary"

    return log_data
