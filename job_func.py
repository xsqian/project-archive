# test loading repo from git in different mlrun runtimes
# contain function code (this) and locally imported lib (mylib)

from mylib import myfunc

# mlrun job runtime entry
def job_handler(context):
  myfunc()
  context.log_result("out", 5)
