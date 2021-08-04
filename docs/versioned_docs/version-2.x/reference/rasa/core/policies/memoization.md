---
sidebar_label: rasa.core.policies.memoization
title: rasa.core.policies.memoization
---

## MemoizationPolicy Objects

```python
class MemoizationPolicy(Policy)
```

The policy that remembers exact examples of
`max_history` turns from training stories.

Since `slots` that are set some time in the past are
preserved in all future feature vectors until they are set
to None, this policy implicitly remembers and most importantly
recalls examples in the context of the current dialogue
longer than `max_history`.

This policy is not supposed to be the only policy in an ensemble,
it is optimized for precision and not recall.
It should get a 100% precision because it emits probabilities of 1.1
along it&#x27;s predictions, which makes every mistake fatal as
no other policy can overrule it.

If it is needed to recall turns from training dialogues where
some slots might not be set during prediction time, and there are
training stories for this, use AugmentedMemoizationPolicy.

#### \_\_init\_\_

```python
 | __init__(featurizer: Optional[TrackerFeaturizer] = None, priority: int = MEMOIZATION_POLICY_PRIORITY, max_history: Optional[int] = MAX_HISTORY_NOT_SET, lookup: Optional[Dict] = None) -> None
```

Initialize the policy.

**Arguments**:

- `featurizer` - tracker featurizer
- `priority` - the priority of the policy
- `max_history` - maximum history to take into account when featurizing trackers
- `lookup` - a dictionary that stores featurized tracker states and
  predicted actions for them

## AugmentedMemoizationPolicy Objects

```python
class AugmentedMemoizationPolicy(MemoizationPolicy)
```

The policy that remembers examples from training stories
for `max_history` turns.

If it is needed to recall turns from training dialogues
where some slots might not be set during prediction time,
add relevant stories without such slots to training data.
E.g. reminder stories.

Since `slots` that are set some time in the past are
preserved in all future feature vectors until they are set
to None, this policy has a capability to recall the turns
up to `max_history` from training stories during prediction
even if additional slots were filled in the past
for current dialogue.

