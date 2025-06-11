import pytest
from dbt.clients.jinja import MacroGenerator
from pytest import SubRequest
from dbt.config.runtime import RuntimeConfig  # Add this import

@pytest.fixture
def config(request: SubRequest) -> RuntimeConfig:
    # ...
    args = Args(
        profiles_dir = '~/.dbt'
        project_dir=request.config.getoption("--dbt-project-dir"),
        profiles_dir="C:\\Users\\megha\\.dbt",  # hardcoded value
        target=request.config.getoption("--dbt-target"),
        profile=None,
        threads=None,
    )
    # ...

@pytest.mark.parametrize(
    "macro_generator",
    ["macro.dw_pytest.clean_column_name"],  # change `dw_pytest` if your project name is different
    indirect=True,
)
@pytest.mark.parametrize(
    "name,expected",
    [
        ("Order ID", "order_id"),
        ("Customer Name", "customer_name"),
        ("Sales.Amount", "sales_amount"),
        ("  spaces  ", "spaces"),
    ],
)
def test_clean_column_name(macro_generator: MacroGenerator, name: str, expected: str):
    result = macro_generator([name])
    assert result == expected

    result = macro_generator([name.upper()])
    assert result == expected