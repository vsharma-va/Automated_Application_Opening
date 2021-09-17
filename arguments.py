import argparse


def arguments():
    parser = argparse.ArgumentParser()
    event = parser.add_mutually_exclusive_group()
    event.add_argument('-aenv', '--add_env', help='Add A New Env', action='store_true')
    event.add_argument('-dispenv', '--display_all_envs', help='Display All Created Envs', action='store_true')
    event.add_argument('-rex', '--run_existing', type=str, metavar='', help='Run an existing env')
    event.add_argument('-aenvweb', '--add_env_with_web', type=str, metavar='', nargs='*',
                       help='Add A New Env With Website'
                            ' Type URLs separated by a space')
    event.add_argument('-delaenvs', '--del_all_envs', help='Delete all envs', action='store_true')
    event.add_argument('-del', '--del_env', type=str, metavar='', help='Delete Selected Env')
    args = parser.parse_args()
    return [args.add_env, args.display_all_envs, args.run_existing, args.add_env_with_web, args.del_all_envs
            , args.del_env]
