from flask import Flask,jsonify,request
import ipl
app=Flask(__name__)

@app.route('/')
def home ():
    return "Hello World - IPL API"

@app.route('/api/teams')
def teams():
    try:
        teams_data = ipl.teamsapi()
        return jsonify(teams_data)
    except Exception as e:
        return jsonify({"error": "An internal server error occurred while fetching team data."}), 500
    
@app.route('/api/team1_vs_team2')
def team_vs():
    team_1=request.args.get('team1')
    team_2=request.args.get('team2')

    if not team_1 or not team_2:
        return jsonify({"error": "Please provide both team1 and team2 as query parameters."}), 400

    try:
        response = ipl.team1_vs_team2(team_1, team_2)
        return jsonify(response)
    except KeyError as e:
        return jsonify({
            "error": f"Could not retrieve full statistics for the match-up: {team_1} vs {team_2}. This might be due Incorrect Spelling.",
            "detail": f"Missing data for key: {str(e)}"
        }), 404 
    except Exception as e:
        return jsonify({"error": "An internal server error occurred while processing your request."}), 500
    
if __name__ == '__main__':
    app.run(debug=True)