
import sys

exercises = {
    "upper_chest": {
        "dumbbell/barbell": [
            ("Incline Barbell Bench Press", 1),
            ("Incline Dumbbell Press", 2),
            ("Reverse-Grip Barbell Bench Press", 4),
            ("Incline Dumbbell Flyes", 7),
            ("Landmine Press", 9),
            ("Incline Smith Machine Press", 12),
            ("Incline Dumbbell Squeeze Press", 15)
        ],
        "machine": [
            ("Incline Chest Press Machine", 3),
            ("Cable Incline Flyes", 5),
            ("Hammer Strength Incline Press", 6),
            ("Incline Pec Deck Machine", 10),
            ("Smith Machine Incline Press", 13),
            ("Incline Chest Fly Machine", 16),
            ("Lever Incline Press", 18)
        ],
        "bodyweight": [
            ("Feet Elevated Push-up", 8),
            ("Pseudo Planche Push-up", 11),
            ("Incline Push-up", 14),
            ("Decline Diamond Push-up", 17),
            ("Archer Push-up", 19),
            ("Clap Push-up", 20),
            ("Sphinx Push-up", 21)
        ]
    },

    "middle_chest": {
        "dumbbell/barbell": [
            ("Barbell Bench Press", 1),
            ("Dumbbell Bench Press", 2),
            ("Close-Grip Barbell Bench Press", 4),
            ("Dumbbell Flyes", 6),
            ("Cable Crossover", 8),
            ("Smith Machine Bench Press", 12),
            ("Dumbbell Pullover", 16)
        ],
        "machine": [
            ("Chest Press Machine", 3),
            ("Hammer Strength Chest Press", 5),
            ("Pec Deck Machine", 7),
            ("Cable Crossover Machine", 9),
            ("Lever Chest Press", 11),
            ("Seated Chest Fly Machine", 14),
            ("Smith Machine Bench Press", 17)
        ],
        "bodyweight": [
            ("Standard Push-up", 10),
            ("Wide-Grip Push-up", 13),
            ("Diamond Push-up", 15),
            ("Explosive Push-up", 18),
            ("Archer Push-up", 19),
            ("Pseudo Planche Push-up", 20),
            ("Sphinx Push-up", 21)
        ]
    },

    "lower_chest": {
        "dumbbell/barbell": [
            ("Decline Barbell Bench Press", 1),
            ("Decline Dumbbell Press", 2),
            ("Close-Grip Bench Press", 5),
            ("Cable Decline Flyes", 7),
            ("Dumbbell Pullover", 11),
            ("Decline Smith Machine Press", 13),
            ("Landmine Press (low angle)", 16)
        ],
        "machine": [
            ("Decline Chest Press Machine", 3),
            ("Hammer Strength Decline Press", 4),
            ("Cable Decline Fly Machine", 6),
            ("Lever Decline Press", 9),
            ("Smith Machine Decline Press", 12),
            ("Incline Chest Fly Machine (low angle)", 15),
            ("Seated Chest Press Machine (low angle)", 18)
        ],
        "bodyweight": [
            ("Decline Push-up", 8),
            ("Pseudo Planche Push-up", 10),
            ("Feet Elevated Diamond Push-up", 14),
            ("Feet Elevated Archer Push-up", 17),
            ("Clap Push-up (decline)", 19),
            ("Sphinx Push-up (decline)", 20),
            ("Explosive Decline Push-up", 21)
        ]
    },

    "lats": {
        "dumbbell/barbell": [
            ("Barbell Deadlift", 2),
            ("Barbell Bent-over Row", 3),
            ("T-bar Row", 5),
            ("Dumbbell Row", 6),
            ("Barbell Rack Pull", 8),
            ("Meadow's Row", 12),
            ("Dumbbell Renegade Row", 16)
        ],
        "machine": [
            ("Lat Pulldown Machine", 1),
            ("Seated Row Machine", 4),
            ("Cable Row", 7),
            ("Hammer Strength Row", 9),
            ("Assisted Pull-up Machine", 13),
            ("Reverse Pec Deck", 17),
            ("Smith Machine Shrugs", 21)
        ],
        "bodyweight": [
            ("Pull-up", 10),
            ("Chin-up", 11),
            ("Inverted Row", 14),
            ("Negative Pull-up", 15),
            ("Assisted Pull-up", 18),
            ("Australian Pull-up", 19),
            ("Archer Pull-up", 20)
        ]
    },

    "upper_back": {
        "dumbbell/barbell": [
            ("Barbell Power Clean", 1),
            ("Barbell Shrugs", 3),
            ("Dumbbell Shrugs", 4),
            ("Barbell Upright Row", 6),
            ("Face Pulls with Dumbbells", 8),
            ("Dumbbell High Pull", 10),
            ("Dumbbell Rear Delt Flyes", 13)
        ],
        "machine": [
            ("Cable Face Pulls", 2),
            ("Smith Machine Shrugs", 5),
            ("Cable Shrugs", 7),
            ("Reverse Pec Deck", 9),
            ("Hammer Strength Shrugs", 11),
            ("Machine Upright Row", 14),
            ("Trap Bar Deadlift", 16)
        ],
        "bodyweight": [
            ("Scapular Pull-ups", 12),
            ("Inverted Row (high angle)", 15),
            ("Prone Y Raises", 17),
            ("Wall Angels", 18),
            ("Band Pull Aparts", 19),
            ("Superman Hold", 20),
            ("Bodyweight Shrugs (scapular retractions on bar)", 21)
        ]
    },

    "rear_delts": {
        "dumbbell/barbell": [
            ("Dumbbell Rear Delt Flyes", 1),
            ("Bent-over Dumbbell Lateral Raises", 2),
            ("Face Pulls with Dumbbells", 4),
            ("Cable Rear Delt Fly", 6),
            ("Reverse Pec Deck Fly", 8),
            ("Seated Dumbbell Rear Delt Raise", 11),
            ("Barbell Upright Row (wide grip)", 15)
        ],
        "machine": [
            ("Cable Face Pulls", 3),
            ("Reverse Pec Deck Machine", 5),
            ("Cable Rear Delt Fly", 7),
            ("Hammer Strength Rear Delt Fly", 9),
            ("Seated Rear Delt Machine", 10),
            ("Incline Reverse Pec Deck", 12),
            ("Smith Machine Rear Delt Raises", 16)
        ],
        "bodyweight": [
            ("Band Pull Aparts", 13),
            ("Prone Y Raises", 14),
            ("Wall Angels", 17),
            ("Scapular Pull-ups", 18),
            ("Face Pulls with Bands", 19),
            ("Superman Hold", 20),
            ("Inverted Row with Wide Grip", 21)
        ]
    },

    "anterior_delts": {
        "dumbbell/barbell": [
            ("Standing Barbell Overhead Press", 1),
            ("Seated Dumbbell Shoulder Press", 2),
            ("Push Press", 3),
            ("Arnold Press", 5),
            ("Dumbbell Front Raises", 8),
            ("Barbell Front Raises", 10),
            ("Dumbbell Lateral Raises", 13)
        ],
        "machine": [
            ("Shoulder Press Machine", 4),
            ("Hammer Strength Shoulder Press", 6),
            ("Cable Front Raises", 7),
            ("Smith Machine Overhead Press", 9),
            ("Lateral Raise Machine", 11),
            ("Cable Lateral Raises", 12),
            ("Reverse Pec Deck (front focus)", 19)
        ],
        "bodyweight": [
            ("Handstand Push-up (wall supported)", 14),
            ("Pike Push-up", 15),
            ("Decline Pike Push-up", 16),
            ("Hindu Push-up", 17),
            ("Plank to Push-up", 18),
            ("Clap Push-up", 20),
            ("Elevated Feet Shoulder Taps", 21)
        ]
    },

    "lateral_delts": {
        "dumbbell/barbell": [
            ("Dumbbell Lateral Raises", 1),
            ("Dumbbell Overhead Press", 3),
            ("Cable Lateral Raises with Dumbbells", 4),
            ("Barbell Upright Row", 6),
            ("Dumbbell Cuban Press", 9),
            ("Arnold Press", 11),
            ("Kettlebell Overhead Press", 13)
        ],
        "machine": [
            ("Lateral Raise Machine", 2),
            ("Cable Lateral Raises", 5),
            ("Hammer Strength Lateral Raise", 7),
            ("Smith Machine Overhead Press", 8),
            ("Cable Face Pulls", 10),
            ("Reverse Pec Deck", 12),
            ("Seated Dumbbell Shoulder Press", 14)
        ],
        "bodyweight": [
            ("Pike Push-up", 15),
            ("Handstand Wall Walks", 16),
            ("Band Lateral Raises", 17),
            ("Wall Angels", 18),
            ("Side Plank with Arm Raise", 19),
            ("Prone Y Raises", 20),
            ("Arm Circles", 21)
        ]
    },

    "biceps_long_head": {
        "dumbbell/barbell": [
            ("Incline Dumbbell Curl", 1),
            ("Barbell Curl", 2),
            ("Hammer Curl", 4),
            ("Preacher Curl", 6),
            ("Concentration Curl", 8),
            ("Cable Rope Curl", 10),
            ("Zottman Curl", 13)
        ],
        "machine": [
            ("Preacher Curl Machine", 3),
            ("Cable Bicep Curl", 5),
            ("Hammer Strength Bicep Curl", 7),
            ("Bicep Curl Machine", 9),
            ("Cable Rope Hammer Curl", 11),
            ("Incline Curl Machine", 12),
            ("Cable Concentration Curl", 16)
        ],
        "bodyweight": [
            ("Chin-up", 14),
            ("Negative Chin-up", 15),
            ("Inverted Row with Underhand Grip", 17),
            ("Australian Chin-up", 18),
            ("Isometric Chin-up Hold", 19),
            ("Band Assisted Chin-up", 20),
            ("Towel Hang", 21)
        ]
    },

    "biceps_short_head": {
        "dumbbell/barbell": [
            ("Concentration Curl", 1),
            ("Barbell Curl (close grip)", 2),
            ("Spider Curl", 3),
            ("Cable Rope Curl (wide grip)", 5),
            ("Dumbbell Bicep Curl", 7),
            ("Hammer Curl", 9),
            ("Preacher Curl", 11)
        ],
        "machine": [
            ("Preacher Curl Machine", 4),
            ("Cable Concentration Curl", 6),
            ("Bicep Curl Machine", 8),
            ("Cable Rope Hammer Curl", 10),
            ("Hammer Strength Bicep Curl", 12),
            ("Cable Bicep Curl", 13),
            ("Incline Curl Machine", 16)
        ],
        "bodyweight": [
            ("Chin-up", 14),
            ("Negative Chin-up", 15),
            ("Inverted Row with Underhand Grip", 17),
            ("Australian Chin-up", 18),
            ("Isometric Chin-up Hold", 19),
            ("Band Assisted Chin-up", 20),
            ("Towel Hang", 21)
        ]
    },

    "triceps_long_head": {
        "dumbbell/barbell": [
            ("Overhead Dumbbell Extension", 1),
            ("Close-Grip Barbell Bench Press", 2),
            ("Skull Crushers", 4),
            ("Cable Rope Overhead Extension", 6),
            ("Dips (weighted if possible)", 7),
            ("Triceps Kickbacks", 12),
            ("Diamond Push-up", 15)
        ],
        "machine": [
            ("Overhead Triceps Extension Machine", 3),
            ("Cable Rope Overhead Extension", 5),
            ("Triceps Pushdown Machine", 8),
            ("Triceps Dip Machine", 9),
            ("Hammer Strength Triceps Extension", 10),
            ("Cable Kickbacks", 13),
            ("Smith Machine Close-Grip Bench Press", 16)
        ],
        "bodyweight": [
            ("Triceps Dips", 11),
            ("Diamond Push-up", 14),
            ("Close-Grip Push-up", 17),
            ("Bench Dips", 18),
            ("Pseudo Planche Push-up", 19),
            ("Bodyweight Skull Crushers (on bar)", 20),
            ("Straight Bar Dips", 21)
        ]
    },

    "triceps_lateral_head": {
        "dumbbell/barbell": [
            ("Close-Grip Bench Press", 1),
            ("Triceps Pushdown", 3),
            ("Dips", 5),
            ("Overhead Dumbbell Extension", 7),
            ("Skull Crushers", 9),
            ("Cable Kickbacks", 12),
            ("Diamond Push-up", 15)
        ],
        "machine": [
            ("Triceps Pushdown Machine", 2),
            ("Triceps Dip Machine", 4),
            ("Cable Kickbacks", 6),
            ("Hammer Strength Triceps Extension", 8),
            ("Cable Rope Overhead Extension", 10),
            ("Smith Machine Close-Grip Bench Press", 13),
            ("Overhead Triceps Extension Machine", 16)
        ],
        "bodyweight": [
            ("Diamond Push-up", 11),
            ("Triceps Dips", 14),
            ("Close-Grip Push-up", 17),
            ("Bench Dips", 18),
            ("Pseudo Planche Push-up", 19),
            ("Bodyweight Skull Crushers", 20),
            ("Straight Bar Dips", 21)
        ]
    },

    "forearms_brachialis": {
        "dumbbell/barbell": [
            ("Hammer Curl", 1),
            ("Reverse Curl", 2),
            ("Farmer's Walk", 4),
            ("Zottman Curl", 6),
            ("Barbell Wrist Curl", 8),
            ("Dumbbell Wrist Curl", 10),
            ("Cable Wrist Curl", 13)
        ],
        "machine": [
            ("Wrist Curl Machine", 3),
            ("Cable Reverse Curl", 5),
            ("Reverse Wrist Curl Machine", 7),
            ("Forearm Roller", 9),
            ("Hammer Strength Wrist Curl", 11),
            ("Cable Wrist Curl", 12),
            ("Plate Pinch", 16)
        ],
        "bodyweight": [
            ("Dead Hang", 14),
            ("Towel Hang", 15),
            ("Finger Tip Push-up", 17),
            ("Wall Climbing", 18),
            ("Isometric Finger Squeeze", 19),
            ("Bodyweight Wrist Extension", 20),
            ("Forearm Plank", 21)
        ]
    },

    "quads": {
        "dumbbell/barbell": [
            ("Barbell Back Squat", 1),
            ("Barbell Front Squat", 2),
            ("Bulgarian Split Squat", 4),
            ("Barbell Lunges", 6),
            ("Goblet Squat", 8),
            ("Dumbbell Lunges", 10),
            ("Overhead Squat", 16)
        ],
        "machine": [
            ("Hack Squat Machine", 3),
            ("Leg Press", 5),
            ("Leg Extension", 7),
            ("Smith Machine Squat", 9),
            ("Pendulum Squat", 11),
            ("Belt Squat Machine", 12),
            ("Sissy Squat Machine", 17)
        ],
        "bodyweight": [
            ("Pistol Squats", 13),
            ("Jump Squats", 14),
            ("Bodyweight Squats", 15),
            ("Split Squats", 18),
            ("Jump Lunges", 19),
            ("Single Leg Squat", 20),
            ("Wall Sit", 21)
        ]
    },

    "hamstrings": {
        "dumbbell/barbell": [
            ("Romanian Deadlift", 1),
            ("Conventional Deadlift", 2),
            ("Stiff Leg Deadlift", 3),
            ("Dumbbell Romanian Deadlift", 4),
            ("Good Mornings", 7),
            ("Single Leg Romanian Deadlift", 9),
            ("Sumo Deadlift", 11)
        ],
        "machine": [
            ("Lying Leg Curl", 5),
            ("Seated Leg Curl", 6),
            ("Glute Ham Raise Machine", 8),
            ("Nordic Hamstring Curl Machine", 10),
            ("Cable Pull Through", 12),
            ("Smith Machine Romanian Deadlift", 14),
            ("Reverse Hyperextension", 16)
        ],
        "bodyweight": [
            ("Nordic Hamstring Curl", 13),
            ("Glute Ham Raise", 15),
            ("Single Leg Glute Bridge", 17),
            ("Single Leg Deadlift", 18),
            ("Good Morning (bodyweight)", 19),
            ("Reverse Lunge", 20),
            ("Mountain Climbers", 21)
        ]
    },

    "glutes": {
        "dumbbell/barbell": [
            ("Barbell Hip Thrust", 1),
            ("Romanian Deadlift", 2),
            ("Barbell Back Squat", 3),
            ("Bulgarian Split Squat", 4),
            ("Sumo Deadlift", 6),
            ("Dumbbell Hip Thrust", 7),
            ("Single Leg Romanian Deadlift", 10)
        ],
        "machine": [
            ("Hip Thrust Machine", 5),
            ("Cable Pull Through", 8),
            ("Leg Press (wide stance)", 9),
            ("Glute Ham Raise Machine", 11),
            ("Smith Machine Hip Thrust", 12),
            ("Cable Kickbacks", 14),
            ("Abduction Machine", 16)
        ],
        "bodyweight": [
            ("Single Leg Glute Bridge", 13),
            ("Glute Bridge", 15),
            ("Clamshells", 17),
            ("Fire Hydrants", 18),
            ("Curtsy Lunges", 19),
            ("Lateral Walks", 20),
            ("Donkey Kicks", 21)
        ]
    },

    "calves": {
        "dumbbell/barbell": [
            ("Standing Barbell Calf Raise", 1),
            ("Dumbbell Calf Raise", 2),
            ("Single Leg Dumbbell Calf Raise", 4),
            ("Barbell Seated Calf Raise", 6),
            ("Dumbbell Seated Calf Raise", 8),
            ("Farmer's Walk on Toes", 11),
            ("Walking Calf Raises", 14)
        ],
        "machine": [
            ("Standing Calf Raise Machine", 3),
            ("Seated Calf Raise Machine", 5),
            ("Leg Press Calf Raise", 7),
            ("Smith Machine Calf Raise", 9),
            ("Donkey Calf Raise Machine", 10),
            ("Hack Squat Calf Raise", 12),
            ("Cable Calf Raise", 15)
        ],
        "bodyweight": [
            ("Single Leg Calf Raise", 13),
            ("Double Leg Calf Raise", 16),
            ("Calf Raise on Steps", 17),
            ("Jump Rope", 18),
            ("Pogo Jumps", 19),
            ("Wall Calf Raise", 20),
            ("Hill Sprints", 21)
        ]
    },

    "core": {
        "dumbbell/barbell": [
            ("Barbell Rollouts", 2),
            ("Farmers Walk", 4),
            ("Weighted Planks", 6),
            ("Weighted Russian Twists", 8),
            ("Weighted Dead Bug", 10),
            ("Dumbbell Side Bends", 13),
            ("Weighted Sit-ups", 16)
        ],
        "machine": [
            ("Cable Pallof Press", 1),
            ("Cable Woodchoppers", 3),
            ("Cable Crunches", 5),
            ("Cable Side Bends", 7),
            ("Ab Wheel Machine", 9),
            ("Decline Sit-up Machine", 14),
            ("Seated Russian Twists Machine", 18)
        ],
        "bodyweight": [
            ("Plank", 11),
            ("Dead Bug", 12),
            ("Hollow Body Hold", 15),
            ("Bear Crawl", 17),
            ("Mountain Climbers", 19),
            ("Bicycle Crunches", 20),
            ("Russian Twists", 21)
        ]
    },

    "traps": {
        "dumbbell/barbell": [
            ("Barbell Shrugs", 1),
            ("Barbell High Pull", 2),
            ("Dumbbell Shrugs", 3),
            ("Dumbbell High Pull", 5),
            ("Power Shrugs", 7),
            ("Barbell Upright Row", 9),
            ("Behind the Back Barbell Shrugs", 12)
        ],
        "machine": [
            ("Trap Bar Shrugs", 4),
            ("Smith Machine Shrugs", 6),
            ("Cable Shrugs", 8),
            ("Hammer Strength Shrugs", 10),
            ("Machine Upright Row", 11),
            ("Cable Upright Row", 13),
            ("Seated Cable Shrugs", 16)
        ],
        "bodyweight": [
            ("Scapular Pull-ups", 14),
            ("Shoulder Blade Squeezes", 15),
            ("Inverted Row Shrugs", 17),
            ("Band Pull Aparts", 18),
            ("Pike Push-up Shrugs", 19),
            ("Prone Y-T-W Raises", 20),
            ("Wall Handstand Shrugs", 21)
        ]
    }
}


