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
