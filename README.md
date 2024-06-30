# Test Combinations Generator

This Python utility generates test case combinations for software testing. It supports two modes: generating all possible combinations and generating pairwise (orthogonal) combinations. The results are saved to a specified CSV file.

## Features

- Generate all possible combinations of parameter values.
- Generate pairwise (orthogonal) combinations of parameter values.
- Save the generated combinations to a CSV file with appropriate headers.

## Requirements

- Python 3.6 or higher
- allpairspy library (added to requirements.txt)
- argparse library (added to requirements.txt)

## Installation

1. Clone this repository or download the script file.
2. Install the required dependencies using `pip` and `requirements.txt`:

```commandline
pip install -r requirements.txt
```

## Usage

Run the script via the terminal with the following options:

```commandLine
python test_combinations.py --mode MODE --params PARAMS --output OUTPUT
```

## Options
--mode: The mode of generation. Choose between all for all combinations and pairwise for pairwise combinations.
--params: List of parameters and their values in the format param1=value1,value2,... param2=value1,value2,....
--output: The output CSV file to save the combinations.

## Examples

Generate all combinations and save to a CSV file:
```commandLine
python test_combinations.py --mode all --params param1=a,b,c param2=1,2,3 --output all_combinations.csv
```
Generate pairwise combinations and save to a CSV file:
```commandline
python test_combinations.py --mode pairwise --params param1=a,b,c param2=1,2,3 --output pairwise_combinations.csv
```
## Example Output

CSV Output for All Combinations:
```csv
param1,param2
a,1
a,2
a,3
b,1
b,2
b,3
c,1
c,2
c,3
```

CSV Output for Pairwise Combinations
```csv
param1,param2
a,1
a,2
b,2
b,3
c,1
c,3
```
## License

This project is licensed under the MIT License.