import sys
import os
#import codecs
import requests

def main():
  resp = requests.get('http://en.metal-tracker.com/site/rss.html')
  print('len', len(resp.text))
  print(resp.text[:1000])

#def utf2file(ustr, filepath):
#  with open(filepath, 'w', encoding="utf-8") as text_file:
#    text_file.write(ustr)

#def set_enc():
#  desired_enc = 'utf-8'
#  if sys.stdout.encoding != desired_enc:
#    sys.stdout = codecs.getwriter(desired_enc)(sys.stdout.buffer, 'strict')
#  if sys.stderr.encoding != desired_enc:
#    sys.stderr = codecs.getwriter(desired_enc)(sys.stderr.buffer, 'strict')

if __name__ == '__main__':
#  set_enc()
  main()