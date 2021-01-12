# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mouse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mouse.proto',
  package='mouseSenderPackage',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bmouse.proto\x12\x12mouseSenderPackage\"\x06\n\x04void\"!\n\x0b\x45ventString\x12\x12\n\nmouseevent\x18\x01 \x01(\t\">\n\x06\x45vents\x12\x34\n\x0b\x65ventstring\x18\x01 \x03(\x0b\x32\x1f.mouseSenderPackage.EventString2\xae\x01\n\x0bMouseSender\x12Q\n\x0bmouseStream\x12\x1f.mouseSenderPackage.EventString\x1a\x1f.mouseSenderPackage.EventString0\x01\x12L\n\x08sayHello\x12\x1f.mouseSenderPackage.EventString\x1a\x1f.mouseSenderPackage.EventStringb\x06proto3'
)




_VOID = _descriptor.Descriptor(
  name='void',
  full_name='mouseSenderPackage.void',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=41,
)


_EVENTSTRING = _descriptor.Descriptor(
  name='EventString',
  full_name='mouseSenderPackage.EventString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mouseevent', full_name='mouseSenderPackage.EventString.mouseevent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=76,
)


_EVENTS = _descriptor.Descriptor(
  name='Events',
  full_name='mouseSenderPackage.Events',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventstring', full_name='mouseSenderPackage.Events.eventstring', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=140,
)

_EVENTS.fields_by_name['eventstring'].message_type = _EVENTSTRING
DESCRIPTOR.message_types_by_name['void'] = _VOID
DESCRIPTOR.message_types_by_name['EventString'] = _EVENTSTRING
DESCRIPTOR.message_types_by_name['Events'] = _EVENTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

void = _reflection.GeneratedProtocolMessageType('void', (_message.Message,), {
  'DESCRIPTOR' : _VOID,
  '__module__' : 'mouse_pb2'
  # @@protoc_insertion_point(class_scope:mouseSenderPackage.void)
  })
_sym_db.RegisterMessage(void)

EventString = _reflection.GeneratedProtocolMessageType('EventString', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSTRING,
  '__module__' : 'mouse_pb2'
  # @@protoc_insertion_point(class_scope:mouseSenderPackage.EventString)
  })
_sym_db.RegisterMessage(EventString)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {
  'DESCRIPTOR' : _EVENTS,
  '__module__' : 'mouse_pb2'
  # @@protoc_insertion_point(class_scope:mouseSenderPackage.Events)
  })
_sym_db.RegisterMessage(Events)



_MOUSESENDER = _descriptor.ServiceDescriptor(
  name='MouseSender',
  full_name='mouseSenderPackage.MouseSender',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=143,
  serialized_end=317,
  methods=[
  _descriptor.MethodDescriptor(
    name='mouseStream',
    full_name='mouseSenderPackage.MouseSender.mouseStream',
    index=0,
    containing_service=None,
    input_type=_EVENTSTRING,
    output_type=_EVENTSTRING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sayHello',
    full_name='mouseSenderPackage.MouseSender.sayHello',
    index=1,
    containing_service=None,
    input_type=_EVENTSTRING,
    output_type=_EVENTSTRING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MOUSESENDER)

DESCRIPTOR.services_by_name['MouseSender'] = _MOUSESENDER

# @@protoc_insertion_point(module_scope)
