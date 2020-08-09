# -*- coding: utf-8 -*-
"""Shared Folders data."""
from synology_dsm.helpers import SynoFormatHelper


class SynoCoreShareSnapshot(object):
    """Class containing Share data."""

    API_KEY = "SYNO.Core.Share.Snapshot"
    # Syno supports two methods to retrieve resource details, GET and POST.
    # GET returns a limited set of keys. With POST the same keys as GET
    # are returned plus any keys listed in the "additional" parameter.
    # NOTE: The value of the additional key must be a string.
    REQUEST_DATA = {
        "additional": '["desc","lock","schedule_snapshot"]'
    }

    def __init__(self, dsm):
        self._dsm = dsm
        self._data = {}

    def update(self):
        """Updates share data."""
        raw_data = self._dsm.post(self.API_KEY, "list", data=self.REQUEST_DATA)
        if raw_data:
            self._data = raw_data["data"]

    @property
    def snapshots(self):
        """Gets all snapshots for a share."""
        return self._data.get("snapshots", [])

    @property
    def snapshots_desc(self):
        """Return snapshots descriptions"""
        # The snapshot description is analogous to a snapshot name
        snapshots = []
        for snapshot in self.snapshots:
            snapshots.append(snapshot["desc"])
        return snapshots

    def get_share(self, share_desc):
        """Returns a specific snapshot by description"""
        for snapshot in self.snapshot:
            if snapshot["desc"] == share_desc:
                return snapshot
        return {}