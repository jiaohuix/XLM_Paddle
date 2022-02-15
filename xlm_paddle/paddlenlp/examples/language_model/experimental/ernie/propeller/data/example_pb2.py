# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: propeller/data/example.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

from propeller.data import feature_pb2 as propeller_dot_data_dot_feature__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name='propeller/data/example.proto',
    package='propeller',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b(
        '\n\x1cpropeller/data/example.proto\x12\tpropeller\x1a\x1cpropeller/data/feature.proto\"0\n\x07\x45xample\x12%\n\x08\x66\x65\x61tures\x18\x01 \x01(\x0b\x32\x13.propeller.Features\"g\n\x0fSequenceExample\x12$\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x13.propeller.Features\x12.\n\rfeature_lists\x18\x02 \x01(\x0b\x32\x17.propeller.FeatureListsb\x06proto3'
    ),
    dependencies=[propeller_dot_data_dot_feature__pb2.DESCRIPTOR, ])

_EXAMPLE = _descriptor.Descriptor(
    name='Example',
    full_name='propeller.Example',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='features',
            full_name='propeller.Example.features',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=73,
    serialized_end=121, )

_SEQUENCEEXAMPLE = _descriptor.Descriptor(
    name='SequenceExample',
    full_name='propeller.SequenceExample',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='context',
            full_name='propeller.SequenceExample.context',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='feature_lists',
            full_name='propeller.SequenceExample.feature_lists',
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=123,
    serialized_end=226, )

_EXAMPLE.fields_by_name[
    'features'].message_type = propeller_dot_data_dot_feature__pb2._FEATURES
_SEQUENCEEXAMPLE.fields_by_name[
    'context'].message_type = propeller_dot_data_dot_feature__pb2._FEATURES
_SEQUENCEEXAMPLE.fields_by_name[
    'feature_lists'].message_type = propeller_dot_data_dot_feature__pb2._FEATURELISTS
DESCRIPTOR.message_types_by_name['Example'] = _EXAMPLE
DESCRIPTOR.message_types_by_name['SequenceExample'] = _SEQUENCEEXAMPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Example = _reflection.GeneratedProtocolMessageType(
    'Example',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_EXAMPLE,
        __module__='propeller.data.example_pb2'
        # @@protoc_insertion_point(class_scope:propeller.Example)
    ))
_sym_db.RegisterMessage(Example)

SequenceExample = _reflection.GeneratedProtocolMessageType(
    'SequenceExample',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_SEQUENCEEXAMPLE,
        __module__='propeller.data.example_pb2'
        # @@protoc_insertion_point(class_scope:propeller.SequenceExample)
    ))
_sym_db.RegisterMessage(SequenceExample)

# @@protoc_insertion_point(module_scope)
