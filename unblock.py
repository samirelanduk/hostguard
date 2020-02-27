#! /usr/bin/env python3

import os
import sys
from hosts import get_host_lines, save_host_lines

HOST_LOCATION = "/etc/hosts"

if len(sys.argv) < 2:
    print("What hostname should be unblocked?")
    sys.exit()
domain_to_unblock = sys.argv[1]

host_contents = get_host_lines(HOST_LOCATION)

host_contents = [line for line in host_contents\
    if domain_to_unblock not in line.split()[1]]

save_host_lines(HOST_LOCATION, host_contents)

print("Unblocked %s" % domain_to_unblock)

