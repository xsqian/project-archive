# contain function code (this) and locally imported lib (mylib)
from mylib import myfunc


# mlrun nuclio runtime entry
def nuclio_handler(context, event):
    myfunc()
    return context.Response(body='Hello!',
                            headers={},
                            content_type='text/plain',
                            status_code=200)
