from .droplet import Droplet
from .automator import Automator

# creates version from metadata
try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
