# import multiprocessing.process
import requests
import concurrent.futures

def downloadFile(url, name):
  print(f"Started downloading {name}")

  response = requests.get(url)
  open(f"{name}.jpg","wb").write(response.content)
  
  print(f"Finished downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []

# for i in range(50):
#   # downloadFile(url, i)

#   p = multiprocessing.process(target=downloadFile, args=[url, i])
#   p.start()
#   pros.append(p)

# for p in pros:
#   p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(51)]
  l2 = [i for i in range(51)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
    print(r)