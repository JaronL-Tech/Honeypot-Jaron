# libraries
import logging
from logging.handlers import RotatingFileHandler
import socket


# constants
logging.basicConfig(level=logging.INFO)
logging_format = logging.Formatter('%(message)s')

# loggers & logging files
funnel_logger = logging.getLogger("FunnelLogger")
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audits.log',maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)


creds_logger = logging.getLogger("CredsLogger")
creds_logger.setLevel(logging.INFO)
creds_handler = RotatingFileHandler('cmd_audits.log',maxBytes=2000, backupCount=5)
creds_handler.setFormatter(logging_format)
creds_logger.addHandler(creds_handler)



# Emulated Shell
def emulate_shell(channel, client_ip):
    channel.send(b'corporate-jumbbox2$')
    command = b""
    while True:
        char = channel.recv(1)
        channel.send(char)
        if not char:
            channel.close()


        command += char

        if char == b'\r':
            if command.strip() == b'exit':
                response = b'\n Goodbye!\n'
                channel.close()

            elif command.strip() == b'pwd':
                response = b'\n\\usr\local\\' + b'\r\n'


        channel.send(response)
        channel.send('corporate-jumbbox2$')
        command = b""

# SSH Server + sockets 

# Provisions and SSH based honeypot


