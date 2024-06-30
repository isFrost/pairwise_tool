import itertools
import argparse
import csv
from allpairspy import AllPairs


def generate_all_combinations(params):
    return list(itertools.product(*params.values()))


def generate_pairwise_combinations(params):
    param_values = list(params.values())
    return list(AllPairs(param_values))


def save_to_csv(combinations, headers, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)    # CSV writer
        writer.writerow(headers)    # Header
        writer.writerows(combinations)    # Lines


def main():
    parser = argparse.ArgumentParser(description='Generate combinations for testing.')
    parser.add_argument('--mode', choices=['all', 'pairwise'], required=True,
                        help='Mode of generation: "all" for all combinations, "pairwise" for pairwise combinations.')
    parser.add_argument('--params', nargs='+', required=True, type=str,
                        help='List of parameters and their values in the format "param1=value1,value2,'
                             '... param2=value1,value2,..."')
    parser.add_argument('--output', required=True, type=str,
                        help='Output CSV file to save the combinations.')

    args = parser.parse_args()

    # Parse the parameters into a dictionary
    param_dict = {param.split('=')[0]: param.split('=')[1].split(',') for param in args.params}
    headers = list(param_dict.keys())

    combinations = None
    if args.mode == 'all':
        combinations = generate_all_combinations(param_dict)
    elif args.mode == 'pairwise':
        combinations = generate_pairwise_combinations(param_dict)

    save_to_csv(combinations, headers, args.output)
    print(f"Combinations saved to {args.output}")


if __name__ == '__main__':
    main()
