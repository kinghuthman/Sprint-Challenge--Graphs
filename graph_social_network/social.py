import random

class User:
    def __init__(self, name):
        self.name = name
        self.color = ''
        self.parent = None

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(1,numUsers+1):
            self.addUser(user)

        # Create friendships
        for user in self.users:
            for friend in range(avgFriendships):
                friend_id = self.get_random_friend_id(user, numUsers)
                if friend_id in self.friendships[user]:
                    continue
                self.addFriendship(user, friend_id)
    def get_random_friend_id(self, user_id, numUsers):
        friend_id = random.randint(1,numUsers)
        if user_id == friend_id:
            return self.get_random_friend_id(user_id, numUsers)
        else:
            return friend_id

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.users:
            self.users[user].color = 'white'
        self.users[userID].color = 'grey'
        queue = [userID]
        path = []
        while len(queue) > 0:
            current = queue[0]
            visited[current] = self.get_path(current)
            for friend in self.friendships[current]:
                if self.users[friend].color == 'white':
                    self.users[friend].color = 'grey'
                    queue.append(friend)
                    self.users[friend].parent = current
            queue.pop(0)
            self.users[current].color = 'black'
        return visited

    def get_path(self, start):
            path = []
            current = start
            while not current == None:
                path.append(current)
                current = self.users[current].parent
            path.reverse()
            return path   



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
