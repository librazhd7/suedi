import json
import urllib.request
import urllib.parse

# https://docs.github.com/en/rest/markdown/markdown
mds = ['https://github.com/librazhd7/suedi/blob/main/src/client/FABRIC.md',
       'https://github.com/librazhd7/suedi/blob/main/src/cross/FABRIC.md',
       'https://github.com/librazhd7/suedi/blob/main/src/server/FABRIC.md']
urllib.request.addheaders = [('Accept', 'application/vnd.github+json'),
                             ('X-GitHub-Api-Version', '2022-11-28')]
with urllib.request.urlopen('https://api.github.com/markdown', json.dumps({'text': urllib.request.urlopen('').read().decode()}).encode('utf-8')) as md:
  print(md.read().decode('utf-8'))

# check for .minecraft path in windows and linux environments.
# create new instance and parse table data from .md/.html.

#json.dumps(md, indent=4)
#md.close()
