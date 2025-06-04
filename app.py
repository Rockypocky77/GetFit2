from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import pyrebase
import os
from functools import wraps
from datetime import datetime
from main import exercises, workout_days, equipment_options, generate_workout, get_best_exercises, generate_fixed_plan, generate_fastest_plan, generate_yearlong_plan
import requests
import socket



app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'workout-generator-secret-key-change-in-production')

# Firebase configuration
config = {
    "apiKey": "AIzaSyDvVTw-08ME_WXY8SKvADGNQBiB04YslUU",  # Note the 'Y' not 'V'
    "authDomain": "getfit-1e013.firebaseapp.com",
    "databaseURL": "https://getfit-1e013-default-rtdb.firebaseio.com/",
    "projectId": "getfit-1e013",
    "storageBucket": "getfit-1e013.firebasestorage.app",
    "messagingSenderId": "558927428638",
    "appId": "1:558927428638:web:5d6eb594aaf0a24fbfc20f"
}
def test_network_connectivity():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("✓ Basic internet connectivity: OK")
        
        response = requests.get("https://firebase.googleapis.com/", timeout=10)
        print("✓ Firebase API accessibility: OK")
        
        test_url = f"https://{config['projectId']}-default-rtdb.firebaseio.com/.json"
        response = requests.get(test_url, timeout=10)
        print("✓ Your Firebase project accessibility: OK")
        
        return True
    except Exception as e:
        print(f"✗ Network connectivity issue: {str(e)}")
        return False

# ADD this debugging route anywhere in your app.py
@app.route('/debug-firebase')
def debug_firebase():
    results = {}
    
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        results['internet'] = "✓ Connected"
    except:
        results['internet'] = "✗ No internet connection"
    
    try:
        response = requests.get("https://firebase.googleapis.com/", timeout=5)
        results['firebase_api'] = f"✓ Firebase API accessible (Status: {response.status_code})"
    except Exception as e:
        results['firebase_api'] = f"✗ Firebase API error: {str(e)}"
    
    try:
        test_url = f"https://{config['projectId']}-default-rtdb.firebaseio.com/.json"
        response = requests.get(test_url, timeout=5)
        results['database'] = f"✓ Database accessible (Status: {response.status_code})"
    except Exception as e:
        results['database'] = f"✗ Database error: {str(e)}"
    
    return f"<pre>" + "\n".join([f"{k}: {v}" for k, v in results.items()]) + "</pre>"


