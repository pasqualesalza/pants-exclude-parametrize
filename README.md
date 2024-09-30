# pants-exclude-parametrize

This repository provides an example project to demonstrate an unexpected behavior of Pants when managing explicit dependencies in a target like `pex_binary`, but using `parametrize` to indicate multiple resolves.

The project shows that while Pants correctly applies the suffix `@resolve=` to all dependencies, it does not handle exclusions with the `!!` (transitive exclusion prefix) as expected.

## Project Structure

The project is structured under `src/python/example`. Three examples of `pex_binary` are included to illustrate the issue.

### 1. `pex_binary`

This case refers to the `main.py` file, which depends on Python requirements `numpy` and `pandas`. Additionally, `./req.py` explicitly includes the requirements `requests` and `requests-mock`.

Running the following command:

```bash
pants dependencies --transitive src/python/example:pex_binary
```

Produces the expected output:

```
requirements#numpy@resolve=python-custom
requirements#numpy@resolve=python-default
requirements#pandas@resolve=python-custom
requirements#pandas@resolve=python-default
requirements#requests-mock@resolve=python-custom
requirements#requests-mock@resolve=python-default
requirements#requests@resolve=python-custom
requirements#requests@resolve=python-default
requirements/python-custom.lock:_python-custom_lockfile
requirements/python-default.lock:_python-default_lockfile
requirements/requirements.txt
src/python/example/example/main.py@resolve=python-custom
src/python/example/example/main.py@resolve=python-default
src/python/example/example/req.py@resolve=python-custom
src/python/example/example/req.py@resolve=python-default
```

### 2. `pex_binary-exclude`

In this case, an explicit exclude requirement `!!requirements#requests` is added. Running the same command:

```bash
pants dependencies --transitive src/python/example:pex_binary-exclude
```

Results in the following error:

```
12:36:45.88 [ERROR] 1 Exception encountered:

Engine traceback:
  in `dependencies` goal

ResolveError: The address `requirements#requests` from the `dependencies` field from the target src/python/example:pex_binary-exclude@resolve=python-default was not generated by the target `requirements:requirements`. Did you mean one of these addresses?

  * requirements@resolve=python-default
  * requirements#numpy@resolve=python-default
  * requirements#pandas@resolve=python-default
  * requirements#requests@resolve=python-default
  * requirements#requests-mock@resolve=python-default
  * requirements#urllib3@resolve=python-default
  * requirements/requirements.txt
  * requirements@resolve=python-custom
  * requirements#numpy@resolve=python-custom
  * requirements#pandas@resolve=python-custom
  * requirements#requests@resolve=python-custom
  * requirements#requests-mock@resolve=python-custom
  * requirements#urllib3@resolve=python-custom
  * requirements/requirements.txt
```

### 3. `pex_binary-exclude-explicit`

In this case, exclusions are specified explicitly for each resolve using the `!!` prefix: `!!requirements#requests@resolve=python-default` and `!!requirements#requests@resolve=python-custom`.

Running:

```bash
pants dependencies --transitive src/python/example:pex_binary-exclude-explicit
```

Produces the correct output:

```
requirements#numpy@resolve=python-custom
requirements#numpy@resolve=python-default
requirements#pandas@resolve=python-custom
requirements#pandas@resolve=python-default
requirements#requests-mock@resolve=python-custom
requirements#requests-mock@resolve=python-default
requirements/python-custom.lock:_python-custom_lockfile
requirements/python-default.lock:_python-default_lockfile
requirements/requirements.txt
src/python/example/example/main.py@resolve=python-custom
src/python/example/example/main.py@resolve=python-default
src/python/example/example/req.py@resolve=python-custom
src/python/example/example/req.py@resolve=python-default
```

## Conclusion

This project demonstrates the inconsistency in Pants' handling of exclusions when using the transitive exclusion prefix `!!`. The workaround is to specify exclusions explicitly for each resolve.