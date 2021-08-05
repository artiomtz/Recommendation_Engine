
def calculate_compatibility(preferences):
    num_interests = len(preferences[1])
    compatibilities = {}

    for user in preferences:
        for next_user in range(user + 1, len(preferences) + 1):
            score = 0
            for rating in range(num_interests):
                score += preferences[user][rating]*preferences[next_user][rating]
            compatibilities[(user, next_user)] = score

    print(compatibilities)
    return compatibilities


if __name__ == "__main__":
    user_preferences = {1: [4, 3, 4, 3], 2: [3, 0, 5, 4], 3: [2, 2, 2, 2], 4: [5, 2, 4, 4], 5: [2, 2, 4, 2]}

    print('Attempting to calculate compatibility scores...')
    calculate_compatibility(user_preferences)
