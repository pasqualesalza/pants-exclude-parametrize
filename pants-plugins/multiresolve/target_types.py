from __future__ import annotations
from pants.engine.target import (
    Dependencies,
)

import logging
from typing import (
    TYPE_CHECKING,
)

from pants.engine.target import (
    Target,
)

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    pass

from pants.backend.python.target_types import PexBinary, PexBinaryDependenciesField


class MultiResolvePexBinaryDependenciesField(Dependencies):
    supports_transitive_excludes = True


from pants.util.ordered_set import FrozenOrderedSet


class MultiResolvePexBinaryTarget(Target):
    alias = "mr_pex_binary"
    core_fields = (
        *(FrozenOrderedSet(PexBinary.core_fields) - {PexBinaryDependenciesField}),
        MultiResolvePexBinaryDependenciesField,
    )
