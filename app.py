import bottle
@bottle.get('/')
def hi():
  return "<h1>Working!</h1>"
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
bottle.run(host='0.0.0.0', port=1234)
