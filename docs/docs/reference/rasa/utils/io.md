---
sidebar_label: rasa.utils.io
title: rasa.utils.io
---

#### pickle\_dump

```python
pickle_dump(filename: Union[Text, Path], obj: Any) -> None
```

Saves object to file.

**Arguments**:

- `filename` - the filename to save the object to
- `obj` - the object to store

#### pickle\_load

```python
pickle_load(filename: Union[Text, Path]) -> Any
```

Loads an object from a file.

**Arguments**:

- `filename` - the filename to load the object from
  
- `Returns` - the loaded object

#### read\_config\_file

```python
read_config_file(filename: Text) -> Dict[Text, Any]
```

Parses a yaml configuration file. Content needs to be a dictionary

**Arguments**:

- `filename` - The path to the file which should be read.

#### unarchive

```python
unarchive(byte_array: bytes, directory: Text) -> Text
```

Tries to unpack a byte array interpreting it as an archive.

Tries to use tar first to unpack, if that fails, zip will be used.

#### create\_temporary\_file

```python
create_temporary_file(data: Any, suffix: Text = "", mode: Text = "w+") -> Text
```

Creates a tempfile.NamedTemporaryFile object for data.

mode defines NamedTemporaryFile&#x27;s  mode parameter in py3.

#### create\_temporary\_directory

```python
create_temporary_directory() -> Text
```

Creates a tempfile.TemporaryDirectory.

#### create\_path

```python
create_path(file_path: Text) -> None
```

Makes sure all directories in the &#x27;file_path&#x27; exists.

#### file\_type\_validator

```python
file_type_validator(valid_file_types: List[Text], error_message: Text) -> Type["Validator"]
```

Creates a `Validator` class which can be used with `questionary` to validate
file paths.

#### not\_empty\_validator

```python
not_empty_validator(error_message: Text) -> Type["Validator"]
```

Creates a `Validator` class which can be used with `questionary` to validate
that the user entered something other than whitespace.

#### create\_validator

```python
create_validator(function: Callable[[Text], bool], error_message: Text) -> Type["Validator"]
```

Helper method to create `Validator` classes from callable functions. Should be
removed when questionary supports `Validator` objects.

#### zip\_folder

```python
zip_folder(folder: Text) -> Text
```

Create an archive from a folder.

#### json\_unpickle

```python
json_unpickle(file_name: Union[Text, Path]) -> Any
```

Unpickle an object from file using json.

**Arguments**:

- `file_name` - the file to load the object from
  
- `Returns` - the object

#### json\_pickle

```python
json_pickle(file_name: Union[Text, Path], obj: Any) -> None
```

Pickle an object to a file using json.

**Arguments**:

- `file_name` - the file to store the object to
- `obj` - the object to store

