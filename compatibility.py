def calculate_compatibility(preferences):
    num_users = len(preferences)
    num_interests = len(preferences[1])
    compatibilities = {}

    if num_users % 2 == 1:
        num_users -= 1

    for user in range(1, num_users):
        for next_user in range(user + 1, num_users + 1):
            score = 0
            for rating in range(num_interests):
                score += preferences[user][rating]*preferences[next_user][rating]
            compatibilities[(user, next_user)] = score

    print(compatibilities)
    return num_users, num_interests, compatibilities


if __name__ == "__main__":
    user_preferences = {1: [4, 3, 4, 3], 2: [3, 0, 5, 4], 3: [2, 2, 2, 2], 4: [5, 2, 4, 4], 5: [2, 2, 4, 2]}

    print('Attempting to calculate compatibility scores...')
    calculate_compatibility(user_preferences)