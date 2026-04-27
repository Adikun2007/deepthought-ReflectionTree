import json

# load json file
with open("reflection-tree.json") as f:
    data = json.load(f)

nodes_list = data["nodes"]

# make id - node mapping
nodes = {}
for n in nodes_list:
    nodes[n["id"]] = n

answers = {}

# tracking signals
signals = {
    "axis1": {"internal": 0, "external": 0},
    "axis2": {"contribution": 0, "entitlement": 0, "neutral": 0},
    "axis3": {"self": 0, "team": 0, "others": 0}
}

# function to find next node
def get_next(curr_id):
    for n in nodes.values():
        if "parentId" in n and n["parentId"] == curr_id:
            return n
    return None

# function to get highest value
def get_dominant(axis):
    return max(signals[axis], key=signals[axis].get)

current = nodes["START"]

while True:
    node_type = current["type"]

    # print text if exists
    if "text" in current:
        print("\n" + current["text"])

    # end condition
    if node_type == "end":
        break

    # question handling
    elif node_type == "question":
        options = current["options"]

        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")

        choice = int(input("Choose: ")) - 1
        answer = options[choice]

        answers[current["id"]] = answer

        # update signal if exists
        if "signals" in current:
            if answer in current["signals"]:
                axis, value = current["signals"][answer].split(":")
                signals[axis][value] += 1

        current = get_next(current["id"])

    # decision node
    elif node_type == "decision":
        last_answer = list(answers.values())[-1]

        for rule in current["rules"]:
            if last_answer in rule["if"]:
                current = nodes[rule["goto"]]
                break

    # reflection node
    elif node_type == "reflection":
        if "condition" in current:
            axis, value = current["condition"].split("=")

            if get_dominant(axis) != value:
                current = get_next(current["id"])
                continue

        current = get_next(current["id"])

    # summary node
    elif node_type == "summary":
        text = current["text"]

        text = text.replace("{axis1}", get_dominant("axis1"))
        text = text.replace("{axis2}", get_dominant("axis2"))
        text = text.replace("{axis3}", get_dominant("axis3"))

        print("\n" + text)

        current = get_next(current["id"])

    # fallback
    else:
        current = get_next(current["id"])