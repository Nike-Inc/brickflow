"""
Example workflow demonstrating pattern matching in task dependencies.

Pattern matching allows you to specify dependencies using glob patterns
instead of explicitly listing each task. This is particularly useful for
workflows with many similar tasks.
"""

from brickflow import (
    Cluster,
    TaskSettings,
    TaskRunCondition,
    Workflow,
)

wf = Workflow(
    "pattern_matching_demo",
    default_cluster=Cluster.from_existing_cluster("<your-cluster-id>"),
)


# Example 1: Basic Pattern Matching
# Define multiple extract tasks
@wf.task()
def extract_customers():
    print("Extracting customer data...")


@wf.task()
def extract_orders():
    print("Extracting order data...")


@wf.task()
def extract_products():
    print("Extracting product data...")


@wf.task(depends_on="extract_*")  # Matches all tasks starting with "extract_"
def validate_extracts():
    """This task depends on ALL extract_* tasks automatically."""
    print("Validating all extracted data...")


# Example 2: Multiple Stages with Patterns
@wf.task(depends_on=validate_extracts)
def transform_customer_data():
    print("Transforming customer data...")


@wf.task(depends_on=validate_extracts)
def transform_order_data():
    print("Transforming order data...")


@wf.task(depends_on=validate_extracts)
def transform_product_data():
    print("Transforming product data...")


@wf.task(depends_on="transform_*")  # Matches all transform tasks
def aggregate_data():
    """Aggregates data from all transform tasks."""
    print("Aggregating all transformed data...")


# Example 3: Advanced Pattern - Character Sets
@wf.task(depends_on=aggregate_data)
def load_to_region_a():
    print("Loading to region A...")


@wf.task(depends_on=aggregate_data)
def load_to_region_b():
    print("Loading to region B...")


@wf.task(depends_on=aggregate_data)
def load_to_region_c():
    print("Loading to region C...")


@wf.task(depends_on=aggregate_data)
def load_to_region_x():
    print("Loading to region X...")


# Only depends on regions a, b, c (not x)
@wf.task(depends_on="load_to_region_[abc]")
def verify_abc_regions():
    """Pattern matches only regions a, b, and c."""
    print("Verifying regions A, B, and C...")


# Example 4: Multiple Patterns in a List
@wf.task(depends_on=["extract_*", "transform_*"])
def comprehensive_validation():
    """Depends on all extract AND transform tasks."""
    print("Running comprehensive validation...")


# Example 5: Mixing Patterns with Explicit Dependencies
@wf.task()
def setup_config():
    print("Setting up configuration...")


@wf.task(depends_on=[setup_config, "transform_*"])
def export_results():
    """Depends on setup_config AND all transform tasks."""
    print("Exporting results...")


# Example 6: Pattern with Conditional Run
@wf.task(
    depends_on="load_*",
    task_settings=TaskSettings(run_if=TaskRunCondition.AT_LEAST_ONE_SUCCESS),
)
def send_notification():
    """Runs if at least one load task succeeds."""
    print("Sending notification...")


# Example 7: Complex Pattern
@wf.task(depends_on=aggregate_data)
def analyze_customer_segment():
    print("Analyzing customer segments...")


@wf.task(depends_on=aggregate_data)
def analyze_order_trends():
    print("Analyzing order trends...")


# Matches any task containing "customer" or "order"
@wf.task(depends_on="*customer*")
def customer_report():
    """Pattern matches tasks containing 'customer' in the name."""
    print("Generating customer report...")
