---
sidebar_label: tracker_featurizers
title: rasa.core.featurizers.tracker_featurizers
---

## InvalidStory Objects

```python
class InvalidStory(RasaException)
```

Exception that can be raised if story cannot be featurized.

## TrackerFeaturizer Objects

```python
class TrackerFeaturizer()
```

Base class for actual tracker featurizers.

#### \_\_init\_\_

```python
 | __init__(state_featurizer: Optional[SingleStateFeaturizer] = None) -> None
```

Initialize the tracker featurizer.

**Arguments**:

- `state_featurizer` - The state featurizer used to encode the states.

#### training\_states\_actions\_and\_entities

```python
 | training_states_actions_and_entities(trackers: List[DialogueStateTracker], domain: Domain, omit_unset_slots: bool = False) -> Tuple[List[List[State]], List[List[Text]], List[List[Dict[Text, Any]]]]
```

Transforms list of trackers to lists of states, actions and entity data.

**Arguments**:

- `trackers` - The trackers to transform
- `domain` - The domain
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A tuple of list of states, list of actions and list of entity data.

#### training\_states\_and\_actions

```python
 | training_states_and_actions(trackers: List[DialogueStateTracker], domain: Domain, omit_unset_slots: bool = False) -> Tuple[List[List[State]], List[List[Text]]]
```

Transforms list of trackers to lists of states and actions.

**Arguments**:

- `trackers` - The trackers to transform
- `domain` - The domain
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A tuple of list of states and list of actions.

#### featurize\_trackers

```python
 | featurize_trackers(trackers: List[DialogueStateTracker], domain: Domain, interpreter: NaturalLanguageInterpreter, bilou_tagging: bool = False) -> Tuple[
 |         List[List[Dict[Text, List["Features"]]]],
 |         np.ndarray,
 |         List[List[Dict[Text, List["Features"]]]],
 |     ]
```

Featurize the training trackers.

**Arguments**:

- `trackers` - list of training trackers
- `domain` - the domain
- `interpreter` - the interpreter
- `bilou_tagging` - indicates whether BILOU tagging should be used or not
  

**Returns**:

  - a dictionary of state types (INTENT, TEXT, ACTION_NAME, ACTION_TEXT,
  ENTITIES, SLOTS, ACTIVE_LOOP) to a list of features for all dialogue
  turns in all training trackers
  - the label ids (e.g. action ids) for every dialogue turn in all training
  trackers
  - A dictionary of entity type (ENTITY_TAGS) to a list of features
  containing entity tag ids for text user inputs otherwise empty dict
  for all dialogue turns in all training trackers

#### prediction\_states

```python
 | prediction_states(trackers: List[DialogueStateTracker], domain: Domain, use_text_for_last_user_input: bool = False, ignore_rule_only_turns: bool = False, rule_only_data: Optional[Dict[Text, Any]] = None) -> List[List[State]]
```

Transforms list of trackers to lists of states for prediction.

**Arguments**:

- `trackers` - The trackers to transform.
- `domain` - The domain.
- `use_text_for_last_user_input` - Indicates whether to use text or intent label
  for featurizing last user input.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  A list of states.

#### create\_state\_features

```python
 | create_state_features(trackers: List[DialogueStateTracker], domain: Domain, interpreter: NaturalLanguageInterpreter, use_text_for_last_user_input: bool = False, ignore_rule_only_turns: bool = False, rule_only_data: Optional[Dict[Text, Any]] = None) -> List[List[Dict[Text, List["Features"]]]]
```

Create state features for prediction.

**Arguments**:

- `trackers` - A list of state trackers
- `domain` - The domain
- `interpreter` - The interpreter
- `use_text_for_last_user_input` - Indicates whether to use text or intent label
  for featurizing last user input.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  A list (corresponds to the list of trackers)
  of lists (corresponds to all dialogue turns)
  of dictionaries of state type (INTENT, TEXT, ACTION_NAME, ACTION_TEXT,
  ENTITIES, SLOTS, ACTIVE_LOOP) to a list of features for all dialogue
  turns in all trackers.

