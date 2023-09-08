# brickflow-examples
This repository consists of examples for brickflow

## Getting Started

### Prerequisites
```shell
pip install brickflows
```
### Clone the repository

```shell
git clone https://github.com/Nike-Inc/brickflow.git
cd brickflow/examples/brickflow_examples
```

### Update demo_wf.py
```diff
- default_cluster=Cluster.from_existing_cluster("<all-purpose-cluster-id>"),
+ default_cluster=Cluster.from_existing_cluster("your-cluster-id"),
```
```diff
-     permissions=WorkflowPermissions(
-        can_manage_run=[User("abc@gmail.com"), User("xyz@gmail.com")],
-        can_view=[User("def@gmail.com")],
-        can_manage=[User("ghi@gmail.com")],
-    ),
+     permissions=WorkflowPermissions(
+        can_manage_run=[User("dbx-user-1-email"), User("dbx-user-1-email")],
+        can_view=[User("dbx-user-3-email")],
+        can_manage=[User("dbx-user-4-email")],
+    ),
```

```diff
-        email_notifications=EmailNotifications(
-            on_start=["xyz@gmail.com"],
-            on_success=["xyz@gmail.com"],
-            on_failure=["xyz@gmail.com"],
-        ),
+        email_notifications=EmailNotifications(
+           on_start=["your-email"]
+           on_success=["your-email"],
+           on_failure=["your-email"],
+       ),
```

### Deploy the workflow to databricks
```shell
brickflow projects deploy --project brickflow-demo -e local
```

### Run the demo workflow
- login to databricks workspace
- go to the workflows and select the brickflow-demo
- click on the run button
