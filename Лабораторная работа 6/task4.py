import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as f:
        list_of_dict = []
        lines = f.read().split("\n")
        for i in range(1, len(lines)-1):
            dict_ = {lines[0].split(",")[j]: lines[i].split(",")[j] for j in range(len(lines[i].split(",")))}
            list_of_dict.append(dict_)
        return list_of_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
