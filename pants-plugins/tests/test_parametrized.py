from pants.testutil.pants_integration_test import run_pants, setup_tmpdir

def test_parametrized_pex_binary_include() -> None:
    run_pants(["list"])
