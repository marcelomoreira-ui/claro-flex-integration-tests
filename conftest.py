from fixtures.auth_fixtures import *
from fixtures.menu_fixtures import *
from fixtures.address_eligibility_fixtures import *
from fixtures.auth_bff_fixtures import *
from fixtures.customer_fixtures import *

import pytest
from utils.logger import get_logger as logger

logger = logger(__name__)

@pytest.fixture(scope="module", autouse=True)
def suite_setup_teardown(request):

    module_name = request.node.name.replace("test_", "").replace(".py", "").replace("_", " ").upper()
    
    print(f"\n{'='*50} STARTING {module_name} TESTS {'='*50}")
    
    yield
    
    print(f"\n{'='*50} FINISHING {module_name} TESTS {'='*50}")