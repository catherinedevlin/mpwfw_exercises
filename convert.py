# coding=utf-8

from BeautifulSoup import *
import sys
import re
import glob

corePatt = re.compile(r'chance(.*?)</button>', re.DOTALL)
hintPatt = re.compile(r'Hint: <pre>(.*?)</pre>', re.DOTALL)
nobuttons = re.compile(r'<button.*?&lt;p&gt', re.DOTALL)

def convert_file(fname):
    with open(fname) as infile:
        content = infile.read()
    soup = BeautifulSoup(content)
    chunk = corePatt.search(str(soup.body)).group(1)
    chunk = str(chunk).split('Show Hint')[0]
    chunk = nobuttons.sub('', chunk)
    chunk = chunk.replace(r'<br />', r'<br />&nbsp;&nbsp;&nbsp;&nbsp; &gt;&gt;&gt; ')
    chunk = chunk.replace('→', r'<br />&nbsp;&nbsp;&nbsp;&nbsp;')
    chunk = chunk.replace(r'<p>Hint', r'<p>Hints:<br /><br />&lt;ul style="color:white"&gt;<br />&lt;li&gt;')
    chunk = chunk.replace(r'&lt;pre&gt;%0a#1:', r'&lt;ul style="color:white"&gt;<br />&lt;ul&gt;')
    return chunk
    
for fpatt in sys.argv[1:]:
    for fname in glob.glob(fpatt):
        print(convert_file(fname))
    
    
    
