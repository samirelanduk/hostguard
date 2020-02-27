def get_host_lines(location):
    with open(location) as f:
        return f.read().splitlines()


def save_host_lines(location, lines):
    with open(location, "w") as f:
        f.write("\n".join(lines))
    