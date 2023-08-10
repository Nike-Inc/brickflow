#!/bin/sh

# Check if the version argument is provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <version>"
#  exit 1
fi

# Set the provided version as an environment variable
export BUNDLE_CODE_GEN_CLI_VERSION="$1"

rm -rf .databricks/bin/cli/
python tools/install_databricks_cli.py
python tools/modify_schema.py
datamodel-codegen --input brickflow/bundles/transformed_schema.json \
		--use-title-as-name \
		--disable-appending-item-suffix \
		--collapse-root-models \
		--capitalise-enum-members \
		--enum-field-as-literal all \
		--input-file-type jsonschema \
		--output brickflow/bundles/model.py
echo "✅  Code generation completed successfully!"
python tools/modify_model.py
echo "✅  Updated and patched model successfully!"
echo "# generated with Databricks CLI Version: $(.databricks/bin/cli/*/databricks --version)" | \
  cat - brickflow/bundles/model.py > /tmp/codegen && \
   mv /tmp/codegen brickflow/bundles/model.py
echo "✅  Modified the front matter of the script!"
python brickflow/bundles/model.py # validate python file
echo "✅  Validated the file is proper python code!"
