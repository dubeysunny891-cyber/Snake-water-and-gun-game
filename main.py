from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# This is your game logic
def play_game(user_choice):
    options = ["snake", "water", "gun"]
    comp_choice = random.choice(options)
    
    if user_choice == comp_choice:
        result = "It's a draw!"
    elif (user_choice == "snake" and comp_choice == "water") or \
         (user_choice == "water" and comp_choice == "gun") or \
         (user_choice == "gun" and comp_choice == "snake"):
        result = "You Win! 🏆"
    else:
        result = "You Lose! 💀"
    
    return comp_choice, result

@app.route('/')
def home():
    # This tells Flask to show your webpage
    return render_template('index.html')

@app.route('/get_result', methods=['POST'])
def get_result():
    # This gets the click from the webpage and runs the Python logic
    data = request.json
    user_move = data['move']
    computer_move, game_result = play_game(user_move)
    return jsonify({'computer': computer_move, 'result': game_result})

if __name__ == '__main__':
    app.run(debug=True)