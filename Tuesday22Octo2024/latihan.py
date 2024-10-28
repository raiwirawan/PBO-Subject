# Dikarenakan keterbatasan waktu, kami hanya dapat membuat sedikit saja pak

class User:
    def __init__(self, user_id, username, email, password, is_youtube_premium = False, is_logged_in = False):
        self.__user_id = user_id
        self.__username = username
        self.email = email
        self.__password = password,
        self.__is_youtube_premium = bool(is_youtube_premium)
        self.__is_logged_in = bool(is_logged_in)

    def get_user_id(self):
        return self.__user_id
    
    def get_username(self):
        return self.__username
    
    def set_username(self, new_username):
        self.__username = new_username
    
    def set_password(self, new_password):
        self.__password = new_password

    def get_password(self):
        return hash(self.__password)

    def set_premium_status(self, new_status):
        if not bool(new_status):
            return 'Setting premium status failed!'
        self.__is_youtube_premium = bool(new_status)

    def get_premium_status(self):
        return self.__is_youtube_premium
    
    # metode-metode aksi yang bisa dilakukan

    def login(self):
        self.__is_logged_in = True
        return 'You are logged in!'

    def logout(self):
        self.__is_logged_in = False
        return 'You are logged out!'
    
    def upload_video(self, video_name):
        return f'{self.__username} has uploaded {video_name} video'
    
    def delete_video():
        pass

# user = User('adnAkHsFudSfs21', 'ramadenpasar1', 'ramadenpasar01@gmail.com', 'ramalawak123', False)

class Admin(User):
    def __init__(self, user_id, username, email, password, is_youtube_premium=False, is_logged_in=False):
        super().__init__(user_id, username, email, password, is_youtube_premium, is_logged_in)

    def delete_video(self, video_id):
        return f'YouTube Admin has deleted {self.get_username()} user {video_id} video!'

# admin = Admin('adnAkHsFudSfs21', 'ramadenpasar1', 'ramadenpasar01@gmail.com', 'ramalawak123', False)
# print(admin.delete_video('lawakan hari ini'))

class RegularUser(User):
    def __init__(self, user_id, username, email, password, is_youtube_premium=False, is_logged_in=False):
        super().__init__(user_id, username, email, password, is_youtube_premium, is_logged_in)

    def subscribe(self, channel_id):
        return f'{self.get_username()} subscribed {channel_id} channel!'

# regular_user = RegularUser('adnAkHsFudSfs21', 'ramadenpasar1', 'ramadenpasar01@gmail.com', 'ramalawak123', False)
# print(regular_user.subscribe('ramangelawak_official'))

class Video:
    def __init__(self, video_id, video_title, video_description, channel_id, user_id):
        self.__video_id = video_id
        self.video_title = video_title
        self.video_description = video_description
        self.channel_id = channel_id
        self.user_id = user_id

    def get_video_id(self):
        return self.__video_id
    
    def play(self):
        return f"Playing {self.video_title} video!"
    
class LiveStreamVideo(Video):
    def __init__(self, video_id, video_title, video_description, channel_id, user_id):
        super().__init__(video_id, video_title, video_description, channel_id, user_id)

    def play(self):
        return f"Playing {self.video_title} live stream video!"

class Playlist:
    def __init__(self, playlist_id, playlist_name, playlist_url, channel_id, user_id, is_public):
        self.__playlist_id = playlist_id
        self.__playlist_name = playlist_name
        self.__playlist_url = playlist_url
        self.__channel_id = channel_id
        self.__user_id = user_id
        self.__video_list = []
        self.__is_public = bool(is_public)

    def add_video_to_playlist(self, video_id):
        self.__video_list.append(video_id)
        return self.__video_list
    
    def delete_video_from_playlist(self, video_id):
        self.__video_list[:-1]
        return self.__video_list

playlist = Playlist()