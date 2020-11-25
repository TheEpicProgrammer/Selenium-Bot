import json


def get(file, sub=None):
    with open(f"data/{file}.json") as f:
        return json.load(f)[sub] if sub else json.load(f)


def dump(file, data):
    with open(f"data/{file}.json", "w") as f:
        json.dump(data, f, indent=4)


def rules_backup(rules, id):
    with open(f"data/backups/{id}.json", "w+") as f:
        json.dump({i: rules[i] for i in rules if i != "ids"}, f, indent=4)