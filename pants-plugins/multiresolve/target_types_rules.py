from dataclasses import dataclass
import logging
import time

from multiresolve.target_types import MultiResolvePexBinaryDependenciesField
from pants.engine.rules import collect_rules, rule
from pants.engine.target import (
    FieldSet,
    InferDependenciesRequest,
    InferredDependencies,
    ExplicitlyProvidedDependencies,
    DependenciesRequest,
)
from pants.engine.unions import UnionRule
from pants.engine.rules import Get
from pants.backend.python.dependency_inference.subsystem import PythonInferSubsystem
from pants.backend.python.subsystems.setup import PythonSetup
from pants.engine.addresses import Address, Addresses, UnparsedAddressInputs, assert_single_address
logger = logging.getLogger(__name__)


# @dataclass(frozen=True)
# class TestRequest:
#     test: InferredDependencies

# @rule
# async def test_rule(
#     request: TestRequest,
# ) -> InferredDependencies:
#     logger.debug("patch_explicitly_provided_dependencies")
#     # explicitly_provided_deps = await Get(ExplicitlyProvidedDependencies, DependenciesRequest(request.field_set.dependencies))


# @dataclass(frozen=True)
# class MultiResolveValidationFieldSet(FieldSet):
#     # required_fields = (PexBinaryDependenciesField,)
#     required_fields = ()


@dataclass(frozen=True)
class TestFieldSet(FieldSet):
    required_fields = (MultiResolvePexBinaryDependenciesField,)
    dependencies: MultiResolvePexBinaryDependenciesField


class TestRequest(InferDependenciesRequest):
    infer_from = TestFieldSet


@rule
async def test_rule(
    request: TestRequest,
    python_infer_subsystem: PythonInferSubsystem,
    python_setup: PythonSetup,
) -> InferredDependencies:
    explicitly_provided_deps = await Get(
        ExplicitlyProvidedDependencies,
        DependenciesRequest(request.field_set.dependencies),
    )
    logger.warning(f"explicitly_provided_deps: {explicitly_provided_deps}")
    return InferredDependencies(explicitly_provided_deps.includes)


def rules():
    return (
        *collect_rules(),
        UnionRule(InferDependenciesRequest, TestRequest),
    )
