from read_csv import read_csv
from compatibility import calculate_compatibility
from matching import solve_ip


if __name__ == "__main__":
    rank_range = 5
    threshold_compatibility = 0.2
    csv_file_name = 'Sample_Data'
    csv_rating_columns = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

    print('\n\nAttempting to read the CSV file...')
    user_preferences = read_csv(csv_file_name, csv_rating_columns)

    print('\n\nAttempting to calculate compatibility scores...')
    num_users, num_interests, user_compatibility_scores = calculate_compatibility(user_preferences)

    score_max = pow(rank_range, 2) * num_interests
    print('\n\nAttempting to solve the integer programming problem...')
    matches = solve_ip(num_users, user_compatibility_scores, threshold_compatibility, score_max)
    # print(matches)
