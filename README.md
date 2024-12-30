# LikeMinds CLI Task

## Get Started

-   There are no requirements or libaries needed.
-   You can create a python environment and just run the script: `python task.py`

## List of Commands

-   Create a new `access` method.

    ```
    > addAccess <access>
    ```

-   Create a new `resource`.

    ```
    > addResource <resource>
    ```

-   Create a new `role`.

    ```
    > addRole <role>
    ```

-   Create a new `user`.

    ```
    > addUser <user>
    ```

-   Attach an `access` method to a `resource`.

    ```
    > addAccessOnResource <access> <resource>
    ```

-   Attach an `access` method to a `resource` for a `role`.

    ```
    > addAccessOnResourceToRole <access> <resource> <role>
    ```

-   Attach a `role` to a `user`.

    ```
    > addRoleToUser <role> <user>
    ```

-   Check if a `user` has permission to perform `access` on a `resource`.

    ```
    > checkAccess <user> <resource> <access>
    ```

-   List all entities (users, roles, resources, accesses).

    ```
    > listAllEntities
    ```
