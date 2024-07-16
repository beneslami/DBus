This is a very simple project to remotely ask the device's avahi name. 

it basically send a HTTP request to the device. The device renders the request and ask dbus for avahi's hostname. Then 
dbus sends back the response to the client over HTTP.