import dbus

class AvahiServer:
    def __init__(self):
        self.bus = dbus.SystemBus()
        raw_server = self.bus.get_object("org.freedesktop.Avahi", "/")
        self.server = dbus.Interface(raw_server, "org.freedesktop.Avahi.Server")

    def GetVersion(self):
        try:
            return self.server.GetVersionString()
        except dbus.DBusException:
            return None

    def GetHostName(self):
        try:
            self.server.GetHostName()
        except dbus.DBusException:
            return None

    def GetDomainName(self):
        try:
            self.server.GetDomainName()
        except dbus.DBusException:
            return None

    def EntryGroupNew(self):
        try:
            self.server.EntryGroupNew()
        except dbus.DBusException:
            return None