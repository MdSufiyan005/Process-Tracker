import time
import psutil
import socket
from logger import log_event
from config import seen_connections, running
from input_buffer_manager import flush_input_buffer

def get_domain_from_ip(ip):
    """Resolve the domain name for a given IP, if possible."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return "Unknown"

def monitor_network():
    """Continuously monitor network connections and log new ones.
    
    Flush the input buffer when a new network event is logged.
    """
    global running
    while running:
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == 'ESTABLISHED' and conn.raddr:
                remote_ip = conn.raddr.ip
                local_ip = conn.laddr.ip
                pid = conn.pid
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    process_name = "Unknown"
                if remote_ip not in seen_connections:
                    # Flush buffered input events if a new network connection is detected
                    flush_input_buffer()
                    domain = get_domain_from_ip(remote_ip)
                    description = f"Process '{process_name}' connected to {remote_ip} ({domain})"
                    log_event(['Network Activity', process_name, "", str(pid), local_ip, remote_ip, "Monitored", description])
                    seen_connections.add(remote_ip)
        time.sleep(2)
