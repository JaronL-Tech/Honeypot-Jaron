# libraries
import logging
from logging.handlers import RotatingFileHandler


# constants
logging.basicConfig(level=logging.INFO)
logging_format = logging.Formatter('%(message)s')

# loggers & logging files
funnel_logger = logging.getLogger("FunnelLogger")
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audits.log',maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)




# Emulated Shell

# SSH Server + sockets 

# Provisions and SSH based honeypot