# History stack for undo functionality
history_stack = []

def save_state(state_type, data):
    """Save current state to history stack"""
    history_stack.append({
        'type': state_type,
        'data': data
    })
    # Keep only last 10 states to prevent memory issues
    if len(history_stack) > 10:
        history_stack.pop(0)

def undo_last_action():
    """Undo the last action if possible"""
    if history_stack:
        return history_stack.pop()
    return None

# Map days to specific muscle groups for workout structure
workout_days = {
    "Push day": ["upper_chest", "middle_chest", "lower_chest", "anterior_delts", "lateral_delts", "triceps_long_head", "triceps_lateral_head"],
    "Pull day": ["lats", "upper_back", "rear_delts", "biceps_long_head", "biceps_short_head", "forearms_brachialis"],
    "Legs day": ["quads", "hamstrings", "glutes", "calves"],
    "Misc day": ["core", "traps", "forearms_brachialis"]
}

# Available equipment options:
equipment_options = {
    1: "dumbbell/barbell",
    2: "machine",
    3: "both",
    4: "bodyweight"
}

# Progression calculation functions
def generate_fixed_plan(current_weight, target_weight, workouts):
    """Generate a fixed-duration progression plan with proper 5lb increments"""
    # Minimum increment is 5 lbs (2.5 lb plates on each side)
    jump = 5
    plan = []

    # Calculate total number of 5lb jumps needed
    total_jumps = int((target_weight - current_weight) / jump)

    print(f"DEBUG: Current: {current_weight}, Target: {target_weight}, Workouts: {workouts}, Jumps needed: {total_jumps}")

    # If no jumps needed, return current weight for all workouts
    if total_jumps <= 0:
        print("DEBUG: No jumps needed, returning current weight for all workouts")
        return [current_weight] * workouts

    # If we need more jumps than we have workouts, we can't reach target
    if total_jumps >= workouts:
        print(f"Warning: Cannot reach target weight in {workouts} workouts with 5lb increments.")
        print(f"Maximum achievable: {current_weight + (workouts - 1) * jump} lbs")
        # Create a plan that increases every workout
        for i in range(workouts):
            plan.append(current_weight + i * jump)
        return plan

    # Create schedule for when to make jumps
    jumps_schedule = [0] * workouts

    # Evenly space the jumps throughout the plan
    if total_jumps > 0:
        spacing = workouts / total_jumps
        print(f"DEBUG: Spacing jumps every {spacing:.2f} workouts")
        for i in range(total_jumps):
            jump_position = int((i + 1) * spacing) - 1
            # Ensure we don't go out of bounds
            if jump_position < workouts:
                jumps_schedule[jump_position] = 1
                print(f"DEBUG: Jump #{i+1} scheduled at workout #{jump_position + 1}")

    # Build the plan
    weight = current_weight
    for i in range(workouts):
        plan.append(weight)
        if jumps_schedule[i] == 1:
            weight += jump
            print(f"DEBUG: After workout #{i+1}, weight increases to {weight}")

    print(f"DEBUG: Final plan: {plan}")
    return plan

