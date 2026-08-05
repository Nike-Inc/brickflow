import pytest

from brickflow_plugins import BrickflowSecretsBackend as TopLevelBrickflowSecretsBackend
from brickflow_plugins.operators.deprecated_airflow_operators import (
    AirflowProxyOktaClusterAuth,
    BashOperator,
    BranchPythonOperator,
    BrickflowSecretsBackend,
    ShortCircuitOperator,
    TaskDependencySensor,
)
from brickflow_plugins.secrets import (
    BrickflowSecretsBackend as SecretsBrickflowSecretsBackend,
)


@pytest.mark.parametrize(
    "deprecated_class",
    [
        BashOperator,
        BranchPythonOperator,
        ShortCircuitOperator,
        TaskDependencySensor,
        AirflowProxyOktaClusterAuth,
        BrickflowSecretsBackend,
    ],
)
def test_deprecated_airflow_classes_raise_on_instantiation(deprecated_class):
    with pytest.raises(RuntimeError, match="deprecated and no longer supported"):
        deprecated_class()


def test_brickflow_secrets_backend_import_paths():
    assert TopLevelBrickflowSecretsBackend is BrickflowSecretsBackend
    assert SecretsBrickflowSecretsBackend is BrickflowSecretsBackend
