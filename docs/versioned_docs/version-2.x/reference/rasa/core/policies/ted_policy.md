---
sidebar_label: ted_policy
title: rasa.core.policies.ted_policy
---

## TEDPolicy Objects

```python
class TEDPolicy(Policy)
```

Transformer Embedding Dialogue (TED) Policy is described in
https://arxiv.org/abs/1910.00486.
This policy has a pre-defined architecture, which comprises the
following steps:
    - concatenate user input (user intent and entities), previous system actions,
      slots and active forms for each time step into an input vector to
      pre-transformer embedding layer;
    - feed it to transformer;
    - apply a dense layer to the output of the transformer to get embeddings of a
      dialogue for each time step;
    - apply a dense layer to create embeddings for system actions for each time
      step;
    - calculate the similarity between the dialogue embedding and embedded system
      actions. This step is based on the StarSpace
      (https://arxiv.org/abs/1709.03856) idea.

#### \_\_init\_\_

```python
 | __init__(featurizer: Optional[TrackerFeaturizer] = None, priority: int = DEFAULT_POLICY_PRIORITY, max_history: Optional[int] = None, model: Optional[RasaModel] = None, fake_features: Optional[Dict[Text, List["Features"]]] = None, entity_tag_specs: Optional[List[EntityTagSpec]] = None, should_finetune: bool = False, **kwargs: Any, ,) -> None
```

Declare instance variables with default values.

#### train

```python
 | train(training_trackers: List[TrackerWithCachedStates], domain: Domain, interpreter: NaturalLanguageInterpreter, **kwargs: Any, ,) -> None
```

Train the policy on given training trackers.

#### predict\_action\_probabilities

```python
 | predict_action_probabilities(tracker: DialogueStateTracker, domain: Domain, interpreter: NaturalLanguageInterpreter, **kwargs: Any, ,) -> PolicyPrediction
```

Predicts the next action the bot should take after seeing the tracker.

**Arguments**:

- `tracker` - the :class:`rasa.core.trackers.DialogueStateTracker`
- `domain` - the :class:`rasa.shared.core.domain.Domain`
- `interpreter` - Interpreter which may be used by the policies to create
  additional features.
  

**Returns**:

  The policy&#x27;s prediction (e.g. the probabilities for the actions).

#### persist

```python
 | persist(path: Union[Text, Path]) -> None
```

Persists the policy to a storage.

#### load

```python
 | @classmethod
 | load(cls, path: Union[Text, Path], should_finetune: bool = False, epoch_override: int = defaults[EPOCHS], **kwargs: Any, ,) -> "TEDPolicy"
```

Loads a policy from the storage.

**Needs to load its featurizer**

## TED Objects

```python
class TED(TransformerRasaModel)
```

#### \_\_init\_\_

```python
 | __init__(data_signature: Dict[Text, Dict[Text, List[FeatureSignature]]], config: Dict[Text, Any], max_history_featurizer_is_used: bool, label_data: RasaModelData, entity_tag_specs: Optional[List[EntityTagSpec]]) -> None
```

Intializes the TED model.

**Arguments**:

- `data_signature` - the data signature of the input data
- `config` - the model configuration
- `max_history_featurizer_is_used` - if &#x27;True&#x27;
  only the last dialogue turn will be used
- `label_data` - the label data
- `entity_tag_specs` - the entity tag specifications

#### batch\_loss

```python
 | batch_loss(batch_in: Union[Tuple[tf.Tensor], Tuple[np.ndarray]]) -> tf.Tensor
```

Calculates the loss for the given batch.

**Arguments**:

- `batch_in` - The batch.
  

**Returns**:

  The loss of the given batch.

#### prepare\_for\_predict

```python
 | prepare_for_predict() -> None
```

Prepares the model for prediction.

#### batch\_predict

```python
 | batch_predict(batch_in: Union[Tuple[tf.Tensor], Tuple[np.ndarray]]) -> Dict[Text, Union[tf.Tensor, Dict[Text, tf.Tensor]]]
```

Predicts the output of the given batch.

**Arguments**:

- `batch_in` - The batch.
  

**Returns**:

  The output to predict.

