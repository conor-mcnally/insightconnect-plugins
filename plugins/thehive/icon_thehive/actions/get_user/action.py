import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Component

# Custom imports below
import requests


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        client = self.connection.client
        user_id = params.get(Input.ID)

        if user_id:
            url = f"{client.url}/api/user/{user_id}"
        else:
            url = f"{client.url}/api/user/current"

        try:
            user = requests.get(
                url,
                auth=(self.connection.username, self.connection.password),
                verify=self.connection.verify,
            )
            user.raise_for_status()
        except requests.exceptions.HTTPError:
            self.logger.error(user.json())
            raise
        except:
            self.logger.error("Failed to get user")
            raise

        return user.json()
