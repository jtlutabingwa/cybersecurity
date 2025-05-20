# Firewall Simulator

## Objective
To simulate a basic firewall that processes random incoming IP addresses and checks them against a set of predefined firewall rules to either "block" or "allow" access.

### Skills Learned
Dictionary data structures for rule mapping

Function creation and usage

Conditional logic

Use of random number generation

Basic I/O with print()

Script execution with __name__ == "__main__"


### Tools Used
Python 

random module for IP and number generation

Dictionaries for rule configuration


## Steps
Import Required Module
import random
This module allows for random number generation, which is used to simulate network traffic (random IP addresses and request IDs).

Generate Random IP Address

def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}" 
This function returns a string representing a random IP address from the range 192.168.1.0 to 192.168.1.20.

Check IP Against Firewall Rules

def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"
This function iterates over a dictionary of firewall rules. If the incoming IP matches a blocked IP, it returns "block", otherwise "allow".

Define Main Functionality

def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        ...
    }
    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")
        
A dictionary of blocked IPs is defined.

The loop runs 12 times to simulate 12 incoming network requests.

Each iteration:

Generates a random IP.

Checks the IP against the firewall rules.

Generates a random number (as a placeholder for something like a request ID or payload).

Prints the result showing the IP, whether it is allowed or blocked, and the random number.

Execute Script

if __name__ == "__main__":
    main() 
Ensures that the main() function only runs when the script is executed directly (not when imported as a module).



