---
sidebar_label: mitie_intent_classifier
title: rasa.nlu.classifiers.mitie_intent_classifier
---

## MitieIntentClassifier Objects

```python
class MitieIntentClassifier(IntentClassifier)
```

#### \_\_init\_\_

```python
 | __init__(component_config: Optional[Dict[Text, Any]] = None, clf=None) -> None
```

Construct a new intent classifier using the MITIE framework.

#### load

```python
 | @classmethod
 | load(cls, meta: Dict[Text, Any], model_dir: Text, model_metadata: Optional[Metadata] = None, cached_component: Optional["MitieIntentClassifier"] = None, **kwargs: Any, ,) -> "MitieIntentClassifier"
```

Loads trained component (see parent class for full docstring).

