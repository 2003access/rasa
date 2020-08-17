---
sidebar_label: rasa.utils.tensorflow.models
title: rasa.utils.tensorflow.models
---

## RasaModel Objects

```python
class RasaModel(tf.keras.models.Model)
```

Completely override all public methods of keras Model.

Cannot be used as tf.keras.Model

#### \_\_init\_\_

```python
 | __init__(random_seed: Optional[int] = None, tensorboard_log_dir: Optional[Text] = None, tensorboard_log_level: Optional[Text] = "epoch", **kwargs, ,) -> None
```

Initialize the RasaModel.

**Arguments**:

- `random_seed` - set the random seed to get reproducible results

#### fit

```python
 | fit(model_data: RasaModelData, epochs: int, batch_size: Union[List[int], int], evaluate_on_num_examples: int, evaluate_every_num_epochs: int, batch_strategy: Text, silent: bool = False, loading: bool = False, eager: bool = False) -> None
```

Fit model data

#### train\_on\_batch

```python
 | train_on_batch(batch_in: Union[Tuple[tf.Tensor], Tuple[np.ndarray]]) -> None
```

Train on batch

#### batch\_to\_model\_data\_format

```python
 | @staticmethod
 | batch_to_model_data_format(batch: Union[Tuple[tf.Tensor], Tuple[np.ndarray]], data_signature: Dict[Text, List[FeatureSignature]]) -> Dict[Text, List[tf.Tensor]]
```

Convert input batch tensors into batch data format.

Batch contains any number of batch data. The order is equal to the
key-value pairs in session data. As sparse data were converted into indices,
data, shape before, this methods converts them into sparse tensors. Dense data
is kept.

#### linearly\_increasing\_batch\_size

```python
 | @staticmethod
 | linearly_increasing_batch_size(epoch: int, batch_size: Union[List[int], int], epochs: int) -> int
```

Linearly increase batch size with every epoch.

The idea comes from https://arxiv.org/abs/1711.00489.

