---
sidebar_label: rasa.shared.utils.io
title: rasa.shared.utils.io
---

#### raise\_warning

```python
raise_warning(message: Text, category: Optional[Type[Warning]] = None, docs: Optional[Text] = None, **kwargs: Any, ,) -> None
```

Emit a `warnings.warn` with sensible defaults and a colored warning msg.

#### write\_text\_file

```python
write_text_file(content: Text, file_path: Union[Text, Path], encoding: Text = DEFAULT_ENCODING, append: bool = False) -> None
```

Writes text to a file.

**Arguments**:

- `content` - The content to write.
- `file_path` - The path to which the content should be written.
- `encoding` - The encoding which should be used.
- `append` - Whether to append to the file or to truncate the file.

#### read\_file

```python
read_file(filename: Union[Text, Path], encoding: Text = DEFAULT_ENCODING) -> Any
```

Read text from a file.

#### read\_json\_file

```python
read_json_file(filename: Union[Text, Path]) -> Any
```

Read json from a file.

#### list\_directory

```python
list_directory(path: Text) -> List[Text]
```

Returns all files and folders excluding hidden files.

If the path points to a file, returns the file. This is a recursive
implementation returning files in any depth of the path.

#### list\_files

```python
list_files(path: Text) -> List[Text]
```

Returns all files excluding hidden files.

If the path points to a file, returns the file.

#### list\_subdirectories

```python
list_subdirectories(path: Text) -> List[Text]
```

Returns all folders excluding hidden files.

If the path points to a file, returns an empty list.

#### get\_text\_hash

```python
get_text_hash(text: Text, encoding: Text = DEFAULT_ENCODING) -> Text
```

Calculate the md5 hash for a text.

#### fix\_yaml\_loader

```python
fix_yaml_loader() -> None
```

Ensure that any string read by yaml is represented as unicode.

#### replace\_environment\_variables

```python
replace_environment_variables() -> None
```

Enable yaml loader to process the environment variables in the yaml.

#### read\_yaml

```python
read_yaml(content: Text) -> Any
```

Parses yaml from a text.

**Arguments**:

- `content` - A text containing yaml content.
  

**Raises**:

- `ruamel.yaml.parser.ParserError` - If there was an error when parsing the YAML.

#### read\_yaml\_file

```python
read_yaml_file(filename: Union[Text, Path]) -> Union[List[Any], Dict[Text, Any]]
```

Parses a yaml file.

**Arguments**:

- `filename` - The path to the file which should be read.

#### write\_yaml

```python
write_yaml(data: Any, target: Union[Text, Path, StringIO], should_preserve_key_order: bool = False) -> None
```

Writes a yaml to the file or to the stream

**Arguments**:

- `data` - The data to write.
- `target` - The path to the file which should be written or a stream object
- `should_preserve_key_order` - Whether to force preserve key order in `data`.

#### convert\_to\_ordered\_dict

```python
convert_to_ordered_dict(obj: Any) -> Any
```

Convert object to an `OrderedDict`.

**Arguments**:

- `obj` - Object to convert.
  

**Returns**:

  An `OrderedDict` with all nested dictionaries converted if `obj` is a
  dictionary, otherwise the object itself.

#### is\_logging\_disabled

```python
is_logging_disabled() -> bool
```

Returns `True` if log level is set to WARNING or ERROR, `False` otherwise.

#### create\_directory\_for\_file

```python
create_directory_for_file(file_path: Union[Text, Path]) -> None
```

Creates any missing parent directories of this file path.

#### dump\_obj\_as\_json\_to\_file

```python
dump_obj_as_json_to_file(filename: Union[Text, Path], obj: Any) -> None
```

Dump an object as a json string to a file.

#### dump\_obj\_as\_yaml\_to\_string

```python
dump_obj_as_yaml_to_string(obj: Dict) -> Text
```

Writes data (python dict) to a yaml string.

#### create\_directory

```python
create_directory(directory_path: Text) -> None
```

Creates a directory and its super paths.

Succeeds even if the path already exists.

#### raise\_deprecation\_warning

```python
raise_deprecation_warning(message: Text, warn_until_version: Text = NEXT_MAJOR_VERSION_FOR_DEPRECATIONS, docs: Optional[Text] = None, **kwargs: Any, ,) -> None
```

Thin wrapper around `raise_warning()` to raise a deprecation warning. It requires
a version until which we&#x27;ll warn, and after which the support for the feature will
be removed.

