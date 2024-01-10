import json
from dataclasses import dataclass
from typing import Dict, Any


# Generated using ChatGPT 3.5
def get_name(path):
    new_path = path.replace("/", "_").lstrip("_")
    for remove_item in [
        "artifacts",
        "bundle",
        "environments",
        "include",
        "resources",
        "workspace",
        "items",
        "properties",
    ]:
        new_path = new_path.replace(f"{remove_item}_", "")

    new_path = new_path.replace("_items", "")

    return new_path


@dataclass
class SchemaPatch:
    patch_key: str
    dot_path_location: str
    value: Dict[str, Any]

    def apply_patch(self, definitions):
        if self.patch_key in definitions:
            parts = self.dot_path_location.split(".")
            into_object = definitions[self.patch_key]
            if len(parts) > 1:
                for part in parts[:-1]:
                    into_object = into_object[part]
            into_object[parts[-1]] = self.value


schema_patches = [
    SchemaPatch(
        patch_key="environments_properties_resources_pipelines_properties_clusters_items_autoscale",
        dot_path_location="properties.mode",
        value={
            "type": "enum",
            "enum": ["LEGACY", "ENHANCED"],
            "description": "The autoscaling mode to use. Valid values are LEGACY, ENHANCED.",
        },
    ),
    # Update from ["SINGLE_USER", "USER_ISOLATION", "NONE"] to
    # ["LEGACY_TABLE_ACL", "LEGACY_PASSTHROUGH", "LEGACY_SINGLE_USER", "SINGLE_USER", "USER_ISOLATION", "NONE"]
    # Jan 8, 2024 no breaking changes as its adding new optional enums
    *[
        SchemaPatch(
            patch_key=resource,
            dot_path_location=f"properties.data_security_mode",
            value={
                "type": "enum",
                "default": "SINGLE_USER",
                "enum": [
                    "LEGACY_TABLE_ACL",
                    "LEGACY_PASSTHROUGH",
                    "LEGACY_SINGLE_USER",
                    "SINGLE_USER",
                    "USER_ISOLATION",
                    "NONE",
                ],
                "description": "The data security mode to use for clusters. Valid values are "
                '["LEGACY_TABLE_ACL", "LEGACY_PASSTHROUGH", "LEGACY_SINGLE_USER", '
                '"SINGLE_USER", "USER_ISOLATION", "NONE"].',
            },
        )
        for resource in [
            "resources_jobs_properties_job_clusters_items_new_cluster",
            "resources_jobs_properties_tasks_items_new_cluster",
            "targets_properties_resources_jobs_properties_job_clusters_items_new_cluster",
            "targets_properties_resources_jobs_properties_tasks_items_new_cluster",
        ]
    ],
]


def apply_definition_patches(definitions):
    # enhanced_autoscaling_mode for dlt https://docs.databricks.com/delta-live-tables/auto-scaling.html
    for schema_patch in schema_patches:
        schema_patch.apply_patch(definitions)
    # patch1 = "environments_properties_resources_pipelines_properties_clusters_items_autoscale"
    # if patch1 in definitions:
    #     definitions[patch1]["properties"]["mode"] = {
    #         "type": "string",
    #         "enum": ["LEGACY", "ENHANCED"],
    #         "description": "The autoscaling mode to use. Valid values are LEGACY, ENHANCED.",
    #     }
    return definitions


def handle_targets_properties_ref(ref) -> str:
    # handle target and just reuse the same model build into the base without target
    if ref.startswith("#/definitions/targets_properties_"):
        return ref.replace("#/definitions/targets_properties_", "#/definitions/", 1)

    return ref


def remove_all_definitions_that_start_with(
    definitions, start_with="targets_properties_"
):
    return {k: v for k, v in definitions.items() if not k.startswith(start_with)}


def generate_definitions(schema):
    definitions = {}
    definition_lookup = {}
    new_schema = schema.copy()
    new_schema["definitions"] = {}

    def process_object(obj, path):
        for key, value in obj.items():
            if isinstance(value, dict):
                if value.get("type") == "object":
                    new_path = f"{path}/{key}"
                    definition_name = new_path.replace("/", "_").lstrip("_").lstrip("_")

                    # get_name(key, new_path)
                    definition_data = {}
                    if definition_name not in definitions:
                        definition_data["type"] = "object"
                        definition_data["title"] = get_name(new_path)
                        if "required" in value:
                            definition_data["required"] = value["required"]
                        if "additionalProperties" in value and isinstance(
                            value["additionalProperties"], bool
                        ):
                            definition_data["additionalProperties"] = value[
                                "additionalProperties"
                            ]
                    if "properties" in value:
                        definition_data["properties"] = process_object(
                            value["properties"], new_path
                        )
                    elif "additionalProperties" in value and isinstance(
                        value["additionalProperties"], dict
                    ):
                        definition_data["additionalProperties"] = process_object(
                            value["additionalProperties"], new_path
                        )
                    definition_data_json = json.dumps(definition_data)
                    if definition_data_json not in definition_lookup:
                        definitions[definition_name] = definition_data
                        definition_lookup[json.dumps(definition_data)] = definition_name
                        obj[key] = {
                            "$ref": handle_targets_properties_ref(
                                f"#/definitions/{definition_name}"
                            )
                        }
                    else:
                        obj[key] = {
                            "$ref": handle_targets_properties_ref(
                                f"#/definitions/{definition_lookup[definition_data_json]}"
                            )
                        }
                else:
                    obj[key] = process_object(value, f"{path}/{key}")
        return obj

    new_schema["properties"] = process_object(schema["properties"], "")

    new_schema["definitions"] = apply_definition_patches(definitions)
    new_schema["definitions"] = remove_all_definitions_that_start_with(
        new_schema["definitions"]
    )
    new_schema["title"] = "databricks_asset_bundles"
    return new_schema


if __name__ == "__main__":
    # Example usage:
    with open("brickflow/bundles/schema.json", "r") as file:
        schema = json.load(file)

    new_schema = generate_definitions(schema)

    with open("brickflow/bundles/transformed_schema.json", "w") as file:
        json.dump(new_schema, file, indent=4)
