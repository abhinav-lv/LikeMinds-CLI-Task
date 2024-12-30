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
    print("*****************\n")
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
        elif action == "listAllEntities":
            rbac.listAllEntities()
        else:
            print("Invalid command or arguments.")


if __name__ == "__main__":
    main()
