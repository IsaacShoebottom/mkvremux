import argparse
import os

parser = argparse.ArgumentParser(description='Remux a video file')
parser.add_argument('-d', '--directory', help='Directory to search for files')
parser.add_argument('-v', '--verbose', help='Verbose output', action='store_true')
parser.add_argument('-t', '--test', help='Test run', action='store_true')
parser.add_argument('-r', '--remove', help='Delete original file', action='store_true')
args = parser.parse_args()

if args.verbose:
    print('Verbose:', args.verbose)
    print('Test:', args.test)
    print('Delete:', args.delete)

# Start by making a list of every .mp4 file in current directory and any subdirectories
# Then, for each file, run the remux command with mkvtoolnix
# If verbose, print out the command being run
# If test, print out the command but don't run it

if args.directory:
    os.chdir(args.directory)

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.mp4'):
            print(file)
            path = os.path.join(root, file)
            command = f'mkvmerge -o "{path[:-4]}.mkv" "{path}"'
            if args.verbose:
                print(command)
            if not args.test:
                result = os.system(command)
                if args.remove and result == 0:
                    print(f'Removed {path}')
                    os.remove(path)

