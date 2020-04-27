# Outgoing port status
from enum import Enum
PortStatus = Enum('PortStatus', ('Open', 'Firewalled', 'Closed'))