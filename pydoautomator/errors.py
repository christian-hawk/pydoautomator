
class DropletCreationError(Exception):
    def __init__(self):
        super().__init__('Digital Ocean API returned errored')


class FloatingIpAssignmentError(Exception):
    def __init__(self, msg):
        super().__init__('Error on assigning floating ip. Response data is: ' + str(msg))


class TurnoffDropletError(Exception):
    def __init__(self, msg):
        super().__init__('Error shutting down droplet. Response data is: ' + str(msg))


class DestroyDropletError(Exception):
    def __init__(self, msg):
        super().__init__('Error destroying droplet. Response data is: ' + str(msg))
