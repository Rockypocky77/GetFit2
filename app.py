
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os
from main import exercises, workout_days, equipment_options, generate_workout, get_best_exercises, generate_fixed_plan, generate_fastest_plan, generate_yearlong_plan

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'workout-generator-secret-key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setup', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        try:
            age = int(request.form.get('age', 25))
            if age < 12:
                age = 12
            frequency = int(request.form.get('frequency', 4))
            equipment = int(request.form.get('equipment', 3))
            
            if frequency < 3 or frequency > 6:
                frequency = 4
                
            session['user_data'] = {
                'age': age,
                'frequency': frequency,
                'equipment': equipment
            }
            
            result = generate_workout(equipment)
            if result:
                plan, exercise_muscle_map, eq_types = result
                session['workout_plan'] = plan
                session['exercise_muscle_map'] = exercise_muscle_map
                session['eq_types'] = eq_types
                
                return redirect(url_for('workout_plan'))
            else:
                flash('Error generating workout plan. Please try again.', 'error')
                
        except ValueError:
            flash('Please enter valid numbers for age and frequency.', 'error')
    
    return render_template('setup.html', equipment_options=equipment_options)

@app.route('/workout-plan')
def workout_plan():
    if 'workout_plan' not in session:
        return redirect(url_for('setup'))
    
    plan = session['workout_plan']
    return render_template('workout_plan.html', plan=plan)

@app.route('/replace-exercise', methods=['POST'])
def replace_exercise():
    if 'workout_plan' not in session:
        return jsonify({'success': False, 'message': 'No workout plan found'})
    
    try:
        day = request.json.get('day')
        exercise_index = int(request.json.get('exercise_index'))
        
        plan = session['workout_plan']
        exercise_muscle_map = session['exercise_muscle_map']
        eq_types = session['eq_types']
        
        if day not in plan or exercise_index >= len(plan[day]):
            return jsonify({'success': False, 'message': 'Invalid exercise selection'})
        
        exercise_to_replace = plan[day][exercise_index]
        muscle_group = exercise_muscle_map[exercise_to_replace]
        
        # Track replacement attempts for this exercise
        replacement_key = f"{day}_{exercise_index}_replacements"
        if 'replacement_counts' not in session:
            session['replacement_counts'] = {}
        
        replacement_count = session['replacement_counts'].get(replacement_key, 0)
        
        # Get current exercises to exclude (all exercises currently in the plan)
        current_exercises = []
        for day_ex in plan.values():
            current_exercises.extend(day_ex)
        
        # Remove the exercise we're replacing from the exclusion list
        if exercise_to_replace in current_exercises:
            current_exercises.remove(exercise_to_replace)
        
        available_replacements = get_best_exercises(muscle_group, eq_types, current_exercises)
        
        # Skip exercises based on replacement count to get the next best
        if available_replacements and replacement_count < len(available_replacements):
            new_exercise = available_replacements[replacement_count][0]
            
            # Make sure we're not replacing with the same exercise
            if new_exercise == exercise_to_replace and len(available_replacements) > replacement_count + 1:
                replacement_count += 1
                new_exercise = available_replacements[replacement_count][0]
            
            if new_exercise != exercise_to_replace:
                plan[day][exercise_index] = new_exercise
                
                # Update mapping
                del exercise_muscle_map[exercise_to_replace]
                exercise_muscle_map[new_exercise] = muscle_group
                
                # Increment replacement count for this position
                session['replacement_counts'][replacement_key] = replacement_count + 1
                
                session['workout_plan'] = plan
                session['exercise_muscle_map'] = exercise_muscle_map
                
                return jsonify({
                    'success': True, 
                    'new_exercise': new_exercise,
                    'message': f'Replaced "{exercise_to_replace}" with "{new_exercise}"'
                })
            else:
                return jsonify({
                    'success': False, 
                    'message': f'No more alternative exercises available for {muscle_group}'
                })
        else:
            return jsonify({
                'success': False, 
                'message': f'No more alternative exercises available for {muscle_group}'
            })
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/exercise-details', methods=['GET', 'POST'])
def exercise_details():
    if 'workout_plan' not in session:
        return redirect(url_for('setup'))
    
    plan = session['workout_plan']
    
    if request.method == 'POST':
        exercise_details = {}
        
        for day, exercises in plan.items():
            exercise_details[day] = {}
            for i, exercise in enumerate(exercises):
                field_prefix = f"{day}_{i}"
                
                try:
                    sets = int(request.form.get(f'{field_prefix}_sets', 3))
                    reps = int(request.form.get(f'{field_prefix}_reps', 10))
                    current_weight = float(request.form.get(f'{field_prefix}_current', 0))
                    target_weight = float(request.form.get(f'{field_prefix}_target', 5))
                    
                    # Round to nearest 5
                    current_weight = round(current_weight / 5) * 5
                    target_weight = round(target_weight / 5) * 5
                    
                    if target_weight <= current_weight:
                        target_weight = current_weight + 5
                    
                    exercise_details[day][exercise] = {
                        'sets': sets,
                        'reps': reps,
                        'current_weight': current_weight,
                        'target_weight': target_weight
                    }
                except ValueError:
                    # Use defaults if invalid input
                    exercise_details[day][exercise] = {
                        'sets': 3,
                        'reps': 10,
                        'current_weight': 0,
                        'target_weight': 5
                    }
        
        session['exercise_details'] = exercise_details
        return redirect(url_for('progression_plan'))
    
    return render_template('exercise_details.html', plan=plan)

