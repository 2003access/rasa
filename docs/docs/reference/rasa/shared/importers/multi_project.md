---
sidebar_label: rasa.shared.importers.multi_project
title: rasa.shared.importers.multi_project
---
## MultiProjectImporter Objects

```python
class MultiProjectImporter(TrainingDataImporter)
```

#### training\_paths

```python
 | training_paths() -> Set[Text]
```

Returns the paths which should be searched for training data.

#### is\_imported

```python
 | is_imported(path: Text) -> bool
```

Checks whether a path is imported by a skill.

**Arguments**:

- `path` - File or directory path which should be checked.
  

**Returns**:

  `True` if path is imported by a skill, `False` if not.

#### get\_domain

```python
 | get_domain() -> Domain
```

Retrieves model domain (see parent class for full docstring).

#### get\_stories

```python
 | get_stories(template_variables: Optional[Dict] = None, use_e2e: bool = False, exclusion_percentage: Optional[int] = None) -> StoryGraph
```

Retrieves training stories / rules (see parent class for full docstring).

#### get\_conversation\_tests

```python
 | get_conversation_tests() -> StoryGraph
```

Retrieves conversation test stories (see parent class for full docstring).

#### get\_config

```python
 | get_config() -> Dict
```

Retrieves model config (see parent class for full docstring).

#### get\_nlu\_data

```python
 | get_nlu_data(language: Optional[Text] = "en") -> TrainingData
```

Retrieves NLU training data (see parent class for full docstring).

