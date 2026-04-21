import json

if __name__ == '__main__':
    try:
        with open('path/to/data.json', 'r') as file:
            data = json.loads(file.read())

        people = data["people"]
        output = ','.join([*people[0]])
        for obj in people:
            output += f'\n{obj["firstName"]},{obj["lastName"]},{obj["gender"]},{obj["age"]},{obj["number"]}'

        with open('path/to/output.csv', 'w') as file:
            file.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
