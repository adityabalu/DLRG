import argparse
import os
import yaml

def read_yaml_file(filename):
    with open(filename, 'r') as f:
        data = yaml.safe_load(f)
    return data

def create_run_folder(parent_dir):
    version = 1
    while True:
        run_dir = os.path.join(parent_dir, f'run_{version}')
        if not os.path.exists(run_dir):
            os.makedirs(run_dir)
            return run_dir
        version += 1

def write_params_to_file(params, filename):
    with open(filename, 'w') as f:
        yaml.dump(params, f)


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--name', type=str, default='', help='name')
    parser.add_argument('--occupation', type=str, default='', help='occupation')
    parser.add_argument('--ID', type=int, default=0, help='ID')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to YAML configuration file')
    args = parser.parse_args()
    print(args)
    # Read YAML configuration file
    config = read_yaml_file(args.config)

    # Override configuration with command line arguments
    if args.name:
        config['name'] = args.name
    if args.occupation:
        config['occupation'] = args.occupation
    if args.ID:
        config['ID'] = args.ID

    # Create run folder and write parameters to file
    run_dir = create_run_folder('runs')
    params_file = os.path.join(run_dir, 'params.yaml')
    write_params_to_file(config, params_file)


if __name__ == '__main__':
    main()