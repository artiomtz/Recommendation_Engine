from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpBinary


def solve_ip(num_users, compatibility_scores, compatibility_threshold, max_score):
    # create the LP model
    model = LpProblem(name="Pair_Matching", sense=LpMaximize)

    # Initialize the decision variables
    x_i = list(range(1, num_users + 1))
    x_j = list(range(1, num_users + 1))
    x_ij = LpVariable.dicts("Xij", [(i, j) for i in x_i for j in x_j], 0, 1, LpBinary)

    # Add the constraints to the model
    for i in x_i:
        model += (x_ij[(i, i)] == 0, f"one_is_not_matched_with_oneself_i{i}")
        model += (lpSum(x_ij[(i, j)] + x_ij[(j, i)] for j in x_j) <= 1, f"one_match_per_user_i{i}")
        for j in x_j:
            if j > i:
                model += (x_ij[(i, j)] * (compatibility_scores[(i, j)] / max_score - compatibility_threshold) >= 0,
                          f"compatibility_threshold_i{i}_j{j}")

                model += (x_ij[(i, j)] +
                          lpSum(x_ij[(i, k)] for k in range(i+1, len(x_i)+1)
                                if compatibility_scores[(i, j)] > compatibility_scores[(i, k)])
                          + lpSum(x_ij[(k, j)] for k in range(1, j)
                                  if compatibility_scores[(i, j)] > compatibility_scores[(k, j)]) <= 1,
                          f"best_compatibility_i{i}_j{j}")
            if j < i:
                model += (x_ij[(i, j)] * (compatibility_scores[(j, i)] / max_score - compatibility_threshold) >= 0,
                          f"compatibility_threshold_i{i}_j{j}")

                model += (x_ij[(i, j)] +
                          lpSum(x_ij[(i, k)] for k in range(1, i)
                                if compatibility_scores[(j, i)] > compatibility_scores[(k, i)])
                          + lpSum(x_ij[(k, j)] for k in range(j + 1, len(x_j)+1)
                                  if compatibility_scores[(j, i)] > compatibility_scores[(j, k)]) <= 1,
                          f"best_compatibility_i{i}_j{j}")

    # Add the objective function to the model
    obj_func = lpSum(x_ij[(i, j)] for i in x_i for j in x_j)
    model += obj_func

    # Solve the problem
    model.solve()

    # Print the results
    print("---------- MODEL ----------")
    print(model)
    print("---------- RESULTS ----------")
    print(f"Status: {model.status}, {LpStatus[model.status]}")
    print(f"Objective: {model.objective.value()}")

    matches = []
    for var in model.variables():
        print(f"{var.name}: {var.value()}")
        if var.value():
            user1 = int("".join(x for x in var.name.split(",")[0] if x.isdigit()))
            user2 = int("".join(x for x in var.name.split(",")[1] if x.isdigit()))
            matches.append([user1, user2])

    print("\n---------- MATCHES ----------")
    print(matches)
    return matches


if __name__ == "__main__":
    num_of_users = 6
    num_of_interests = 4
    rank_range = 5
    score_max = pow(rank_range, 2)*num_of_interests
    threshold_compatibility = 0.3
    user_compatibility_scores = {(1, 2): 56, (1, 3): 22, (1, 4): 74, (1, 5): 92, (1, 6): 32,
                                 (2, 3): 47, (2, 4): 17, (2, 5): 68, (2, 6): 42, (3, 4): 9,
                                 (3, 5): 13, (3, 6): 83, (4, 5): 45, (4, 6): 71, (5, 6): 28}

    print("Attempting to solve the integer programming problem...")
    solve_ip(num_of_users, user_compatibility_scores, threshold_compatibility, score_max)
