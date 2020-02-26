#! /usr/bin/env python3

import os
import sys

if len(sys.argv) < 2:
    print("What hostname should be blocked?")
    sys.exit()

domain_to_block = sys.argv[1]

HOST_LOCATION = "/etc/hosts"

with open(HOST_LOCATION) as f:
    host_contents = f.read().splitlines()

new_line = "0.0.0.0 " + domain_to_block

if new_line not in host_contents:
    host_contents.append(new_line)

with open(HOST_LOCATION, "w") as f:
    f.write("\n".join(host_contents))

print("Blocked %s" % domain_to_block)
