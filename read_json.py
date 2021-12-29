import json


def read_json(json_data, max_rank):
    json_data_filtered = {}
    preferences = {}
    num_interests = json_data['num_interests']

    for user_id in json_data:
        if str(user_id).isnumeric():
            json_data_filtered[user_id] = json_data[user_id]

    for user_id, user_interests in sorted(json_data_filtered.items(), key=lambda item: int(item[0])):
        interest_ids = []

        if len(user_interests) < num_interests:
            continue

        for interest in user_interests:
            interest_ids.append(int(str(interest).split("'")[1]))

        sorted_interest_ids = sorted(interest_ids)
        preferences[int(user_id)] = []

        for interest_id in sorted_interest_ids:
            for i, interest in enumerate(user_interests):
                interest_id_loop = int(str(interest).split("'")[1])
                if interest_id_loop == interest_id:
                    interest_value = str(interest)[-2:-1]
                    if interest_value.isnumeric() and 0 < int(interest_value) <= max_rank:
                        preferences[int(user_id)].append(int(interest_value))
                    else:
                        preferences[int(user_id)].append(1)
                    break

    num_users = len(preferences)
    print(f"Interests: {num_interests}")
    print(f"Users: {num_users}")
    print(preferences)
    return preferences, num_interests, num_users


if __name__ == "__main__":
    rank_range = 5

    with open('input_test_data/input_test_data_1.json') as json_file:
        json_dict = json.load(json_file)

    print('Attempting to read the JSON file...')
    read_json(json_dict, rank_range)
