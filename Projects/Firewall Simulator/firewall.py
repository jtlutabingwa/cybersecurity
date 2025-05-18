import random   # Helps generate random IP Addresses

def generate_random_ip():   # Generates the random IP address
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):    # Checks if the IP addresses matches any of the rules and returns the action
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"

def main(): # Gives a list of IP Addresses to block
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    for _ in range(12):     # Generates 12 random IP Addresses to compare with the firewall rules to simulate network traffic
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":  # Ensures main function runs once script is executed
    main()
