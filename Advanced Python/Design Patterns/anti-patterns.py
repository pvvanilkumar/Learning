#Bad
def filter_for_foo(l):
   r = [e for e in l if e.find("foo") != -1]
   if not check_some_critical_condition(r):
      return None
   return r

res = filter_for_foo(["bar","foo","faz"])

if res is not None:
   #continue processing
   pass

#Good
def filter_for_foo(l):
   r = [e for e in l if e.find("foo") != -1]
   if not check_some_critical_condition(r):
      raise SomeException("critical condition unmet!")
   return r

try:
   res = filter_for_foo(["bar","foo","faz"])
   #continue processing

except SomeException:
   i = 0
while i < 10:
   do_something()
   #we forget to increment i