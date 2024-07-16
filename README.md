Applications that use D-Bus typically connect to a bus daemon, which forwards messages between the applications. To use 
D-Bus, you need to create a ```Bus``` object representing the connection to the bus daemon.

There are generally two bus daemons you may be interested in. Each user login session should have a session bus, 
which is local to that session. It's used to communicate between desktop applications.
Connect to the session bus by creating a ```SessionBus``` object:
```angular2html
from pydbus import SessionBus

session_bus = SessionBus()
```

The _system bus_ is global and usually started during boot; it's used to communicate with system services like **systemd**, 
**udev** and **NetworkManager**. To connect to the system bus, create a ```SystemBus``` object:

```angular2html
from pydbus import SystemBus

system_bus = SystemBus()
```
Of course, you can connect to both in the same application.

D-Bus applications can export objects for other applications' use. To start working with an object in another application, 
you need to know two things:

* bus name: This identifies which application you want to communicate with. You'll usually identify applications by a 
well-known name, which is a dot-separated string starting with a reversed domain name, such as ```org.freedesktop.NetworkManager``` or
```com.example.WordProcessor```. 
* object path: Applications can export many objects - for instance, example.com's word processor might provide an object 
representing the word processor application itself and an object for each document window opened, or it might also 
provide an object for each paragraph within a document.

To identify which one you want to interact with, you use an object path, a slash-separated string resembling a filename. 
For instance, example.com's word processor might provide an object at ```/``` representing the word processor itself, 
and objects at ```/documents/123``` and ```/documents/345``` representing opened document windows. All objects have methods, 
properties and signals.

To handle signals emitted by exported objects, or to export your own objects, you need to setup an event loop. 
The only main loop supported by ```pydbus``` is ```GLib.MainLoop```. 
```angular2html
from gi.repository import GLib

loop = GLib.MainLoop()

loop.run() # to execute the loop
```
While ```loop.run()``` is executing, GLib will watch for signals you're subscribed to, or accesses to objects you exported, 
and execute correct callbacks when appropriate. To stop, call ```loop.quit()```.

To interact with a remote object, you use a **proxy object**. This is a Python object which acts as a proxy or "stand-in" 
for the remote object - when you call a method on a proxy object, this causes dbus-python to make a method call on the 
remote object, passing back any return values from the remote object's method as the return values of the proxy method call.

To obtain a proxy object, call the ```get``` method on the ```Bus```. For example, _NetworkManager_ has the well-known 
name ```org.freedesktop.NetworkManager``` and exports an object whose object path is ```/org/freedesktop/NetworkManager```, 
plus an object per network interface at object paths like ```/org/freedesktop/NetworkManager/Devices/eth0```. You can 
get a proxy for the object representing eth0 like this:
```angular2html
from pydbus import SystemBus

bus = SystemBus()

proxy = bus.get('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager/Devices/0')
```
pydbus has implemented shortcuts for the most common cases. If you start the bus name with "." (".NetworkManager"), 
"org.freedesktop" will become automatically prepended. If you specify a relative object path (without the leading "/"), 
the bus name transformed to a path format will get prepended ("/org/freedesktop/NetworkManager/"). If you don't specify 
the object path at all, the transformed bus name will be used automatically ("/org/freedesktop/NetworkManager"). 
Therefore, you may rewrite the above code as:
```angular2html
from pydbus import SystemBus
bus = SystemBus()
dev = bus.get('.NetworkManager', 'Devices/0')
```
D-Bus uses interfaces to provide a namespacing mechanism for methods, signals and properties. An interface is a group of
related methods, signals and properties, identified by a name which is a series of dot-separated components starting with 
a reversed domain name. For instance, each NetworkManager object representing a network interface implements the interface
```org.freedesktop.NetworkManager.Device```.


credit: Linus Lewandowski