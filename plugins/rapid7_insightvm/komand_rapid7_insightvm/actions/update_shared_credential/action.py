import insightconnect_plugin_runtime
from .schema import UpdateSharedCredentialInput, UpdateSharedCredentialOutput, Input, Output, Component
# Custom imports below


class UpdateSharedCredential(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_shared_credential',
                description=Component.DESCRIPTION,
                input=UpdateSharedCredentialInput(),
                output=UpdateSharedCredentialOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
