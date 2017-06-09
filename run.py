from controllers import app
# from OpenSSL import SSL
import start_up

start_up.start_up(app)
# context = ('server.crt', 'server.key')
# app.run(debug=True, host='0.0.0.0', port=5566, threaded=True, ssl_context=context)
# app.run(debug=True, host='0.0.0.0', port=5566, processes=10, ssl_context=context)
app.run(debug=True, host='0.0.0.0', port=5566, processes=10)
