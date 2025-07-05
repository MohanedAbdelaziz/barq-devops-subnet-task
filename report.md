# Network Analysis Report

## 1. Which subnet has the most hosts?
The subnets with the most hosts are:
- `10.15.4.0/22` (1022 usable hosts)
- `10.2.0.0/22` (1022 usable hosts)
- `10.20.4.0/22` (1022 usable hosts)
- `10.3.0.0/22` (1022 usable hosts)
- `172.16.48.0/22` (1022 usable hosts)
- `172.16.60.0/22` (1022 usable hosts)
- `192.168.100.0/22` (1022 usable hosts)
- `192.168.20.0/22` (1022 usable hosts)

These /22 subnets all have the largest address space with 1022 usable hosts each.

## 2. Are there any overlapping subnets? If yes, which ones?
After analyzing the network ranges, I found the following potential overlaps:

1. **10.0.0.0/23** (10.0.0.0-10.0.1.255) and **10.0.3.0/24** (10.0.3.0-10.0.3.255)  
   - These don't overlap but are close neighbors in the 10.0.0.0 network

2. **172.16.0.0/23** (172.16.0.0-172.16.1.255) and **172.16.8.0/23** (172.16.8.0-172.16.9.255)  
   - These are properly separated with no overlap

3. **172.16.14.0/23** (172.16.14.0-172.16.15.255) and **172.16.15.0/24** (nonexistent in data)  
   - No actual overlap found in current data

No actual overlapping subnets were found in the provided data. All subnets are properly segmented.

## 3. What is the smallest and largest subnet in terms of address space?
- **Smallest subnet**: The /24 subnets (255.255.255.0) with 254 usable hosts:
  - 10.0.3.0/24
  - 10.4.3.0/24
  - 10.50.2.0/24
  - 172.16.20.0/24
  - 172.16.40.0/24
  - 192.168.1.0/24
  - 192.168.2.0/24
  - 192.168.3.0/24
  - 192.168.4.0/24
  - 192.168.10.0/24

- **Largest subnet**: The /22 subnets (255.255.252.0) with 1022 usable hosts (listed in question 1)


## 4. Suggested Subnetting Strategy to Reduce Wasted IPs

To reduce IP waste, I suggest the following simple steps:

1. **Use VLSM (Variable Length Subnet Masking)**

   * Instead of giving every network a fixed size like /22 or /24, use subnet sizes based on how many hosts are actually needed.

2. **Merge small networks when possible**

   * If there are many small networks doing the same job or in the same place (like 192.168.1.0/24, 192.168.2.0/24), we can combine them into a bigger subnet (like 192.168.0.0/22).

3. **Group IPs by location or function**

   * For better organization and easier management:

     * Use 10.0.0.0/16 for Site A
     * Use 10.1.0.0/16 for Site B
     * Use 172.16.0.0/16 for servers or infrastructure
     * Use 192.168.0.0/16 for user devices

4. **Give each subnet just what it needs**

   * If a /22 subnet (1022 hosts) is too big, we can make it smaller like /23 or /24 to save IPs.

5. **Leave space for future growth**

   * Try to keep some IP blocks available between subnets, so we can expand later without changing existing networks.

6. **Track everything with proper documentation**

   * Use an IP Address Management (IPAM) tool to keep records of how IPs are used and make better decisions later.g