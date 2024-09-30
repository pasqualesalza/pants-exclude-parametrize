from pants.backend.python.target_types import PythonDistribution, PythonResolveField
from pants.core.target_types import ResourcesGeneratorTarget, ResourceTarget


def rules():
    # Hack the moved fields of the ResourcesGeneratorTarget to include PythonResolveField when generating a ResourceTarget.
    ResourcesGeneratorTarget.moved_fields = (
        *ResourcesGeneratorTarget.moved_fields,
        PythonResolveField,
    )

    # Adding the PythonResolveField to core targets.
    return [
        PythonDistribution.register_plugin_field(PythonResolveField),
        ResourcesGeneratorTarget.register_plugin_field(PythonResolveField),
        ResourceTarget.register_plugin_field(PythonResolveField),
    ]
