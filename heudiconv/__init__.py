# set logger handler
import logging
import os
from .info import __packagename__
from ._version import __version__

# Rudimentary logging support.
lgr = logging.getLogger(__name__)
logging.basicConfig(
    format='%(levelname)s: %(message)s',
    level=getattr(logging, os.environ.get('HEUDICONV_LOG_LEVEL', 'INFO'))
)
lgr.debug("Starting the abomination")  # just to "run-test" logging
