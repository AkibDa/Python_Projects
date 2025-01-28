import os 

files = os.listdir("clutteredFolder")

i = 1
j = 1
k = 1

for file in files:

  if file.endswith(".png"):

    print(file)

    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")

    i = i + 1

  elif file.endswith(".pdf"):

    print(file)

    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{j}.pdf")

    j = j + 1

  else:

    print(file)

    os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{k}.txt")

    k = k = 1