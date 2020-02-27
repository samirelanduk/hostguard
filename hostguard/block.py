#! /usr/bin/env python3

import os
import sys
from hosts import get_host_lines, save_host_lines

HOST_LOCATION = "/etc/hosts"

if len(sys.argv) < 2:
    print("What hostname should be blocked?")
    sys.exit()
domain_to_block = sys.argv[1]

host_contents = get_host_lines(HOST_LOCATION)

new_line = "0.0.0.0 " + domain_to_block
if new_line not in host_contents:
    host_contents.append(new_line)

save_host_lines(HOST_LOCATION, host_contents)

print("Blocked %s" % domain_to_block)
