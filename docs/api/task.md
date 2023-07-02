
::: brickflow.engine.task
    handler: python
    options:
        members:
            - Task
            - EmailNotifications
            - JarTaskLibrary
            - EggTaskLibrary
            - WheelTaskLibrary
            - PypiTaskLibrary
            - MavenTaskLibrary
            - CranTaskLibrary
            - BrickflowTriggerRule
            - BrickflowTaskEnvVars
            - TaskSettings
            - TaskType
        filters:
            - "!^_[^_]"
            - "!^__[^__]"

