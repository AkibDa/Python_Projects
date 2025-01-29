import time
import argparse
import requests

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)

def download_file(url, local_filename):
  if local_filename is None:
   local_filename = url.split('/')[-1]

  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192):
        f.write(chunk)
  return local_filename

parser = argparse.ArgumentParser()

parser.add_argument("url", help="Url of the file to download")
parser.add_argument("-o","--output",help="Name of the file",default=None)

args = parser.parse_args()

print(args.url)
print(args.output)
download_file(args.url, args.outpt)