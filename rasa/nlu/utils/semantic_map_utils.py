
from typing import Text, Set, Optional, Dict, List
from scipy.sparse import csr_matrix, coo_matrix
import json
import numpy as np
import re


class SemanticFingerprint:

  def __init__(self, height: int, width: int, activations: Set[int]) -> None:
    assert height > 0
    assert width > 0
    self.height = height
    self.width = width
    self.activations = activations

  def __len__(self):
    return len(self.activations)

  @property
  def num_cells(self):
    return self.height * self.width

  def as_ascii_art(self) -> Text:
    art = "\n"
    for row in range(self.height):
      for col in range(self.width):
        if col + self.width * row + 1 in self.activations:
          art += "*"
        else:
          art += " "
      art += "\n"
    return art

  def as_activations(self) -> Set[int]:
    return self.activations

  def as_csr_matrix(self, boost: Optional[float] = None) -> csr_matrix:
    if boost:
      data = [1. + boost * self._num_neightbours(a) for a in self.activations]
    else:
      data = np.ones(len(self.activations))
    row_indices = [(a - 1) // self.width for a in self.activations]
    col_indices = [(a - 1) % self.width for a in self.activations]

    return csr_matrix((data, (row_indices, col_indices)), shape=(self.height, self.width), dtype=np.float32)

  def as_coo_row_vector(self, boost: Optional[float] = None) -> coo_matrix:
    return self.as_csr_matrix(boost).reshape((1, -1)).tocoo()

  def as_dense_vector(self, boost: Optional[float] = None) -> np.array:
    return np.reshape(self.as_csr_matrix(boost).todense(), (self.height * self.width, ))

  def as_weighted_activations(self, boost: float = 1. / np.math.pi) -> Dict[int, float]:
    return {a: 1. + boost * self._num_neightbours(a) for a in self.activations}

  def _num_neightbours(self, cell: int, local_topology: int = 8) -> int:  # ToDo: Implement degree > 1 neighbourhood
    if local_topology == 4:
      return len(self.activations.intersection({
        self._shift_onto_map(cell - 1),           # Left
        self._shift_onto_map(cell + 1),           # Right
        self._shift_onto_map(cell - self.width),  # Top
        self._shift_onto_map(cell + self.width)   # Bottom
        }))
    elif local_topology == 8:
      return len(self.activations.intersection({
        self._shift_onto_map(cell - 1),           # Left
        self._shift_onto_map(cell + 1),           # Right
        self._shift_onto_map(cell - self.width),  # Top
        self._shift_onto_map(cell + self.width),  # Bottom
        self._shift_onto_map(cell - 1 - self.width),  # Top Left
        self._shift_onto_map(cell + 1 - self.width),  # Top Right
        self._shift_onto_map(cell - 1 + self.width),  # Bottom Left
        self._shift_onto_map(cell + 1 + self.width),  # Bottom Right
        }))
    else:
      raise ValueError("Local topology must be either 4 or 8.")  # ToDo: Implement 6

  def _shift_onto_map(self, cell: int) -> int:
    """ Ensures that the given cell is on the map by translating its position """

    # Globally the map's topology is a torus, so
    # top and bottom edges are connected, and left
    # and right edges are connected.
    x = (cell - 1) % self.width
    y = (cell - 1) // self.width
    if y < 0:
      y += self.height * abs(y // self.height)
    return x + y * self.width + 1


class SemanticMap:

  def __init__(self, filename: Text) -> None:
    with open(filename, "r", encoding="utf-8") as file:
      data = json.load(file)

    self.width = data["Width"]
    self.height = data["Height"]
    self.local_topology = data["LocalTopology"]
    self.global_topology = data["GlobalTopology"]
    self.note = data["Note"]
    self._embeddings: Dict[Text, List[int]] = data["Embeddings"]
    self._vocab_pattern = re.compile("|".join([r"\b" + re.escape(word) + r"\b" for word in self._embeddings.keys() if not word.startswith("<")]))
    self._special_token_pattern = re.compile("|".join([re.escape(word) for word in self._embeddings.keys() if word.startswith("<")]))

  @property
  def num_cells(self):
    return self.height * self.width

  def get_empty_fingerprint(self):
    return SemanticFingerprint(self.height, self.width, set())

  def get_term_fingerprint(self, term: Text) -> SemanticFingerprint:
    activations = self._embeddings.get(term.lower())
    if not activations:
      return self.get_empty_fingerprint()
    else:
      return SemanticFingerprint(self.height, self.width, set(activations))

  def get_term_fingerprint_as_csr_matrix(self, term: Text) -> SemanticFingerprint:
    return self.get_term_fingerprint(term).as_csr_matrix()

  def get_fingerprint(self, text: Text) -> SemanticFingerprint:
    term_fingerprints = [self.get_term_fingerprint(term) for term in self.get_known_terms(text)]
    if term_fingerprints:
      return self.semantic_merge(*term_fingerprints)
    else:
      return self.get_empty_fingerprint()

  def get_known_terms(self, text: Text) -> List[Text]:
    terms = self._vocab_pattern.findall(text.lower()) + self._special_token_pattern.findall(text.lower())
    return terms

  def semantic_merge(self, *fingerprints: SemanticFingerprint) -> SemanticFingerprint:
    if fingerprints:
      num_active = len(fingerprints[0])
      total = np.sum([fp.as_csr_matrix(boost=0.3) for fp in fingerprints]).toarray().flatten()
      activations = np.argpartition(total, -num_active)[-num_active:] + 1
      return SemanticFingerprint(self.height, self.width, set(activations))
    else:
      return self.get_empty_fingerprint()

  def is_vocabulary_member(self, term: Text) -> bool:
    return term in self._embeddings

  def has_fingerprint(self, text: Text) -> bool:
    return len(self.get_known_terms(text.lower())) > 0

  @property
  def vocabulary(self) -> Set[Text]:
    return set(self._embeddings.keys())


def semantic_overlap(fp1: SemanticFingerprint, fp2: SemanticFingerprint, method: Text = "Jaccard") -> float:
  """Returns the overlap score of the two fingerprints.

     The score is a floating point number between 0 and 1, where
     0 means that the two words are unrelated and 1 means that
     they share exactly the same meaning.
  """

  if method == "SzymkiewiczSimpson":
    return _szymkiewicz_simpson_overlap(fp1, fp2)
  elif method == "Jaccard":
    return _jaccard_overlap(fp1, fp2)
  elif method == "Rand":
    return _rand_overlap(fp1, fp2)
  else:
    raise ValueError(f"Method '{method}' is not one of 'SzymkiewiczSimpson', 'Jaccard', or 'Rand'")


def _szymkiewicz_simpson_overlap(fp1: SemanticFingerprint, fp2: SemanticFingerprint) -> float:
  num_common = len(fp1.as_activations().intersection(fp2.as_activations()))
  min_length = min(len(fp1.as_activations()), len(fp2.as_activations()))
  if min_length == 0:
    return 0
  else:
    return float(num_common / min_length)


def _jaccard_overlap(fp1: SemanticFingerprint, fp2: SemanticFingerprint) -> float:
  num_common = len(fp1.as_activations().intersection(fp2.as_activations()))
  union_length = len(fp1.as_activations().union(fp2.as_activations()))
  if union_length == 0:
    return 1.
  else:
    return float(num_common / union_length)


def _rand_overlap(fp1: SemanticFingerprint, fp2: SemanticFingerprint) -> float:
  num_cells = fp1.height * fp1.width
  num_11 = len(fp1.as_activations().intersection(fp2.as_activations()))
  num_10 = len(fp1.as_activations().difference(fp2.as_activations()))
  num_01 = len(fp2.as_activations().difference(fp1.as_activations()))
  num_00 = num_cells - (num_10 + num_01 + num_11)
  return float((num_00 + num_11) / num_cells)

