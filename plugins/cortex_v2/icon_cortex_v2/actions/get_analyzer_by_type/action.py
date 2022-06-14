import insightconnect_plugin_runtime
from .schema import GetAnalyzerByTypeInput, GetAnalyzerByTypeOutput, Input, Output, Component

# Custom imports below
from icon_cortex_v2.util.convert import analyzers_to_dicts
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError, CortexException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class GetAnalyzerByType(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_analyzer_by_type",
            description=Component.DESCRIPTION,
            input=GetAnalyzerByTypeInput(),
            output=GetAnalyzerByTypeOutput(),
        )

    def run(self, params={}):
        try:
            analyzers = self.connection.api.analyzers.get_by_type(params.get(Input.TYPE))

        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        except CortexException as e:
            raise ConnectionTestException(cause="Failed to get analyzers.", assistance=f"{e}.")

        return {Output.LIST: analyzers_to_dicts(analyzers)}