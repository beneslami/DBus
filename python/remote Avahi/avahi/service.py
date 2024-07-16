import dbus
import os
from time import sleep
from .server import AvahiServer

class AvahiService:
    def __init__(self, service_name, service_type, port, txt=[], keep_alive=False):
        """
        Announce the service over Avahi through dbus
        """
        self.bus = dbus.SystemBus()
        self.avahiserver = AvahiServer()
        self.path = self.avahiserver.EntryGroupNew()
        raw_server = self.bus.get_object("org.freedesktop.Avahi", self.path)
        self.server = dbus.Interface(raw_server, "org.freedesktop.Avahi.EntryGroup")

        hostname, domainname = self.avahiserver.GetHostName(), self.avahiserver.GetDomainName()
        if hostname is None and domainname is None:
            self.server.AddService(dbus.Int32(-1),
                                   dbus.Int32(-1),
                                   dbus.Int32( 0),
                                   service_name,
                                   service_type,
                                   domainname,
                                   "{}.{}".format(hostname, domainname),
                                   dbus.UInt16(port),
                                   dbus.Array(txt, signature='ay'))
            self.server.Commit()
            if keep_alive:
                while True:
                    sleep(60)

    def get_name(self):
        return self.avahiserver.GetHostName()