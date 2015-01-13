## L4 - P7 - Q1

def foo(x):
   def bar(x):
      return x + 1
   return bar(x * 2)

print(foo(3))
