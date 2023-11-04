# zCIDR
1. **Command-Line Interface:** The script employs the `argparse` module to accept command-line arguments, allowing users to input a CIDR range directly when executing the script.
2. **CIDR Parsing:** Upon receiving a CIDR range as input, the script validates and parses it to extract all individual IP addresses present within the specified range.
3. **IP Address Output:** The script outputs a list of IP addresses present in the CIDR range, enabling users to easily access the individual IPs without additional formatting or numbering.

**Usage:**

Users can run the script from a terminal or command prompt by providing the CIDR range as a command-line argument. For instance:

```
python zcidr.py -cidr 192.168.1.0/24
```
