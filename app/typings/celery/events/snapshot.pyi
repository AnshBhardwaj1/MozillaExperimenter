"""
This type stub file was generated by pyright.
"""

"""Periodically store events in a database.

Consuming the events as a stream isn't always suitable
so this module implements a system to take snapshots of the
state of a cluster at regular intervals.  There's a full
implementation of this writing the snapshots to a database
in :mod:`djcelery.snapshots` in the `django-celery` distribution.
"""
__all__ = ("Polaroid", "evcam")
logger = ...

class Polaroid:
    """Record event snapshots."""

    timer = ...
    shutter_signal = ...
    cleanup_signal = ...
    clear_after = ...
    _tref = ...
    _ctref = ...
    def __init__(
        self, state, freq=..., maxrate=..., cleanup_freq=..., timer=..., app=...
    ) -> None: ...
    def install(self): ...
    def on_shutter(self, state): ...
    def on_cleanup(self): ...
    def cleanup(self): ...
    def shutter(self): ...
    def capture(self): ...
    def cancel(self): ...
    def __enter__(self): ...
    def __exit__(self, *exc_info): ...

def evcam(
    camera,
    freq=...,
    maxrate=...,
    loglevel=...,
    logfile=...,
    pidfile=...,
    timer=...,
    app=...,
    **kwargs
):  # -> None:
    """Start snapshot recorder."""
    ...
