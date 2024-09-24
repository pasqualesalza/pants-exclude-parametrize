__defaults__(
    {
        (
            python_sources,
            pex_binary,
        ): dict(
            resolve=parametrize("python-default", "python-custom"),
        ),
    }
)

python_sources()

pex_binary(
    name="pex_binary",
    entry_point="main.py",
    dependencies=["./req.py"],
)

pex_binary(
    name="pex_binary-exclude",
    entry_point="main.py",
    dependencies=["./req.py", "!!requirements#requests"],
)

pex_binary(
    name="pex_binary-exclude-explicit",
    entry_point="main.py",
    dependencies=[
        "./req.py",
        "!!requirements#requests@resolve=python-default",
        "!!requirements#requests@resolve=python-custom",
    ],
)

resource(name="pyproject", source="pyproject.toml")

python_distribution(
    name="python_distribution",
    dependencies=[":pyproject"],
    provides=python_artifact(
        name="example",
        version="0.0.1",
    ),
    generate_setup=False,
    resolve=parametrize("python-default", "python-custom"),
)
