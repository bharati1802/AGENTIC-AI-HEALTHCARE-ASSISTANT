import json

def check_claim_status(name):

    data = {
        "rahul": "Approved",
        "amit": "Pending",
        "sneha": "Rejected"
    }

    name = name.lower().strip()
    status = data.get(name, "Not Found")

    result = f"📄 Claim status for {name.title()}: {status}"

    # ✅ Save to JSON file
    save_to_json(name, status)

    return result


def save_to_json(name, status):

    record = {
        "name": name,
        "status": status
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(record)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)