def generate_fastest_plan(current_weight, target_weight):
    """Generate the fastest possible progression plan with autoregulation"""
    plan = []
    weight = current_weight
    jump = 5  # 2.5 lb plates on each side

    while weight < target_weight:
        # Autoregulate: repeat the same weight twice before increasing
        plan.append(weight)
        plan.append(weight)  # Stay at same weight for 2 workouts
        weight += jump

        # Don't exceed target
        if weight > target_weight:
            weight = target_weight

    # Make sure we hit the target weight at least once
    if not plan or plan[-1] != target_weight:
        plan.append(target_weight)

    return plan

def generate_yearlong_plan(current_weight, target_weight, frequency):
    """Generate a proper yearlong progression plan"""
    total_workouts = frequency * 52  # 52 weeks in a year
    return generate_fixed_plan(current_weight, target_weight, total_workouts)

def get_best_exercises(muscle, eq_types, exclude_exercises=None):
    """Get exercises for a muscle group, sorted by rank"""
    if exclude_exercises is None:
        exclude_exercises = []

    available_ex = []
    for eq in eq_types:
        if eq in exercises[muscle]:
            for exercise_name, rank in exercises[muscle][eq]:
                if exercise_name not in exclude_exercises:
                    available_ex.append((exercise_name, rank, muscle))

    # Sort by rank (lower number = better rank)
    available_ex.sort(key=lambda x: x[1])
    return available_ex

