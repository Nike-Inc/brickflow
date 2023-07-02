from brickflow import RelativePathPackageResolver

RelativePathPackageResolver.add_relative_path(
    globals(), current_file_to_root="../", root_to_module="."
)
