import pandas as pd
import ipaddress
import json
import os

def analyze_subnets(input_file='ip_data.xlsx', output_json='subnet_report.json', output_csv='results.csv'):
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    try:
        df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Failed to read Excel file: {e}")
        return

    expected_columns = {'IP Address', 'Subnet Mask'}
    if not expected_columns.issubset(df.columns):
        print(f"Excel file must contain columns: {expected_columns}")
        return

    results = []
    subnet_info = {}

    for index, row in df.iterrows():
        ip = str(row['IP Address']).strip()
        mask = str(row['Subnet Mask']).strip()

        try:
            interface = ipaddress.IPv4Interface(f"{ip}/{mask}")
            network = interface.network

            cidr = network.prefixlen
            net_addr = network.network_address
            broadcast = network.broadcast_address
            usable_hosts = network.num_addresses - 2 if network.num_addresses > 2 else network.num_addresses

            result = {
                'IP': ip,
                'Subnet Mask': mask,
                'CIDR': cidr,
                'Network Address': str(net_addr),
                'Broadcast Address': str(broadcast),
                'Usable Hosts': usable_hosts
            }
            results.append(result)

            subnet_key = f"{net_addr}/{cidr}"
            if subnet_key not in subnet_info:
                subnet_info[subnet_key] = {
                    'network': str(net_addr),
                    'cidr': cidr,
                    'total_hosts': network.num_addresses,
                    'usable_hosts': 0,
                    'member_ips': []
                }

            subnet_info[subnet_key]['usable_hosts'] += usable_hosts
            subnet_info[subnet_key]['member_ips'].append(ip)

        except Exception as e:
            print(f"Skipping invalid entry (Row {index + 2}): {ip}/{mask} → {e}")
            continue

    sorted_results = sorted(results, key=lambda x: (x['Network Address'], x['IP']))
    pd.DataFrame(sorted_results).to_csv(output_csv, index=False)
    print(f"CSV report saved: {output_csv}")

    sorted_subnets = dict(sorted(subnet_info.items(), key=lambda item: item[1]['usable_hosts'], reverse=True))
    with open(output_json, 'w') as f:
        json.dump(sorted_subnets, f, indent=2)
    print(f"JSON report saved: {output_json}")

    return sorted_subnets

if __name__ == "__main__":
    analyze_subnets()