def generate_workout(equipment_choice):
    eq_types = []
    if equipment_choice == 1:
        eq_types = ["dumbbell/barbell", "bodyweight"]
    elif equipment_choice == 2:
        eq_types = ["machine", "bodyweight"]
    elif equipment_choice == 3:
        eq_types = ["dumbbell/barbell", "machine", "bodyweight"]
    elif equipment_choice == 4:
        eq_types = ["bodyweight"]
    else:
        print("Invalid equipment choice.")
        return None

    plan = {}
    exercise_muscle_map = {}  # Track which muscle group each exercise belongs to

    for day, muscles in workout_days.items():
        day_exercises = []
        used_exercises = []

        # First, get one exercise from each muscle group (highest ranking)
        for muscle in muscles:
            if muscle not in exercises:
                continue

            best_exercises = get_best_exercises(muscle, eq_types)
            if best_exercises:
                exercise_name = best_exercises[0][0]
                day_exercises.append(exercise_name)
                used_exercises.append(exercise_name)
                exercise_muscle_map[exercise_name] = muscle

        # Now add more exercises to reach minimum 4, maximum 7
        all_available = []
        for muscle in muscles:
            if muscle in exercises:
                muscle_exercises = get_best_exercises(muscle, eq_types, used_exercises)
                all_available.extend(muscle_exercises)

        # Sort all available exercises by rank
        all_available.sort(key=lambda x: x[1])

        # Add exercises until we reach 4-7 total
        for exercise_name, rank, muscle in all_available:
            if len(day_exercises) >= 7:
                break
            if exercise_name not in used_exercises:
                day_exercises.append(exercise_name)
                used_exercises.append(exercise_name)
                exercise_muscle_map[exercise_name] = muscle

        # Ensure we have at least 4 exercises
        while len(day_exercises) < 4 and len(day_exercises) < len(all_available):
            for exercise_name, rank, muscle in all_available:
                if exercise_name not in used_exercises:
                    day_exercises.append(exercise_name)
                    used_exercises.append(exercise_name)
                    exercise_muscle_map[exercise_name] = muscle
                    break

        plan[day] = day_exercises

    return plan, exercise_muscle_map, eq_types

