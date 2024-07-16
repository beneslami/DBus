from pydbus import SystemBus
from pprint import pprint


def get_connection_details(connection_path, bus):
    interface_active_connection = "org.freedesktop.NetworkManager"
    connection_proxy = bus.get(interface_active_connection, connection_path)
    details = {
        "ID": connection_proxy.Id,
        "UUID": connection_proxy.Uuid,
        "Type": connection_proxy.Type,
        "Devices": connection_proxy.Devices,
        "State": connection_proxy.State,
        "State Flags": connection_proxy.StateFlags,
        "Connection": connection_proxy.Connection,
        "Specific Object": connection_proxy.SpecificObject,
    }
    return details


if __name__ == '__main__':
    bus = SystemBus()
    interface_netman = "org.freedesktop.NetworkManager"
    network_manager_proxy = bus.get(interface_netman)
    active_connections = network_manager_proxy.ActiveConnections
    print("Active Connections:")
    for conn_path in active_connections:
        details = get_connection_details(conn_path, bus)
        pprint(details)
        print("\n")