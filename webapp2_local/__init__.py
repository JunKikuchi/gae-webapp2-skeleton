import webapp2

def custom_dispatcher(router, request, response):
  rv = router.default_dispatcher(request, response)
  if isinstance(rv, basestring):
    rv = webapp2.Response(rv)
  elif isinstance(rv, tuple):
    rv = webapp2.Response(*rv)
  return rv
