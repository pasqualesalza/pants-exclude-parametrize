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

pex_binary(
    name="pex_binary",
    entry_point="./example/main.py",
    dependencies=["./example/req.py"],
)

pex_binary(
    name="pex_binary-exclude",
    entry_point="./example/main.py",
    dependencies=["./example/req.py", "!!requirements#requests"],
)

pex_binary(
    name="pex_binary-exclude-explicit",
    entry_point="./example/main.py",
    dependencies=[
        "./example/req.py",
        "!!requirements#requests@resolve=python-default",
        "!!requirements#requests@resolve=python-custom",
    ],
)

resource(name="pyproject", source="pyproject.toml")

python_distribution(
    name="python_distribution",
    dependencies=[":pyproject"],
    provides=python_artifact(),
    generate_setup=False,
    resolve=parametrize("python-default", "python-custom"),
)