#### persist

```python
 | persist(path: Union[Text, Path]) -> None
```

Persist the tracker featurizer to the given path.

**Arguments**:

- `path` - The path to persist the tracker featurizer to.

#### load

```python
 | @staticmethod
 | load(path: Text) -> Optional["TrackerFeaturizer"]
```

Load the featurizer from file.

**Arguments**:

- `path` - The path to load the tracker featurizer from.
  

**Returns**:

  The loaded tracker featurizer.

## FullDialogueTrackerFeaturizer Objects

```python
class FullDialogueTrackerFeaturizer(TrackerFeaturizer)
```

Creates full dialogue training data for time distributed architectures.

Creates training data that uses each time output for prediction.
Training data is padded up to the length of the longest dialogue with -1.

#### training\_states\_actions\_and\_entities

```python
 | training_states_actions_and_entities(trackers: List[DialogueStateTracker], domain: Domain, omit_unset_slots: bool = False) -> Tuple[List[List[State]], List[List[Text]], List[List[Dict[Text, Any]]]]
```

Transforms list of trackers to lists of states, actions and entity data.

**Arguments**:

- `trackers` - The trackers to transform
- `domain` - The domain
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A tuple of list of states, list of actions and list of entity data.

#### prediction\_states

```python
 | prediction_states(trackers: List[DialogueStateTracker], domain: Domain, use_text_for_last_user_input: bool = False, ignore_rule_only_turns: bool = False, rule_only_data: Optional[Dict[Text, Any]] = None) -> List[List[State]]
```

Transforms list of trackers to lists of states for prediction.

**Arguments**:

- `trackers` - The trackers to transform.
- `domain` - The domain.
- `use_text_for_last_user_input` - Indicates whether to use text or intent label
  for featurizing last user input.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  A list of states.

## MaxHistoryTrackerFeaturizer Objects

```python
class MaxHistoryTrackerFeaturizer(TrackerFeaturizer)
```

Slices the tracker history into max_history batches.

Creates training data that uses last output for prediction.
Training data is padded up to the max_history with -1.

#### slice\_state\_history

```python
 | @staticmethod
 | slice_state_history(states: List[State], slice_length: Optional[int]) -> List[State]
```

Slice states from the trackers history.

If the slice is at the array borders, padding will be added to ensure
the slice length.

**Arguments**:

- `states` - The states
- `slice_length` - The slice length
  

**Returns**:

  The sliced states.

#### training\_states\_actions\_and\_entities

```python
 | training_states_actions_and_entities(trackers: List[DialogueStateTracker], domain: Domain, omit_unset_slots: bool = False) -> Tuple[List[List[State]], List[List[Text]], List[List[Dict[Text, Any]]]]
```

Transforms list of trackers to lists of states, actions and entity data.

**Arguments**:

- `trackers` - The trackers to transform
- `domain` - The domain
- `omit_unset_slots` - If `True` do not include the initial values of slots.
  

**Returns**:

  A tuple of list of states, list of actions and list of entity data.

#### prediction\_states

```python
 | prediction_states(trackers: List[DialogueStateTracker], domain: Domain, use_text_for_last_user_input: bool = False, ignore_rule_only_turns: bool = False, rule_only_data: Optional[Dict[Text, Any]] = None) -> List[List[State]]
```

Transforms list of trackers to lists of states for prediction.

**Arguments**:

- `trackers` - The trackers to transform.
- `domain` - The domain.
- `use_text_for_last_user_input` - Indicates whether to use text or intent label
  for featurizing last user input.
- `ignore_rule_only_turns` - If True ignore dialogue turns that are present
  only in rules.
- `rule_only_data` - Slots and loops,
  which only occur in rules but not in stories.
  

**Returns**:

  A list of states.

