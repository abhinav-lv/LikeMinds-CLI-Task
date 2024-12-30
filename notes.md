Users

Resources

Access (Access Types / Actions)

At the start, no resources / users / actions

1. Create users and add them to users list [Users]
2. Create resources and add them to resources list [Resources]
3. Create actions, add them to available actions [Actions]
4. Create a role, and store it to Roles
5. addAccessOnResource - (no action if action is not in Actions) [Allows the permissible actions for that resource]
6. addAccessOnResourceToRole - [attach permitted actions on the resource to that role]
7. Add role to user
8. Check access (user, resource, action)

Users: Abhinav

Resources: Image

Actions: READ, WRITE

Roles: Admin

ResourceToActions: [Resource]->List of Actions

RolesToResourceActions: [Role]->List of ResourceActions ->map of resource -> actions

UsersToRoles: [User] -> List of Roles
