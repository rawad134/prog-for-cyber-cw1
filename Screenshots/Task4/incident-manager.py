"""Security incident manager using a dictionary."""

# 1. Create the incident dictionary
incident = {
    "username": "jsmith",
    "ip_address": "10.0.0.45",
    "event_type": "Failed login",
    "risk_level": "Low",
}

# 2. Display username and IP address
print("Username:", incident["username"])
print("IP Address:", incident["ip_address"])

# 3. Add a new field called status
incident["status"] = "Open"

# 4. Update the risk level
incident["risk_level"] = "High"

# 5. Remove one field (pop with a default avoids KeyError)
removed_value = incident.pop("event_type", None)
print("\nRemoved field 'event_type' with value:", removed_value)

# 6. Display all remaining keys and values
print("\nRemaining incident details:")
for key, value in incident.items():
    print(f"{key}: {value}")

# 7. Display the total number of key-value pairs
print("\nTotal key-value pairs:", len(incident))
