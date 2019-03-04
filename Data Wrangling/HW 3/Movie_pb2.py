# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Movie.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Movie.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bMovie.proto\"\x9c\x05\n\x05Movie\x12\r\n\x05\x63olor\x18\x01 \x01(\t\x12\x1e\n\x16num_critic_for_reviews\x18\x02 \x01(\x02\x12\x10\n\x08\x64uration\x18\x03 \x01(\x02\x12\r\n\x05gross\x18\x04 \x01(\x02\x12\x0e\n\x06genres\x18\x05 \x01(\t\x12\x13\n\x0bmovie_title\x18\x06 \x02(\t\x12\x1c\n\x14\x66\x61\x63\x65number_in_poster\x18\x07 \x01(\x02\x12\x17\n\x0fnum_voted_users\x18\x08 \x01(\x03\x12!\n\x19\x63\x61st_total_facebook_likes\x18\t \x01(\x03\x12\x15\n\rplot_keywords\x18\n \x01(\t\x12\x17\n\x0fmovie_imdb_link\x18\x0b \x01(\t\x12\x1c\n\x14num_user_for_reviews\x18\x0c \x01(\x02\x12\x10\n\x08language\x18\r \x01(\t\x12\x0f\n\x07\x63ountry\x18\x0e \x01(\t\x12\x16\n\x0e\x63ontent_rating\x18\x0f \x01(\t\x12\x0e\n\x06\x62udget\x18\x10 \x01(\x02\x12\x12\n\ntitle_year\x18\x11 \x01(\x02\x12\x12\n\nimdb_score\x18\x12 \x01(\x02\x12\x14\n\x0c\x61spect_ratio\x18\x13 \x01(\x02\x12\x1c\n\x14movie_facebook_likes\x18\x14 \x01(\x05\x12\x1d\n\x06person\x18\x15 \x03(\x0b\x32\r.Movie.Person\x1a\xaf\x01\n\x06Person\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1a\n\x12num_facebook_likes\x18\x02 \x01(\x05\x12\x34\n\x04role\x18\x03 \x01(\x0e\x32\x1c.Movie.Person.role_of_person:\x08\x44irector\"E\n\x0erole_of_person\x12\x0c\n\x08\x44irector\x10\x00\x12\x0b\n\x07\x61\x63tor_1\x10\x01\x12\x0b\n\x07\x61\x63tor_2\x10\x02\x12\x0b\n\x07\x61\x63tor_3\x10\x03\"\"\n\tMovieBase\x12\x15\n\x05movie\x18\x01 \x03(\x0b\x32\x06.Movie')
)



_MOVIE_PERSON_ROLE_OF_PERSON = _descriptor.EnumDescriptor(
  name='role_of_person',
  full_name='Movie.Person.role_of_person',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Director', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='actor_1', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='actor_2', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='actor_3', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=615,
  serialized_end=684,
)
_sym_db.RegisterEnumDescriptor(_MOVIE_PERSON_ROLE_OF_PERSON)


_MOVIE_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Movie.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Movie.Person.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_facebook_likes', full_name='Movie.Person.num_facebook_likes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role', full_name='Movie.Person.role', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MOVIE_PERSON_ROLE_OF_PERSON,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=684,
)

_MOVIE = _descriptor.Descriptor(
  name='Movie',
  full_name='Movie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='Movie.color', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_critic_for_reviews', full_name='Movie.num_critic_for_reviews', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='duration', full_name='Movie.duration', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gross', full_name='Movie.gross', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genres', full_name='Movie.genres', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movie_title', full_name='Movie.movie_title', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='facenumber_in_poster', full_name='Movie.facenumber_in_poster', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_voted_users', full_name='Movie.num_voted_users', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cast_total_facebook_likes', full_name='Movie.cast_total_facebook_likes', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plot_keywords', full_name='Movie.plot_keywords', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movie_imdb_link', full_name='Movie.movie_imdb_link', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_user_for_reviews', full_name='Movie.num_user_for_reviews', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='language', full_name='Movie.language', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='Movie.country', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_rating', full_name='Movie.content_rating', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='budget', full_name='Movie.budget', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_year', full_name='Movie.title_year', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imdb_score', full_name='Movie.imdb_score', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aspect_ratio', full_name='Movie.aspect_ratio', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='movie_facebook_likes', full_name='Movie.movie_facebook_likes', index=19,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='person', full_name='Movie.person', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_MOVIE_PERSON, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=684,
)


_MOVIEBASE = _descriptor.Descriptor(
  name='MovieBase',
  full_name='MovieBase',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='movie', full_name='MovieBase.movie', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=686,
  serialized_end=720,
)

_MOVIE_PERSON.fields_by_name['role'].enum_type = _MOVIE_PERSON_ROLE_OF_PERSON
_MOVIE_PERSON.containing_type = _MOVIE
_MOVIE_PERSON_ROLE_OF_PERSON.containing_type = _MOVIE_PERSON
_MOVIE.fields_by_name['person'].message_type = _MOVIE_PERSON
_MOVIEBASE.fields_by_name['movie'].message_type = _MOVIE
DESCRIPTOR.message_types_by_name['Movie'] = _MOVIE
DESCRIPTOR.message_types_by_name['MovieBase'] = _MOVIEBASE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), dict(

  Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
    DESCRIPTOR = _MOVIE_PERSON,
    __module__ = 'Movie_pb2'
    # @@protoc_insertion_point(class_scope:Movie.Person)
    ))
  ,
  DESCRIPTOR = _MOVIE,
  __module__ = 'Movie_pb2'
  # @@protoc_insertion_point(class_scope:Movie)
  ))
_sym_db.RegisterMessage(Movie)
_sym_db.RegisterMessage(Movie.Person)

MovieBase = _reflection.GeneratedProtocolMessageType('MovieBase', (_message.Message,), dict(
  DESCRIPTOR = _MOVIEBASE,
  __module__ = 'Movie_pb2'
  # @@protoc_insertion_point(class_scope:MovieBase)
  ))
_sym_db.RegisterMessage(MovieBase)


# @@protoc_insertion_point(module_scope)
