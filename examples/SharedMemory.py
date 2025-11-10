""" This example is taken from the Ephys-Live Project
"""

from BaseSharedMemory import BaseSharedMemoryDict
from BaseConfigs import BaseConfigs


class Config(BaseConfigs):
    app_name = "ScottsPyQtTemplate"
    preferences_fp = "preferences.yaml"

    default_preferences = {
        "isIntanDevice": False,
        "intanDevice": {
            "ipaddr": "127.0.0.1",
            "port_command": 5000,
            "port_waveform": 5001,
            "port_spike": 5001
        }
    }


class SharedMemoryDict(BaseSharedMemoryDict):
    
    @property
    def intanDevice_ipaddr(self):
        ret = self.__intanDevice.get("ipaddr", None)
        if not ret:
            self._preferences["ipaddr"] = self._configs.default_preferences["ipaddr"]
            self.write_preferences()
        return ret

    @property
    def intanDevice_portCmd(self):
        ret = self.__intanDevice.get("port_command", None)
        if not ret:
            self._preferences["port_command"] = self._configs.default_preferences["port_command"]
            self.write_preferences()
        return ret

    @property
    def intanDevice_portWaveform(self):
        ret = self.__intanDevice.get("port_waveform", None)
        if not ret:
            self._preferences["port_waveform"] = self._configs.default_preferences["port_waveform"]
            self.write_preferences()
        return ret

    @property
    def intanDevice_portSpike(self):
        ret = self.__intanDevice.get("port_spike", None)
        if not ret:
            self._preferences["port_spike"] = self._configs.default_preferences["port_spike"]
            self.write_preferences()
        return ret
    
    @property
    def __intanDevice(self):
        ret = self._preferences.get("intanDevice", None)
        if not ret:
            self._preferences["intanDevice"] = self._configs.default_preferences["intanDevice"]
            self.write_preferences()
        return ret

    @property
    def isIntanDevice(self):
        ret = self._preferences.get("isIntanDevice", None)
        if not ret:
            self._preferences["isIntanDevice"] = self._configs.default_preferences["isIntanDevice"]
            self.write_preferences()
        return ret
    

sharedMemoryDict = SharedMemoryDict(Config)
