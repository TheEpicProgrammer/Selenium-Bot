import json


def rules_get():
    with open("data/rules.json") as f:
        return json.load(f)


def rules_dump(new):
    with open("data/rules.json", "w") as f:
        json.dump(new, f, indent=4)


def rules_backup(rules, id):
    rules.pop("ids")
    with open(f"data/files/backups/{id}.json", "w+") as f:
        json.dump(rules, f, indent=4)