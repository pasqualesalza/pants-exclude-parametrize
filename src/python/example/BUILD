__defaults__(
    {
        (
            python_sources,
            pex_binary,
            mr_pex_binary,
        ): dict(
            resolve=parametrize("python-default", "python-custom"),
        ),
    }
)

python_sources()

mr_pex_binary(
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
