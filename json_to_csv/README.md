# JSON to CSV Converter

A simple Python script that converts a JSON file containing an array of objects into a CSV file.

## Project Structure

```
json_to_csv/
├── main.py   # Main script
├── data.json        # Sample input file
├── output.csv       # Generated output file
└── README.md
```

## How It Works

The script reads a JSON file, extracts the `people` array, uses the keys of the first object as CSV headers, then writes each person's data as a row in the output CSV.

## Usage

1. Place your JSON file at the input path (default: `path/to/data.json`)
2. Run the script:

```bash
python main.py
```

3. The output CSV will be saved to `path/to/output.csv`

## Input Format

The JSON file should contain a `people` key with an array of objects:

```json
{
  "people": [
    {
      "firstName": "Joe",
      "lastName": "Jackson",
      "gender": "male",
      "age": 28,
      "number": "7349282382"
    }
  ]
}
```

## Output Format

```
firstName,lastName,gender,age,number
Joe,Jackson,male,28,7349282382
```

## Requirements

- Python 3.x
- No external libraries needed (uses built-in `json` module)


