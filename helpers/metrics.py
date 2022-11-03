duels = [
    "sliding_tackle",
    "slide_tackle_ratio",
    "Ground defending duel",
    "Ground defending duel_acc_percentage",
    "Ground loose ball duel",
    "Ground loose ball duel_acc_percentage",
    "dangerous_duel_loss_ratio",
    "Air duel",
    "Air duel_acc_percentage",
    "yellow_card",
    "Foul",
    "ip_cluster"
]


game_reading = [
    "anticipated",
    "anticipation",
    "anticipation_percentage",
    "interception",
    "interception_percentage",
    "Clearance",
    "ip_cluster"
]



# --------------------------------------------------------


# POSSESION ATTRIBUTES --------------------------------------------------------


progression = [
    "progressive_passes",
    "progressive_passes_distance",
    "pp_pass_ratio",
    "forward",
    "Acceleration",
    "ip_cluster"
]

established = [
    "switches",
    "backward",
    "horizontal",
    "Head pass",
    "Head pass_acc_percentage",
    "High pass",
    "High pass_acc_percentage",
    "Simple pass",
    "Simple pass_acc_percentage",
    "passing_distance",
    "dangerous_ball_lost",
    "ip_cluster"
]

# --------------------------------------------------------

# ATTACKING ATTRIBUTES ------------------------------

creating = [
    "assist",
    "key_pass",
    "key_pass_ratio",
    "through",
    "Cross",
    "Cross_acc_percentage",
    "Smart pass",
    "Smart pass_acc_percentage",
    "counter_attack",
    "Ground attacking duel",
    "ip_cluster"
]

finishing = [
    "goal",
    "opportunity",
    "Shot",
    "Shot_acc_percentage",
    "goals_pr_shot",
    "ip_cluster"
]
# --------------------------------------------------------
# MISCH ATTRIBUTES ---------------------------------------
overall_accuracy = [
    "accurate",
    "acc_ratio",
    "not_accurate"
    "cluster"
]

categories = [
    "finishing",
    "game_reading",
    "duels",
    "progression",
    'established',
    'creating',
    'ip_cluster'
]

dict_lists = {
    'duels': duels,
    'game_reading': game_reading,
    'progression': progression,
    'established': established,
    'creating': creating,
    'finishing': finishing
                   }