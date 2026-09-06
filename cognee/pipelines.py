# Don't add any more code here, this file is used only for the purpose
# of enabling imports from `cognee.pipelines` module.
# `from cognee.pipelines import Task` for example.

from .modules.pipelines import Task, run_tasks

__all__ = ["Task", "run_tasks"]