def print_workout_plan(plan):
    """Print the current workout plan"""
    print("\nCurrent Workout Plan:\n")
    for day, ex_list in plan.items():
        print(f"{day}:")
        if ex_list:
            for i, ex in enumerate(ex_list, 1):
                print(f"  {i}. {ex}")
        else:
            print("  No exercises available for the selected equipment.")
        print()

def replace_exercise(plan, exercise_muscle_map, eq_types):
    """Handle exercise replacement functionality with undo support"""
    while True:
        replace_choice = input("\nWould you like to replace any exercise? (yes/no/undo): ").lower().strip()

        if replace_choice in ['no', 'n']:
            break
        elif replace_choice in ['undo', 'u']:
            last_state = undo_last_action()
            if last_state and last_state['type'] == 'exercise_replacement':
                # Restore previous state
                old_data = last_state['data']
                plan[old_data['day']][old_data['index']] = old_data['old_exercise']
                del exercise_muscle_map[old_data['new_exercise']]
                exercise_muscle_map[old_data['old_exercise']] = old_data['muscle_group']
                print(f"\n✅ Undid replacement: Restored '{old_data['old_exercise']}'")
                print_workout_plan(plan)
            else:
                print("❌ No exercise replacement to undo.")
        elif replace_choice in ['yes', 'y']:
            # Save current state before making changes
            current_state = {
                'plan': {day: exercises[:] for day, exercises in plan.items()},
                'exercise_muscle_map': exercise_muscle_map.copy()
            }

            # Show available days
            day_options = list(plan.keys())
            print("\nAvailable workout days:")
            for i, day in enumerate(day_options, 1):
                print(f"{i}. {day}")

            try:
                day_choice = int(input("Which day? (enter number): ")) - 1
                if day_choice < 0 or day_choice >= len(day_options):
                    print("Invalid day selection.")
                    continue

                selected_day = day_options[day_choice]
                exercises_list = plan[selected_day]

                if not exercises_list:
                    print("No exercises available for this day.")
                    continue

                # Show exercises for selected day
                print(f"\nExercises for {selected_day}:")
                for i, exercise in enumerate(exercises_list, 1):
                    print(f"{i}. {exercise}")

                exercise_choice = int(input("Which exercise number to replace? (enter number): ")) - 1
                if exercise_choice < 0 or exercise_choice >= len(exercises_list):
                    print("Invalid exercise selection.")
                    continue

                exercise_to_replace = exercises_list[exercise_choice]
                muscle_group = exercise_muscle_map[exercise_to_replace]

                # Get all exercises for this muscle group, excluding current ones in the plan
                current_exercises = []
                for day_ex in plan.values():
                    current_exercises.extend(day_ex)

                available_replacements = get_best_exercises(muscle_group, eq_types, current_exercises)

                if available_replacements:
                    # Replace with the next best exercise
                    new_exercise = available_replacements[0][0]

                    # Save the replacement action for undo
                    save_state('exercise_replacement', {
                        'day': selected_day,
                        'index': exercise_choice,
                        'old_exercise': exercise_to_replace,
                        'new_exercise': new_exercise,
                        'muscle_group': muscle_group
                    })

                    exercises_list[exercise_choice] = new_exercise

                    # Update the mapping
                    del exercise_muscle_map[exercise_to_replace]
                    exercise_muscle_map[new_exercise] = muscle_group

                    print(f"\n✅ Replaced '{exercise_to_replace}' with '{new_exercise}'")
                    print("💡 Type 'undo' to reverse this change if needed.")
                    print_workout_plan(plan)
                else:
                    print(f"❌ No alternative exercises available for {muscle_group} with your equipment selection.")

            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Please enter 'yes', 'no', or 'undo'.")

