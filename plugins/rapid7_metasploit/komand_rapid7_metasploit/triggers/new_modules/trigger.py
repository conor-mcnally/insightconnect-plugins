import insightconnect_plugin_runtime
import time
from .schema import NewModulesInput, NewModulesOutput

# Custom imports below
import requests


class NewModules(insightconnect_plugin_runtime.Trigger):
    CACHE_FILE_NAME = "metasploit_modules"
    cache_file = None
    _META_JSON = "https://github.com/rapid7/metasploit-framework/raw/master/db/modules_metadata_base.json"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="new_modules",
            description="Checks for new Metasploit modules",
            input=NewModulesInput(),
            output=NewModulesOutput(),
        )

    def run(self, params={}):
        """Run the trigger"""
        # Open and auto-close the file to create the cache file on very first start up
        with insightconnect_plugin_runtime.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            self.logger.debug(f"Run: Got or created cache file: {cache_file}")

        while True:
            metasploit_data = []
            # Create update Metasploit JSON
            try:
                resp = requests.get(self._META_JSON)
                metasploit_json = resp.json()
                for meta_module in metasploit_json:
                    metasploit_data.append(metasploit_json[meta_module])
            except Exception as e:
                self.logger.error("An error occurred while accessing Metasploit information: ", e)
                raise
            # Check to see if module has been cached if not send module
            for module in metasploit_data:
                with insightconnect_plugin_runtime.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                    contents = cache_file.readlines()
                    contents = [x.strip() for x in contents]
                    if module["fullname"] not in contents:
                        cache_file.write(module["fullname"] + "\n")
                        self.send({"module": insightconnect_plugin_runtime.helper.clean(module)})
            time.sleep(params.get("interval", 60))

    def test(self):
        # Test and build cache file
        with insightconnect_plugin_runtime.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
            self.logger.debug(f"Run: Got or created cache file: {cache_file}")
        metasploit_data = []
        # Create update Metasploit JSON
        try:
            resp = requests.get(self._META_JSON)
            metasploit_json = resp.json()
            for meta_module in metasploit_json:
                metasploit_data.append(metasploit_json[meta_module])
        except Exception as e:
            self.logger.error("An error occurred while accessing Metasploit information: ", e)
            raise

        for module in metasploit_data:
            with insightconnect_plugin_runtime.helper.open_cachefile(self.CACHE_FILE_NAME) as cache_file:
                contents = cache_file.readlines()
                contents = [x.strip() for x in contents]
                if module["fullname"] not in contents:
                    cache_file.write(module["fullname"] + "\n")
        return {"success": "true"}