# Initialize Firebase
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html', user=session['user'])
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
# REPLACE your existing signup route with this enhanced version
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        
        print(f"=== SIGNUP ATTEMPT ===")
        print(f"Email: {email}")
        print(f"Username: {username}")
        print(f"Password length: {len(password)}")
        
        try:
            print("Attempting Firebase user creation...")
            
            # Create user account
            user = auth.create_user_with_email_and_password(email, password)
            print(f"✓ User created: {user['localId']}")
            
            # Store additional user data in database
            user_data = {
                "username": username,
                "email": email,
                "created_at": str(datetime.now()),
                "workout_plans": {},
                "saved_schedules": {}
            }
            
            print("Saving to database...")
            db.child("users").child(user['localId']).set(user_data)
            print("✓ User data saved")
            
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
            
        except Exception as e:
            print(f"✗ Full error details: {str(e)}")
            print(f"Error type: {type(e).__name__}")
            
            error_message = str(e)
            
            if "EMAIL_EXISTS" in error_message:
                flash('Email already exists!', 'error')
            elif "WEAK_PASSWORD" in error_message:
                flash('Password should be at least 6 characters!', 'error')
            elif "INVALID_EMAIL" in error_message:
                flash('Please enter a valid email address!', 'error')
            else:
                flash(f'Error creating account: {error_message}', 'error')
    
    return render_template('auth/signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            # Sign in user
            user = auth.sign_in_with_email_and_password(email, password)
            
            # Get user data from database
            user_data = db.child("users").child(user['localId']).get().val()
            
            # Store in session
            session['user'] = {
                'id': user['localId'],
                'email': email,
                'username': user_data['username'] if user_data else email
            }
            
            flash(f'Welcome back, {session["user"]["username"]}!', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            flash('Invalid email or password!', 'error')
    
    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    username = session.get('user', {}).get('username', 'User')
    session.clear()
    flash(f'Goodbye, {username}!', 'success')
    return redirect(url_for('index'))

@app.route('/setup', methods=['GET', 'POST'])
@login_required
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
    
    return render_template('setup.html', equipment_options=equipment_options, user=session['user'])

@app.route('/workout-plan')
@login_required
def workout_plan():
    if 'workout_plan' not in session:
        return redirect(url_for('setup'))
    
    plan = session['workout_plan']
    return render_template('workout_plan.html', plan=plan, user=session['user'])

@app.route('/replace-exercise', methods=['POST'])
@login_required
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
@login_required
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
    
    return render_template('exercise_details.html', plan=plan, user=session['user'])

@app.route('/progression-plan', methods=['GET', 'POST'])
@login_required
def progression_plan():
    if 'exercise_details' not in session:
        return redirect(url_for('exercise_details'))
    
    if request.method == 'POST':
        plan_type = request.form.get('plan_type', 'thirty_day')
        session['plan_type'] = plan_type
        return redirect(url_for('final_schedule'))
    
    return render_template('progression_plan.html', user=session['user'])

@app.route('/final-schedule')
@login_required
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
                         user_data=user_data,
                         user=session['user'])

@app.route('/save-schedule', methods=['POST'])
@login_required
def save_schedule():
    user_id = session['user']['id']
    
    if 'exercise_details' not in session or 'plan_type' not in session:
        flash('No schedule to save. Please create a workout plan first.', 'error')
        return redirect(url_for('setup'))
    
    # Create schedule data
    schedule_data = {
        'workout_plan': session['workout_plan'],
        'exercise_details': session['exercise_details'],
        'plan_type': session['plan_type'],
        'user_data': session['user_data'],
        'created_at': str(datetime.now()),
        'name': request.form.get('schedule_name', f"Workout Plan - {datetime.now().strftime('%Y-%m-%d')}")
    }
    
    # Generate schedule ID
    schedule_id = f"schedule_{int(datetime.now().timestamp())}"
    
    # Save to Firebase
    db.child("users").child(user_id).child("saved_schedules").child(schedule_id).set(schedule_data)
    
    flash('Workout schedule saved successfully!', 'success')
    return redirect(url_for('my_schedules'))

@app.route('/my-schedules')
@login_required
def my_schedules():
    user_id = session['user']['id']
    user_data = db.child("users").child(user_id).get().val()
    
    schedules = user_data.get('saved_schedules', {}) if user_data else {}
    schedule_list = []
    
    for schedule_id, schedule in schedules.items():
        schedule['id'] = schedule_id
        schedule_list.append(schedule)
    
    # Sort by creation date (newest first)
    schedule_list.sort(key=lambda x: x.get('created_at', ''), reverse=True)
    
    return render_template('my_schedules.html', schedules=schedule_list, user=session['user'])

@app.route('/load-schedule/<schedule_id>')
@login_required
def load_schedule(schedule_id):
    user_id = session['user']['id']
    
    # Get schedule from database
    schedule_data = db.child("users").child(user_id).child("saved_schedules").child(schedule_id).get().val()
    
    if not schedule_data:
        flash('Schedule not found!', 'error')
        return redirect(url_for('my_schedules'))
    
    # Load into session
    session['workout_plan'] = schedule_data['workout_plan']
    session['exercise_details'] = schedule_data['exercise_details']
    session['plan_type'] = schedule_data['plan_type']
    session['user_data'] = schedule_data['user_data']
    
    flash(f'Loaded schedule: {schedule_data["name"]}', 'success')
    return redirect(url_for('final_schedule'))

@app.route('/delete-schedule/<schedule_id>')
@login_required
def delete_schedule(schedule_id):
    user_id = session['user']['id']
    
    # Delete from database
    db.child("users").child(user_id).child("saved_schedules").child(schedule_id).remove()
    
    flash('Schedule deleted successfully!', 'success')
    return redirect(url_for('my_schedules'))

@app.route('/reset')
def reset():
    # Only clear workout-related session data, keep user logged in
    workout_keys = ['user_data', 'workout_plan', 'exercise_muscle_map', 'eq_types', 
                   'exercise_details', 'plan_type', 'replacement_counts']
    for key in workout_keys:
        session.pop(key, None)
    
    flash('Workout plan reset successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    print("=== STARTING LOCAL DEVELOPMENT SERVER ===")
    print("Testing network connectivity...")
    test_network_connectivity()
    print("Visit http://localhost:5001/debug-firebase to test Firebase connectivity")
    app.run(host='0.0.0.0', port=5001, debug=True)
