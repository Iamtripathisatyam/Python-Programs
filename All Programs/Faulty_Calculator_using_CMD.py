import argparse
import sys
def calc(args):

    if args.a == 45 and args.b == 3 and args.c == 'mul':
        return 555
    elif args.a == 56 and args.b == 9 and args.c == 'add':
        return 77
    elif args.a == 56 and args.b == 6 and args.c == 'div':
        return 4
    elif args.c == 'add':
        return args.a + args.b
    elif args.c == 'sub':
        return args.a - args.b
    elif args.c == 'mul':
        return args.a * args.b
    elif args.c == 'div':
        return args.a / args.b
    elif args.c == 'per':
        return args.a % args.b
    else:
        print("Warning !! Something went wrong !!")



# if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--a', type=float,
                    default=0,
                    help="Please Contact to Satyam Tripathi")
parser.add_argument('--b', type=float,
                    default=0,
                    help="Please Contact to Satyam Tripathi")
parser.add_argument('--c', type= str,
                    default = 'add',
                    help="Please Contact to Satyam Tripathi")

args  = parser.parse_args()
sys.stdout.write(str(calc(args)))


