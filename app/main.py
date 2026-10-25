import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv" or parts[1] == parts[2]:
        return

    _, source, destination = parts

    try:
        with open(source, "r", encoding="utf-8") as src:
            content = src.read()
    except FileNotFoundError:
        return

    if "/" in destination:
        path_elements = destination.split("/")

        if destination.endswith("/"):
            directories = [dir_name for dir_name in path_elements if dir_name]
            destination_file = "/".join(directories) + "/" + source
        else:
            directories = path_elements[:-1]
            destination_file = destination

        current_path = ""
        for directory in directories:
            current_path = current_path + directory + "/"
            try:
                os.mkdir(current_path)
            except FileExistsError:
                pass
    else:
        destination_file = destination

    with open(destination_file, "w", encoding="utf-8") as dst:
        dst.write(content)

    os.remove(source)