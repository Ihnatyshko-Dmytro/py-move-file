import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv" or parts[1] == parts[2]:
        return

    source, destination = parts[1], parts[2]

    if not os.path.exists(source):
        return

    if destination.endswith("/"):
        destination_dir = destination
        destination_file = os.path.join(destination, os.path.basename(source))
    else:
        destination_dir = os.path.dirname(destination)
        destination_file = destination

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r", encoding="utf-8") as src, open(
        destination_file, "w", encoding="utf-8"
    ) as dst:
        dst.write(src.read())
    os.remove(source)
