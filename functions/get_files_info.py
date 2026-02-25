import os


def get_files_info(working_directory, directory="."):
    """
    Get the information about the files in a directory.

    Args:
        working_directory: The working directory to get the files from.
        directory: The directory to get the files from.

    Returns:
        A string with the information about the files in the directory.
    """
    try:
        working_directory_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))
        valid_target_dir = (
            os.path.commonpath([working_directory_abs, target_dir])
            == working_directory_abs
        )
        if not valid_target_dir:
            return f'Error: Cannot list "{directory} as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        contents = os.listdir(target_dir)

        output = ""
        for content in contents:
            content_path = os.path.join(target_dir, content)
            is_dir = os.path.isdir(content_path)
            size = os.path.getsize(content_path)
            output += f"- {content}: file_size={size} bytes, is_dir={is_dir}\n"

        return output
    except Exception as e:
        return f"Error: {e}"