@app.route('/progression-plan', methods=['GET', 'POST'])
def progression_plan():
    if 'exercise_details' not in session:
        return redirect(url_for('exercise_details'))
    
    if request.method == 'POST':
        plan_type = request.form.get('plan_type', 'thirty_day')
        session['plan_type'] = plan_type
        return redirect(url_for('final_schedule'))
    
    return render_template('progression_plan.html')

@app.route('/final-schedule')
def final_schedule():
    if 'exercise_details' not in session or 'plan_type' not in session:
        return redirect(url_for('setup'))
    
    exercise_details = session['exercise_details']
    plan_type = session['plan_type']
    user_data = session['user_data']
    frequency = user_data['frequency']
    
    # Create progression schedule
    schedule = {}
    
    if plan_type == 'yearlong':
        total_weeks = 52
    elif plan_type == 'thirty_day':
        total_weeks = 4
    else:  # as_soon_as_possible
        total_weeks = 8
    
    # Calculate progression for each exercise
    for day, exercises in exercise_details.items():
        schedule[day] = {}
        for exercise, details in exercises.items():
            current_weight = details['current_weight']
            target_weight = details['target_weight']
            
            if plan_type == 'thirty_day':
                total_workouts = frequency * 4
                progression = generate_fixed_plan(current_weight, target_weight, total_workouts)
            elif plan_type == 'yearlong':
                progression = generate_yearlong_plan(current_weight, target_weight, frequency)
            else:  # as_soon_as_possible
                progression = generate_fastest_plan(current_weight, target_weight)
            
            schedule[day][exercise] = {
                'details': details,
                'progression': progression
            }
    
    # Generate workout pattern
    if frequency <= 3:
        workout_pattern = ['Monday', 'Wednesday', 'Friday'][:frequency]
    elif frequency == 4:
        workout_pattern = ['Monday', 'Tuesday', 'Thursday', 'Friday']
    elif frequency == 5:
        workout_pattern = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    else:
        workout_pattern = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][:frequency]
    
    return render_template('final_schedule.html', 
                         schedule=schedule, 
                         total_weeks=total_weeks,
                         frequency=frequency,
                         workout_pattern=workout_pattern,
                         plan_type=plan_type,
                         user_data=user_data)

@app.route('/reset')
def reset():
    session.clear()
    flash('Workout plan reset successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
