import re
import asyncio

pattern = r"failures"

text = '''The intricacies of distributed systems always fascinated me.  Imagine orchestrating hundreds of machines, each a cog in a larger computational engine. The challenges are immense ensuring data consistency, managing network latency, and handling inevitable hardware failures. Yet, the potential rewards are equally significant: scalable applications that can handle millions of users, complex simulations that model real-world phenomena, and the power to analyze massive datasets. It's a constant learning process, diving into new architectures, exploring different consensus algorithms, and grappling with the trade-offs between performance and reliability. But that's what makes it so exciting the constant push to innovate and build systems that are more robust, more efficient, and ultimately, more impactful.'''

match = re.search(pattern, text)

if match:
  print("Match found! ")
else:
  print("Not found. ")

async def my_async_function():
  await asyncio.sleep(1)
  return "Hello, Async World!"

async def main():
  result = await my_async_function()
  print(result)

asyncio.run(main())

async def function1():
  await asyncio.sleep(1)
  print("func1")
  return "Akib"

async def function2():
  await asyncio.sleep(2)
  print("func2")
  return "Akib Da"

async def function3():
  await asyncio.sleep(3)
  print("func3")
  return "Alom Da"

async def main():
  L = await asyncio.gather(
    function1(),
    function2(),
    function3(),
  )
  print(L)

asyncio.run(main())