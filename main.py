from read_csv import read_csv
from read_json import read_json
from remap_ids import remap_ids
from compatibility import calculate_compatibility
from matching import solve_ip
import json


if __name__ == "__main__":
    rank_range = 5
    threshold_compatibility = 0.2

    # csv_file_name = "input_test_data/sample_data"
    # csv_rating_columns = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
    #
    # print("\n\nAttempting to read the CSV file...")
    # user_preferences, num_interests, num_users = read_csv(csv_file_name, csv_rating_columns)

    with open("input_test_data/input_test_data_1.json") as json_file:
        json_dict = json.load(json_file)

    print("\n\nAttempting to read the JSON file...")
    user_preferences, num_interests, num_users = read_json(json_dict, rank_range)
    print(f"Interests: {num_interests}")
    print(f"Users: {num_users}")
    print(user_preferences)

    print("\n\nAttempting to reassign incremental IDs...")
    user_preferences, mapping = remap_ids(user_preferences, {}, True)
    print(f"Remapping: {mapping}")
    print(f"New IDs: {user_preferences}")

    print("\n\nAttempting to calculate compatibility scores...")
    user_compatibility_scores, num_users = calculate_compatibility(user_preferences, num_interests, num_users)
    print(f"Users: {num_users}")
    print(user_compatibility_scores)

    score_max = pow(rank_range, 2) * num_interests
    print("\n\nAttempting to solve the integer programming problem...")
    matches = solve_ip(num_users, user_compatibility_scores, threshold_compatibility, score_max)

    print("\n\nAttempting to reassign original IDs...")
    final_results = remap_ids(matches, mapping, False)
    
    print("\n\n---------- FINAL MATCH RESULTS ----------")
    print(final_results)
