import insightconnect_plugin_runtime
from .schema import ConnectionSchema
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        pass

    def test(self):
        # TODO: Implement connection test
        pass
