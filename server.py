from bottle import get, post, request, route, run, template

@get('/lighting')
def lighting():
	return '''
		<form action="/lighting" method="post">
			Lighting Start Time: <input name="lighting_start" type="text" />
			Photoperiod: <input name="photoperiod" type="text" />
			<input value="Submit" type="submit" />
		</form>
	'''

@post('/lighting')
def do_lighting():
	lighting_start = int(request.forms.get('lighting_start'))
	photoperiod = int(request.forms.get('photoperiod'))

	if lighting_start < 24 and lighting_start >= 0 and photoperiod > 0:
		return "<p>Lighting Adjust Success</p>"
	else:
		return "<p>Lighting Adjust Failed</p>"

	return "<p>Lighting Start: %i</p>\n<p>Photoperiod: %i</p>" % lighting_start, photoperiod


run(host='0.0.0.0', port=8080, debug=True)
