import glob 


def get_script_file_names():
    return glob.glob("app/script_data/*.txt")


def parse_positions_data(positions_arr):
    parsed = []
    for position_data in positions_arr:
        name, position = position_data.split('-')
        parsed.append({
            "name": name.strip(),
            "position": int(position)
        })
    return parsed 


def parse_blocking_data(blocking_data_str):
    part, content = blocking_data_str.split('.') 
    start, end, *positions = content.split(',') 
    return {
        "part": int(part),
        "startChar": int(start), 
        "endChar": int(end),
        "positions": parse_positions_data(positions) 
    }


def parse_script_file(file_name):
    blocking_data = []

    with open(file_name, 'rt') as f:
        # First line contains script id
        script_id = f.readline()
        # Garbage second line
        f.readline()
        # Third line contains script verse
        script_text = f.readline()
        # Garbage fourth line
        f.readline()
        # Remaining lines contain blocking data
        for blocking_data_str in iter(lambda: f.readline(), ''):
            blocking_data.append(
                parse_blocking_data(blocking_data_str)
            )

    return {
        "id": int(script_id),
        "text": script_text.strip(),
        "blocking": blocking_data,
        "file": file_name, #TODO should serialize/remove this
    }


def parse_script_data():
    scripts = []
    text_files = get_script_file_names()
    for file_name in text_files:
        scripts.append(parse_script_file(file_name))
    return scripts


def update_and_serialize_blocking(new_positions, existing_blockings):
    blocking_strings = []
    for new_position in new_positions:
        part_id = new_position["part"]

        existing_blocking = next((
            existing_blocking 
            for existing_blocking in existing_blockings
            if existing_blocking['part'] == part_id
        ), None)
        
        start = existing_blocking['startChar']
        end = existing_blocking['endChar']
        blocking_string = f"{part_id}. {start}, {end}"

        for blocking_data in new_position["blocking"]:
            blocking_string += f", {blocking_data['name']}-{blocking_data['position']}" 
            
        blocking_string += '\n'
        blocking_strings.append(blocking_string)

    return blocking_strings


def get_script_by_id(script_id):
    scripts = parse_script_data()
    return next((
        script 
        for script in scripts
        if script['id'] == script_id
    ), {})


def update_script_by_id(script_id, positions):
    script = get_script_by_id(script_id)
    file_name = script["file"]
    blocking_strings = update_and_serialize_blocking(
        new_positions=positions,
        existing_blockings=script['blocking']
    )

    with open(file_name, "w") as f:
        f.writelines([
            f"{script_id}\n",
            "\n",
            f"{script.get('text')}\n",
            "\n",
            *blocking_strings,
        ])