def collect_exercise_details(plan):
    """Collect sets, reps, current weight, and target weight for each exercise with undo support"""
    exercise_details = {}

    print("\n" + "="*60)
    print("EXERCISE CONFIGURATION")
    print("="*60)
    print("For each exercise, please provide the following details:")
    print("- Sets: How many sets you want to perform")
    print("- Reps: How many repetitions per set")
    print("- Current Weight: Your current working weight (lbs)")
    print("- Target Weight: Your goal weight (lbs)")
    print("💡 Type 'undo' at any time to go back and change previous entries")
    print("⚠️  Note: Weight increases are in 5lb increments (2.5lb plates on each side)")
    print("-" * 60)

    all_exercises = []
    for day, exercises in plan.items():
        for exercise in exercises:
            all_exercises.append((day, exercise))

    current_index = 0

    while current_index < len(all_exercises):
        day, exercise = all_exercises[current_index]

        if day not in exercise_details:
            exercise_details[day] = {}

        print(f"\n📅 {day.upper()} - Exercise {current_index + 1}/{len(all_exercises)}")
        print(f"🏋️ {exercise}:")

        try:
            sets_input = input("  Sets: ").strip().lower()
            if sets_input == 'undo' and current_index > 0:
                current_index -= 1
                # Remove the previous exercise data
                prev_day, prev_exercise = all_exercises[current_index]
                if prev_day in exercise_details and prev_exercise in exercise_details[prev_day]:
                    del exercise_details[prev_day][prev_exercise]
                    if not exercise_details[prev_day]:  # If day is empty, remove it
                        del exercise_details[prev_day]
                print(f"⏪ Going back to previous exercise...")
                continue

            sets = int(sets_input)

            reps_input = input("  Reps per set: ").strip().lower()
            if reps_input == 'undo' and current_index > 0:
                current_index -= 1
                prev_day, prev_exercise = all_exercises[current_index]
                if prev_day in exercise_details and prev_exercise in exercise_details[prev_day]:
                    del exercise_details[prev_day][prev_exercise]
                    if not exercise_details[prev_day]:
                        del exercise_details[prev_day]
                print(f"⏪ Going back to previous exercise...")
                continue

            reps = int(reps_input)

            current_weight_input = input("  Current weight (lbs): ").strip().lower()
            if current_weight_input == 'undo' and current_index > 0:
                current_index -= 1
                prev_day, prev_exercise = all_exercises[current_index]
                if prev_day in exercise_details and prev_exercise in exercise_details[prev_day]:
                    del exercise_details[prev_day][prev_exercise]
                    if not exercise_details[prev_day]:
                        del exercise_details[prev_day]
                print(f"⏪ Going back to previous exercise...")
                continue

            current_weight = float(current_weight_input)
            # Round to nearest 5 for consistency
            current_weight = round(current_weight / 5) * 5

            target_weight_input = input("  Target weight (lbs): ").strip().lower()
            if target_weight_input == 'undo' and current_index > 0:
                current_index -= 1
                prev_day, prev_exercise = all_exercises[current_index]
                if prev_day in exercise_details and prev_exercise in exercise_details[prev_day]:
                    del exercise_details[prev_day][prev_exercise]
                    if not exercise_details[prev_day]:
                        del exercise_details[prev_day]
                print(f"⏪ Going back to previous exercise...")
                continue

            target_weight = float(target_weight_input)
            # Round to nearest 5 for consistency
            target_weight = round(target_weight / 5) * 5

            # Validate that target is achievable
            if target_weight <= current_weight:
                print(f"⚠️  Target weight ({target_weight}) should be higher than current weight ({current_weight})")
                print("💡 Using current weight + 5 lbs as minimum target")
                target_weight = current_weight + 5

            exercise_details[day][exercise] = {
                'sets': sets,
                'reps': reps,
                'current_weight': current_weight,
                'target_weight': target_weight
            }

            print(f"✅ Saved: {sets} sets × {reps} reps @ {current_weight}-{target_weight} lbs")
            current_index += 1

        except ValueError:
            if sets_input != 'undo' and reps_input != 'undo' and current_weight_input != 'undo' and target_weight_input != 'undo':
                print("❌ Invalid input. Please enter valid numbers.")
                print("💡 Using default values (3 sets, 10 reps, 0 current weight, 5 target weight)")
                exercise_details[day][exercise] = {
                    'sets': 3,
                    'reps': 10,
                    'current_weight': 0,
                    'target_weight': 5
                }
                current_index += 1

    # Final confirmation with option to redo
    print(f"\n📋 EXERCISE DETAILS SUMMARY:")
    print("="*50)
    for day, exercises in exercise_details.items():
        print(f"\n📅 {day}:")
        for exercise, details in exercises.items():
            print(f"  🏋️ {exercise}: {details['sets']} sets × {details['reps']} reps @ {details['current_weight']}-{details['target_weight']} lbs")

    while True:
        confirm = input(f"\n✅ Confirm these exercise details? (yes/no/redo): ").lower().strip()
        if confirm in ['yes', 'y']:
            break
        elif confirm in ['no', 'n']:
            return None
        elif confirm in ['redo', 'r']:
            return collect_exercise_details(plan)  # Recursive call to start over
        else:
            print("Please enter 'yes', 'no', or 'redo'.")

    return exercise_details

