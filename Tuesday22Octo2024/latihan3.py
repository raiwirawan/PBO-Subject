class User:
    def __init__(self, username):
        self.username = username
        self.subscriptions = []
    
    def subscribe(self, channel):
        self.subscriptions.append(channel)
        channel.add_subscriber(self)

    def watch_video(self, video):
        print(f"{self.username} is watching {video.title}")

class Video:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def display_comments(self):
        for comment in self.comments:
            print(comment)

class Channel:
    def __init__(self, name):
        self.name = name
        self.videos = []
        self.subscribers = []

    def upload_video(self, video):
        self.videos.append(video)

    def add_subscriber(self, user):
        self.subscribers.append(user)

class Comment:
    def __init__(self, user, content):
        self.user = user
        self.content = content

    def __str__(self):
        return f"{self.user.username}: {self.content}"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat pengguna
    user1 = User("Alice")
    user2 = User("Bob")

    # Membuat channel
    channel1 = Channel("Tech Reviews")

    # Membuat video
    video1 = Video("Python OOP Tutorial", "Learn about OOP concepts in Python.")
    
    # Mengunggah video ke channel
    channel1.upload_video(video1)

    # Pengguna berlangganan ke channel
    user1.subscribe(channel1)
    
    # Pengguna menonton video
    user1.watch_video(video1)

    # Menambahkan komentar ke video
    comment1 = Comment(user1, "Great tutorial!")
    video1.add_comment(comment1)

    # Menampilkan komentar
    video1.display_comments()