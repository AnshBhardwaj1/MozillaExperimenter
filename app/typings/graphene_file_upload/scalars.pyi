"""
This type stub file was generated by pyright.
"""

import graphene

"""Scalars

Defines upload scalar for use in defining file-specific interfaces
"""

class Upload(graphene.types.Scalar):
    """Create scalar that ignores normal serialization/deserialization, since
    that will be handled by the multipart request spec"""

    @staticmethod
    def serialize(value): ...
    @staticmethod
    def parse_literal(node): ...
    @staticmethod
    def parse_value(value): ...