def create_progression_schedule(exercise_details, plan_type, frequency, age):
    """Create a week-by-week progression schedule"""
    schedule = {}

    # Determine number of weeks based on plan type
    if plan_type == 'yearlong':
        total_weeks = 52
    elif plan_type == 'thirty_day':
        total_weeks = 4
    else:  # as_soon_as_possible
        total_weeks = 8  # Reasonable timeframe for ASAP

    # Calculate progression for each exercise
    for day, exercises in exercise_details.items():
        schedule[day] = {}
        for exercise, details in exercises.items():
            current_weight = details['current_weight']
            target_weight = details['target_weight']

            print(f"Generating progression for {exercise}: {current_weight} → {target_weight} lbs ({plan_type})")

            if plan_type == 'thirty_day':
                total_workouts = frequency * 4
                progression = generate_fixed_plan(current_weight, target_weight, total_workouts)
            elif plan_type == 'yearlong':
                progression = generate_yearlong_plan(current_weight, target_weight, frequency)
            else:  # as_soon_as_possible
                progression = generate_fastest_plan(current_weight, target_weight)

            # Show progression preview
            if len(progression) > 10:
                print(f"  Progression preview: {progression[:5]} ... {progression[-5:]}")
            else:
                print(f"  Full progression: {progression}")

            schedule[day][exercise] = {
                'details': details,
                'progression': progression
            }

    return schedule, total_weeks

