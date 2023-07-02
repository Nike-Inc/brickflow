databricks bundle schema > brickflow/bundles/schema.json
python tools/modify_schema.py
datamodel-codegen --input brickflow/bundles/transformed_schema.json \
		--use-title-as-name \
		--disable-appending-item-suffix \
		--collapse-root-models \
		--capitalise-enum-members \
		--enum-field-as-literal all \
		--input-file-type jsonschema \
		--output brickflow/bundles/model.py
python tools/modify_model.py
echo "# generated with Databricks CLI Version: $(databricks --version)" | \
  cat - brickflow/bundles/model.py > /tmp/codegen && \
   mv /tmp/codegen brickflow/bundles/model.py
python brickflow/bundles/model.py # validate python file
