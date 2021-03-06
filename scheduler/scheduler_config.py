# scheduler_config.py
# File that stores configurations for generating the schedule. Imported into scheduler.py.
# This will be generated based on configurations made in the UI. Some of these are just examples for now.

num_employees = 8
num_weeks = 2
shifts = ['O', 'M', 'A', 'N']

# Shift constraints on continuous sequence :
#     (shift, hard_min, soft_min, min_penalty,
#             soft_max, hard_max, max_penalty)
shift_constraints = [
    # One or two consecutive days of rest, this is a hard constraint.
    (0, 1, 1, 0, 2, 2, 0),
    # betweem 2 and 3 consecutive days of night shifts, 1 and 4 are
    # possible but penalized.
    (3, 1, 2, 20, 3, 4, 5),
]

# Weekly sum constraints on shifts days:
#     (shift, hard_min, soft_min, min_penalty,
#             soft_max, hard_max, max_penalty)
weekly_sum_constraints = [
    # Constraints on rests per week. At least 1 rest per week. At most 3 rests per week.
    (0, 1, 2, 7, 2, 3, 4),
    # # At least 1 night shift per week (penalized). At most 4 (hard).
    # (3, 0, 1, 3, 4, 4, 0),
]

# Penalized transitions:
#     (previous_shift, next_shift, penalty (0 means forbidden))
penalized_transitions = [
    # Morning to night is forbidden.
    (1, 3, 0),
    # Morning to afternoon is forbidden.
    (1, 2, 0),
    # Afternoon to night is forbidden.
    (2, 3, 0),
    # Night to morning is forbidden.
    (3, 1, 0),
]

# Daily demands for work shifts (morning, afternon, night) for each day
#   of the week starting on Monday.
weekly_cover_demands = [
    (1, 1, 1),  # Monday
    (1, 1, 1),  # Tuesday
    (1, 1, 1),  # Wednesday
    (1, 1, 1),  # Thursday
    (1, 1, 1),  # Friday
    (1, 1, 1),  # Saturday
    (1, 1, 1),  # Sunday
]

# Penalty for exceeding the cover constraint per shift type.
excess_cover_penalties = (2, 2, 5)