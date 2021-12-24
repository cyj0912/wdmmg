# Smarter split to handle quoted strings that contain comma
def smarter_split(line, ch):
    splits = []
    state = 0
    prev_i = 0
    for i in range(len(line)):
        if state == 0 and line[i] == ch:
            splits.append(line[prev_i:i])
            prev_i = i + 1
        elif state == 0 and line[i] == '"':
            state = 1
        elif state == 1 and line[i] == '"':
            state = 0
    if prev_i < len(line):
        splits.append(line[prev_i:])
    return splits


def clean(a):
    a = a.strip()
    a = a.strip('"')
    a = a.strip()
    return a


def split(line: str, split_char: str) -> list[str]:
    return [clean(a) for a in smarter_split(line, split_char)]


def csv_to_dict(file_path: str, split_char: str = ",") -> list[dict[str, str]]:
    # First line is attributes
    # Separator is ,
    result = []
    with open(file_path) as f:
        lines = f.read().splitlines()
        attrs = split(lines[0], split_char)
        contents = lines[1:]
        for content in contents:
            content = split(content, split_char)
            data = {attrs[i]: content[i] for i in range(len(content))}
            result.append(data)
    return result
