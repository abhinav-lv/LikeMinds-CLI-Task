class Access:
    def __init__(self, name):
        self.name = name


class Resource:
    def __init__(self, name):
        self.name = name
        self.allowedAccesses = set()

    def addAccess(self, access):
        self.allowedAccesses.add(access.name)


class Role:
    def __init__(self, name):
        self.name = name
        self.accessMap = {}

    def addAccessToResource(self, access, resource):
        if resource.name not in self.accessMap:
            self.accessMap[resource.name] = set()
        self.accessMap[resource.name].add(access.name)


class User:
    def __init__(self, name):
        self.name = name
        self.roles = []

    def addRole(self, role):
        self.roles.append(role)


class RBACSystem:
    def __init__(self):
        self.users = {}
        self.roles = {}
        self.resources = {}
        self.accesses = {}

    def addAccess(self, name):
        if name in self.accesses:
            print(f"Access '{name}' already exists.")
        else:
            self.accesses[name] = Access(name)

    def addResource(self, name):
        if name in self.resources:
            print(f"Resource '{name}' already exists.")
        else:
            self.resources[name] = Resource(name)

    def addRole(self, name):
        if name in self.roles:
            print(f"Role '{name}' already exists.")
        else:
            self.roles[name] = Role(name)

    def addUser(self, name):
        if name in self.users:
            print(f"User '{name}' already exists.")
        else:
            self.users[name] = User(name)

    def addAccessOnResource(self, accessName, resourceName):
        if accessName not in self.accesses:
            print(f"Access '{accessName}' does not exist.")
            return
        if resourceName not in self.resources:
            print(f"Resource '{resourceName}' does not exist.")
            return

        resource = self.resources[resourceName]
        access = self.accesses[accessName]
        resource.addAccess(access)

    def addAccessOnResourceToRole(self, accessName, resourceName, roleName):
        if roleName not in self.roles:
            print(f"Role '{roleName}' does not exist.")
            return
        if resourceName not in self.resources:
            print(f"Resource '{resourceName}' does not exist.")
            return
        if accessName not in self.accesses:
            print(f"Access '{accessName}' does not exist.")
            return

        role = self.roles[roleName]
        resource = self.resources[resourceName]

        if accessName not in resource.allowedAccesses:
            print(f"Access '{accessName}' is not allowed on resource '{resourceName}'.")
            return

        access = self.accesses[accessName]
        role.addAccessToResource(access, resource)

    def addRoleToUser(self, roleName, userName):
        if userName not in self.users:
            print(f"User '{userName}' does not exist.")
            return
        if roleName not in self.roles:
            print(f"Role '{roleName}' does not exist.")
            return

        user = self.users[userName]
        role = self.roles[roleName]
        user.addRole(role)

    def checkAccess(self, userName, resourceName, accessName):
        if userName not in self.users:
            return f"User '{userName}' does not exist."
        if resourceName not in self.resources:
            return f"Resource '{resourceName}' does not exist."
        if accessName not in self.accesses:
            return f"Access '{accessName}' does not exist."

        user = self.users[userName]
        # resource = self.resources[resourceName]

        for role in user.roles:
            if resourceName in role.accessMap and accessName in role.accessMap[resourceName]:
                return f"YES, '{userName}' has access to perform '{accessName}' on '{resourceName}'"

        return f"NO, '{userName}' cannot perform '{accessName}' on '{resourceName}'"

    def listAllEntities(self):
        print("Users:")
        for userName in self.users:
            print(f"  {userName}")
        print("\nRoles:")
        for roleName in self.roles:
            print(f"  {roleName}")
        print("\nResources:")
        for resourceName in self.resources:
            print(f"  {resourceName}")
        print("\nAccesses:")
        for accessName in self.accesses:
            print(f"  {accessName}")

def main():
    rbac = RBACSystem()
    print("*****************")
    print(" RBAC CLI System")
    print("*****************")
    while True:
        command = input("> ").strip()
        if command.lower() == "exit":
            break

        parts = command.split()
        if not parts:
            continue

        action = parts[0]

        if action == "addAccess" and len(parts) == 2:
            rbac.addAccess(parts[1])
        elif action == "addResource" and len(parts) == 2:
            rbac.addResource(parts[1])
        elif action == "addRole" and len(parts) == 2:
            rbac.addRole(parts[1])
        elif action == "addUser" and len(parts) == 2:
            rbac.addUser(parts[1])
        elif action == "addAccessOnResource" and len(parts) == 3:
            rbac.addAccessOnResource(parts[1], parts[2])
        elif action == "addAccessOnResourceToRole" and len(parts) == 4:
            rbac.addAccessOnResourceToRole(parts[1], parts[2], parts[3])
        elif action == "addRoleToUser" and len(parts) == 3:
            rbac.addRoleToUser(parts[1], parts[2])
        elif action == "checkAccess" and len(parts) == 4:
            print(rbac.checkAccess(parts[1], parts[2], parts[3]))
        elif action == "listAllEntities":
            rbac.listAllEntities()
        else:
            print("Invalid command or arguments.")
        
        print()


if __name__ == "__main__":
    main()
