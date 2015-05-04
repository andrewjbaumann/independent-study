# indent your Python code to put into an email
import glob
# glob supports Unix style pathname extensions
processed = glob.glob('*.txt')
for file_name in sorted(processed):
    print '    ------' + file_name

    with open(file_name) as f:
        for line in f:
            print '    ' + line.rstrip()

    print