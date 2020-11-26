from libqtile.widget.battery import Battery, BatteryStatus, BatteryState


class CustomBattery(Battery):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    icons = {
        0: u'\uf244',
        1: u'\uf243',
        2: u'\uf242',
        3: u'\uf241',
        4: u'\uf240',
    }


    def build_string(self, status: BatteryStatus) -> str:
        """Determine the string to return for the given battery state

        Parameters
        ----------
        status:
            The current status of the battery

        Returns
        -------
        str
            The string to display for the current status.
        """
        if self.hide_threshold is not None and status.percent > self.hide_threshold:
            return ''

        if self.layout is not None:
            if status.state in [BatteryState.DISCHARGING, BatteryState.UNKNOWN] and status.percent < self.low_percentage:
                self.layout.colour = self.low_foreground
            else:
                self.layout.colour = self.foreground

        hour = status.time // 3600
        minute = (status.time // 60) % 60

        level_index = int(status.percent * 5)
        level_index = min(level_index, 4)

        return CustomBattery.icons[level_index]