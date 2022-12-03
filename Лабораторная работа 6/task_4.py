import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        list_ = []
        is_header = True
        for row in f:
            list_rows = row.rstrip().split(new_line)
            for line in list_rows:
                if is_header:
                    headers = line.split(delimiter)
                    is_header = False
                    continue
                list_.append(dict(zip(headers, line.split(delimiter))))
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
