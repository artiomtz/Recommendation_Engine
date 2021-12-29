
def remap_ids(preferences, mapping, map_unmap):

    if map_unmap:
        preferences_new_ids = {}
        mapping_new = {}

        for i, user in enumerate(preferences):
            mapping_new[i+1] = user
            preferences_new_ids[i+1] = preferences[user]

        print(f"Remapping: {mapping_new}")
        print(f"New IDs: {preferences_new_ids}")
        return preferences_new_ids, mapping_new

    else:
        matches_new_ids = []

        for i in preferences:
            matches_new_ids.append([mapping[i[0]], mapping[i[1]]])

        print(f"---------- FINAL MATCH RESULTS ----------\n{matches_new_ids}")
        return matches_new_ids


if __name__ == "__main__":
    user_pref = {0: [4, 3, 4, 3], 1: [3, 0, 5, 4], 7: [2, 2, 2, 2], 9: [5, 2, 4, 4], 15: [2, 2, 4, 2], 16: [1, 2, 1, 2]}
    set_mapping = {1: 0, 2: 1, 3: 7, 4: 9, 5: 15, 6: 16}
    match_results = [[1, 4], [3, 6], [5, 2]]

    print('Attempting to reassign incremental IDs...')
    remap_ids(user_pref, {}, True)

    print('Attempting to reassign original IDs...')
    remap_ids(match_results, set_mapping, False)
