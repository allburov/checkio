#!/home/aburov/venvs/checkio-venv/bin/checkio --domain=py run ip-network-route-summarization

# .task-description td{	align:         center;	border-bottom: 1px solid #000000;	border-top:    1px solid #000000;}.task-description .blank{	border-width: 0px}.task-description .left{	align:        center;	border-left: 1px solid #000000;	padding-left: 10px;	padding-right: 10px;	}.task-description .right{	align:        center;	padding-left: 10px;	padding-right: 10px;	border-left: 1px solid #000000;	border-right: 1px solid #000000;}.task-description table {       margin-left: 15%;	}#animation-results-block .task-description table {       margin-left: 0;	}#animation-results-block .task-description .left {	padding-left: 0px;	padding-right: 0px;	}An IP network is a set of routers that communicate routing information using a protocol.	A router is uniquely identified by an IP address.
# In IPv4, an IP address consists of 32 bits, canonically represented as 4 decimal numbers of 8 bits each. The decimal numbers range from 0 (00000000) to 255 (11111111).
# Each router has a "routing table" that contains a list of IP addresses, for the router to know where to send IP packets.
# 
# 
# 
# 
# Route summarization in IP networksAs the network grows large (hundreds of routers), the number of IP addresses in the routing table increases rapidly.	Maintaining a high number of IP addresses in the routing table would result in a loss of performances (memory, bandwidth and CPU resources limitation).
# Route summarization, also called route aggregation, consists in reducing the number of routes by aggregating them into a "summary route".
# 
# Let's consider the following example:
# 
# 
# We have 4 routers connected toA.Ais aware about all 4 IP addresses, because it has a direct interface to each of them. However,Awill not send them all toB.
# Instead, it will aggregate the addresses into a summary route, and send this new route toB.
# This implies that:
# 
# - Less bandwidth is used on the link betweenAandB.-Bsaves memory: it has only one route to store in its routing table-Bsaves CPU resources: there are less entries to consider when handling incoming IP packets
# 
# Computing a summary routeAhas all 4 addresses stored in its routing table.
# 
# Address 1172.16.12.0Address 2172.16.13.0Address 3172.16.14.0Address 4172.16.15.0
# 
# Awill convert these IP addresses to binary format, align them and find the boundary line between the common prefix on the left (highlighted in red), and the remaining bits on the right.
# 
# Address 110101100000100000000110000000000Address 210101100000100000000110100000000Address 310101100000100000000111000000000Address 410101100000100000000111100000000
# 
# Acreates a new IP address made of the common bits, and all other bits set to "0".
# This new IP address is converted back to decimal numbers.
# Finally,Acomputes the number of common bits, also called "subnet".
# The summary route is this new IP address, followed by a slash and the subnet: 172.16.12.0/22
# 
# Input:A list of strings containing the IP addresses
# 
# Output:A string containing the summary route, represented as an IP address, followed by a slash and the subnet.
# 
# Preconditions:
# all(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",d) for d in data))
# all(-1<int(n)<256 for n in d.split(".") for d in data)
# len(data) == len(set(data)) and len(data) > 1
# 
# 
# 
# END_DESC
import ipaddress


def commonprefix(m):
    """
    Given a list of pathnames, returns the longest common leading component
    Idea from os.path.commonprefix


    """
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1


def checkio(hosts):
    # Convert addresses to binary repr
    hosts_binary = map(bin, map(int, map(ipaddress.IPv4Address, hosts)))
    # Get binary prefix
    common_prefix = commonprefix([str(x) for x in hosts_binary])
    big_network_size = len(common_prefix) - 2  # -0b prefix in binary representation

    network = ipaddress.IPv4Network(hosts[0]).supernet(new_prefix=big_network_size)
    return str(network)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"
    print('Done!')
