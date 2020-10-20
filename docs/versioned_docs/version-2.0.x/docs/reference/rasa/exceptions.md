---
sidebar_label: rasa.exceptions
title: rasa.exceptions
---

## ModelNotFound Objects

```python
class ModelNotFound(RasaException)
```

Raised when a model is not found in the path provided by the user.

## NoEventsToMigrateError Objects

```python
class NoEventsToMigrateError(RasaException)
```

Raised when no events to be migrated are found.

## NoConversationsInTrackerStoreError Objects

```python
class NoConversationsInTrackerStoreError(RasaException)
```

Raised when a tracker store does not contain any conversations.

## NoEventsInTimeRangeError Objects

```python
class NoEventsInTimeRangeError(RasaException)
```

Raised when a tracker store does not contain events within a given time range.

## MissingDependencyException Objects

```python
class MissingDependencyException(RasaException)
```

Raised if a python package dependency is needed, but not installed.

## PublishingError Objects

```python
class PublishingError(RasaException)
```

Raised when publishing of an event fails.

**Attributes**:

- `timestamp` - Unix timestamp of the event during which publishing fails.

