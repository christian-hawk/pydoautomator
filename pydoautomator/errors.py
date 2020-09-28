
class DropletCreationError(Exception):
    def __init__(self):
        super().__init__('Digital Ocean API returned errored')
