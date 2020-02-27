#! /usr/bin/env python3

from hosts import get_host_lines

HOST_LOCATION = "/etc/hosts"

host_contents = get_host_lines(HOST_LOCATION)
for line in host_contents:
    print(line.split()[1])