def print_weekly_schedule(schedule, total_weeks, frequency):
    """Print the complete weekly workout schedule"""
    print("\n" + "="*80)
    print("📅 WEEKLY WORKOUT SCHEDULE")
    print("="*80)

    # Define workout days based on frequency
    if frequency <= 3:
        workout_pattern = ['Monday', 'Wednesday', 'Friday'][:frequency]
    elif frequency == 4:
        workout_pattern = ['Monday', 'Tuesday', 'Thursday', 'Friday']
    elif frequency == 5:
        workout_pattern = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    else:
        workout_pattern = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][:frequency]

    days_list = list(schedule.keys())

    # Track how many times each exercise has been performed
    exercise_session_counts = {}
    for day in days_list:
        for exercise in schedule[day].keys():
            exercise_session_counts[f"{day}_{exercise}"] = 0

    # Calculate total workout sessions needed for display
    max_display_weeks = min(total_weeks, 12)
    total_sessions_to_show = max_display_weeks * frequency

    for week in range(1, max_display_weeks + 1):
        print(f"\n📆 WEEK {week}")
        print("-" * 40)

        for workout_day_index, day_name in enumerate(workout_pattern):
            current_day = days_list[workout_day_index % len(days_list)]
            print(f"\n🏋️ {day_name} - {current_day}")

            for exercise, data in schedule[current_day].items():
                details = data['details']
                progression = data['progression']

                # Get the session count for this specific exercise
                counter_key = f"{current_day}_{exercise}"
                session_count = exercise_session_counts[counter_key]

                # Get current weight from progression
                if session_count < len(progression):
                    current_weight = progression[session_count]
                else:
                    current_weight = progression[-1]

                print(f"  • {exercise}")
                print(f"    {details['sets']} sets × {details['reps']} reps @ {current_weight:.0f} lbs")
                print(f"    (Session #{session_count + 1} for this exercise)")

                # Increment the session count for this exercise
                exercise_session_counts[counter_key] += 1

        # Add rest days
        all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        rest_days = [day for day in all_days if day not in workout_pattern]
        if rest_days:
            print(f"\n😴 Rest Days: {', '.join(rest_days)}")

    # Show progression summary
    print(f"\n" + "="*80)
    print("📈 PROGRESSION SUMMARY")
    print("="*80)
    for day in days_list:
        print(f"\n📅 {day}:")
        for exercise, data in schedule[day].items():
            details = data['details']
            progression = data['progression']
            start_weight = details['current_weight']
            target_weight = details['target_weight']

            # Show first few and last few weights
            if len(progression) > 6:
                display_progression = f"{progression[0]}, {progression[1]}, {progression[2]} ... {progression[-3]}, {progression[-2]}, {progression[-1]}"
            else:
                display_progression = ", ".join(map(str, progression))

            print(f"  🏋️ {exercise}:")
            print(f"    Start: {start_weight} lbs → Target: {target_weight} lbs")
            print(f"    Progression: {display_progression}")
            print(f"    Total sessions: {len(progression)}")

def main():
    print("🏋️ Welcome to the Enhanced Workout Generator! 💪\n")
    print("⚠️  Important: Weight increases are in 5lb increments only (2.5lb plates on each side)\n")

    # Get basic user information
    try:
        age = int(input("Enter your age: "))
        frequency = int(input("How many times per week do you plan to workout? (3-6): "))
        if frequency < 3 or frequency > 6:
            print("Frequency adjusted to 4 times per week (recommended range: 3-6)")
            frequency = 4
    except ValueError:
        print("Invalid input. Using default values (age: 25, frequency: 4)")
        age = 25
        frequency = 4

    print("\nWhat equipment do you have access to? (type the number)")
    print("1. Weights only (dumbbell/barbell)")
    print("2. Machines only")
    print("3. Both weights and machines")
    print("4. Neither (bodyweight only)")

    try:
        choice = int(input("Your choice: "))
        result = generate_workout(choice)

        if result is None:
            return

        plan, exercise_muscle_map, eq_types = result
        print_workout_plan(plan)
        replace_exercise(plan, exercise_muscle_map, eq_types)

        print("\nFinal Workout Plan:")
        print_workout_plan(plan)

        # Confirm the plan
        confirm = input("Confirm this workout plan? (yes/no): ").lower().strip()
        if confirm not in ['yes', 'y']:
            print("Plan not confirmed. Exiting...")
            return

        print("\n🎯 PROGRESSION PLANNING")
        print("Choose your progression plan:")
        print("a) Year-long plan (52 weeks) - Very gradual progression")
        print("b) Thirty-day plan (4 weeks) - Moderate progression")
        print("c) As soon as possible plan (aggressive progression with autoregulation)")

        plan_option = input("Enter 'a', 'b', or 'c': ").strip().lower()

        if plan_option == 'a':
            plan_type = 'yearlong'
            print("\n📅 Generating year-long progression plan...")
        elif plan_option == 'b':
            plan_type = 'thirty_day'
            print("\n📅 Generating 30-day progression plan...")
        elif plan_option == 'c':
            plan_type = 'as_soon_as_possible'
            print("\n📅 Generating aggressive progression plan...")
        else:
            print("Invalid selection. Using 30-day plan as default.")
            plan_type = 'thirty_day'

        # Collect exercise details
        exercise_details = collect_exercise_details(plan)

        # Check if user cancelled exercise details collection
        if exercise_details is None:
            print("❌ Exercise details collection cancelled. Exiting...")
            return

        # Create progression schedule
        schedule, total_weeks = create_progression_schedule(exercise_details, plan_type, frequency, age)

        # Print the weekly schedule
        print_weekly_schedule(schedule, total_weeks, frequency)

        print(f"\n✅ Complete {plan_type.replace('_', ' ')} progression plan generated!")
        print(f"📊 Total duration: {total_weeks} weeks")
        print(f"🏋️ Workout frequency: {frequency} times per week")
        print("💡 Remember: All weight increases are in 5lb increments!")

    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()
