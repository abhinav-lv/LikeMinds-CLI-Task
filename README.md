# LikeMinds CLI Task

## Get Started

-   There are no requirements or libaries needed.
-   You can create a python environment and just run the script: `python task.py`

## Note

-   I tried implementing `argparse` to make an actual CLI app, but couldn't get it to work.
-   Due to limited time, I just used a while loop where commands are entered when the program is running.
-   So we can just run the program, and pass the commands when the program is running.

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

-   Exit the program
    ```
    > exit
    ```
