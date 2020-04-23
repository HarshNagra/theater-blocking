import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from actors import enrich_script_with_actors
from scripts import (
    get_script_by_id,
    update_script_by_id,
)
from validate import (
    validate_json,
    validate_schema,
)


# Start the app and setup the static directory for the html, css, and js files.
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'Theatre Blocking root route'

### DO NOT modify this example route. ###
@app.route('/example')
def example_block():
    example_script = "O Romeo, Romeo, wherefore art thou Romeo? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love And I’ll no longer be a Capulet."

    # This example block is inside a list - not in a dictionary with keys, which is what
    # we want when sending a JSON object with multiple pieces of data.
    return jsonify([example_script, 0, 41, 4])


''' Modify the routes below accordingly to 
parse the text files and send the correct JSON.'''

## GET route for script and blocking info
@app.route('/script/<int:script_id>')
def script(script_id):
    try:
        script = get_script_by_id(script_id)
        script_with_actor_names = enrich_script_with_actors(script)
        del script_with_actor_names['file']
        return jsonify({
            "scripts": [script_with_actor_names],
        })
    except (Exception, RuntimeError) as e:
        return jsonify({"error": str(e)}), 500


## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/script', methods=['POST'])
@validate_json
@validate_schema('addBlocking')
def addBlocking():
    try:
        script_id = request.json.get("scriptNum")
        parts = request.json.get("parts")
        return jsonify(update_script_by_id(script_id, parts))
    except (Exception, RuntimeError) as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

