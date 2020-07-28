"""Common get functions for log"""

# Python
import re
import logging
from datetime import datetime

# Genie
from genie.utils.timeout import Timeout
from genie.libs.sdk.libs.utils.normalize import GroupKeys
from genie.metaparser.util.exceptions import SchemaEmptyParserError

log = logging.getLogger(__name__)

def get_log_message_time(device, message):
    """ Gets the timestamp of a log message

    Args:
        device (obj): Device object
        message (str): Message

    Returns:
        (datetime): Timestamp object
    """

    try:
        out = device.parse('show log messages')
    except SchemaEmptyParserError:
        return None

    messages_ = out.q.contains('.*{}.*'.format(message), regex=True)
    
    if not messages_:
        return None

    return datetime.strptime(messages_[0][1].split(' ')[2], '%H:%M:%S')

