
class DropletCreationError(Exception):
    def __init__(self):
        super().__init__('Digital Ocean API returned errored')


class FloatingIpAssignmentError(Exception):
    def __init__(self, msg):
        super().__init__('Error on assigning floating ip. Response data is: ' + str(msg))
