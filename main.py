from flask import Flask
from flask import request, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    players_num = request.args.get("players_num", "")
    if players_num:
        platform = platform_builder(players_num)
    else:
        platform = ""
    return render_template("index.html", output=platform)
            
# @app.route("/<int:players_num>")
def platform_builder(players_num):
    try:
        num = int(players_num)
        def get_assigned (file):
            handle = open(file)
            list =[]
            for item in handle:
                item = item.rstrip()
                list.append(item)
            assignment = random.choice(list)
            return assignment

        name = ""
        if num <= 1:
            return "Awww Would it be nice to have at least 2 people for the scene? 😚"
        else:
            for num_iterable in range(num):
                if num_iterable == num -1:
                    punctuation = "."
                elif num_iterable == num -2:
                    punctuation = " and "               
                else:
                    punctuation = ", "
                name += f'{get_assigned("database/dict-names.txt")}{punctuation}'

        action = get_assigned("database/dict-actions.txt")
        location = get_assigned("database/dict-locations.txt")                           
        action_formated = action[0].lower() + action[1:]
        location_formated = location[0].lower() + location[1:]
        
        return f'You are {name} \n And you are {action_formated} in the {location_formated}.'
    
    except ValueError:
        return "Please enter the number only."


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)        