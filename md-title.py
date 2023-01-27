import re, sys


# get filename from command line
filename = sys.argv[1]
# open file
with open(filename, 'r') as f:
    # read file
    content = f.read()
    # match markdown title # Title
    match = re.search(r'^#\s+(.*)\s*$', content, re.MULTILINE)
    # match markdown title ========= content
    if (not match):
        match = re.search(r'^=+\s*$', content, re.MULTILINE)
        if (match):
            # get title from previous line
            match = re.search(r'^(.*)\s*$', content[:match.start()], re.MULTILINE)
    # match markdown title ------------ content
    if (not match):
        match = re.search(r'^-+\s*$', content, re.MULTILINE)
        if (match):
            # get title from previous line
            match = re.search(r'^(.*)\s*$', content[:match.start()], re.MULTILINE)
    if (match):
        # print title
        print(match.group(1))
    else:
        # output to stderr
        sys.stderr.write('No title found in ' + filename + '\n')
