def get_entry_from_envy(entry_name):
    with open(".env", "r") as env_file:
        for line in env_file.readlines():
            if line.lower().startswith(entry_name):
                return line[len(entry_name) + 1:]