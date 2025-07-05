import matplotlib.pyplot as plt
import json
import os

def visualize_subnets(input_file='subnet_report.json', output_image='network_plot.png'):
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    try:
        with open(input_file) as f:
            data = json.load(f)
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        return

    sorted_data = sorted(data.items(), key=lambda item: item[1]['usable_hosts'], reverse=True)

    subnets = [item[0] for item in sorted_data]
    hosts = [item[1]['usable_hosts'] for item in sorted_data]

    if not subnets:
        print("No data to plot.")
        return

    plt.figure(figsize=(12, max(6, len(subnets) * 0.4))) 
    bars = plt.barh(subnets, hosts, color='skyblue')

    plt.xlabel('Number of Usable Hosts')
    plt.ylabel('Subnet (CIDR)')
    plt.title('Usable Hosts per Subnet')

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height() / 2,
                 str(width), va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(output_image)
    plt.close()

    print(f"Plot saved to {output_image}")

if __name__ == "__main__":
    visualize_subnets()
