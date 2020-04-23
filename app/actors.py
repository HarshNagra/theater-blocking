import csv


def parse_actors():
    with open('app/actors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        actors = []
        for row in csv_reader:
            actors.append({
                "id": row[0],
                "name": row[1]           
            })
        return actors


def get_actor_by_name(actor_name, actors=parse_actors()):
    return next((
        actor 
        for actor in actors
        if actor.get('name') == actor_name
    ), {})


def enrich_script_with_actors(script):
    actors = parse_actors()
    for blocking in script.get('blocking'):
        for position in blocking.get('positions'):
            actor_name = position.get('name')
            position['id'] = get_actor_by_name(
                actor_name,
                actors,
            ).get('id')
    return script