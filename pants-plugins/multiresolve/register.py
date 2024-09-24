from pants.backend.python.target_types import PythonDistribution, PythonResolveField

def rules():
    # return (*target_types_rules.rules(),)
    return [PythonDistribution.register_plugin_field(PythonResolveField)]
