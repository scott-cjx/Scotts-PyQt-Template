from appdata import AppDataPaths
import yaml
import os

from BaseConfigs import BaseConfigs


class BaseSharedMemoryDict:
    __doc__ = \
    """ BaseSharedMemoryDict and/or its inherited subclasses must be instantiated in a module of its own in its
    respective project. This allows for the project itself to have sharedMemory. This sharedMemory instance should 
    also be passed into the BaseWidget (if in use)
    """

    _configs = None
    _preferences_fp: str
    _preferences: dict = {}

    def __init__(self, configs: BaseConfigs = BaseConfigs) -> None:
        self._configs = configs
        self._init_preferences()
    
    @property
    def appData_dir(self):
        ret = AppDataPaths(self._configs.app_name).app_data_path
        os.makedirs(ret, exist_ok=True)
        print("Preference File: " + ret)
        return ret
    
    def _init_preferences(self):
        self._preferences_fp = os.path.join(self.appData_dir, self._configs.preferences_fp)

        if os.path.exists(self._preferences_fp):
            self._preferences = self.read_preferences()

        if not self._preferences:
            self._preferences = self._configs.default_preferences
            self.write_preferences()

    def read_preferences(self):
        with open(self._preferences_fp, "r") as f:
            self._preferences = yaml.safe_load(f)
        return self._preferences
    
    def write_preferences(self):
        with open(self._preferences_fp, "w") as f:
            yaml.safe_dump(self._preferences, f)

    @property
    def someProperty(self):
        ret = self._preferences.get("someProperty", None)
        if not ret:
            self._preferences["someProperty"] = self._configs.default_preferences["someProperty"]
            self.write_preferences()
        return ret

baseSharedMemoryDict = BaseSharedMemoryDict()
