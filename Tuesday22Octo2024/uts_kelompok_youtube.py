class User:
    def __init__(self, username, email):
        # Konstruktor kelas User, digunakan untuk menginisialisasi objek User baru.
        self.__username = username  # Enkapsulasi: menyimpan username dengan akses terbatas (private).
        self.__email = email  # Enkapsulasi: menyimpan email dengan akses terbatas (private).
        self.__subscribed_channels = []  # Enkapsulasi: menyimpan daftar channel yang disubscribed dengan akses terbatas (private).
    
    def get_username(self):
        # Metode untuk mendapatkan username pengguna.
        return self.__username  # Mengembalikan nilai username.

    def set_username(self, new_username):
        # Metode untuk mengubah username pengguna.
        self.__username = new_username  # Mengupdate nilai username dengan yang baru.

    def subscribe(self, channel):
        # Metode untuk menambahkan channel ke daftar langganan pengguna.
        self.__subscribed_channels.append(channel)  # Menambahkan channel ke dalam daftar subscribed_channels.

    def unsubscribe(self, channel):
        # Metode untuk menghapus channel dari daftar langganan pengguna.
        self.__subscribed_channels.remove(channel)  # Menghapus channel dari daftar subscribed_channels.

    def upload_video(self, video_title):
        # Metode untuk mengupload video oleh pengguna.
        print(f"{self.__username} uploaded a video: {video_title}")  # Menampilkan pesan yang menunjukkan video yang diupload oleh pengguna.


class Video:
    def __init__(self, title, description):
        # Konstruktor kelas Video, digunakan untuk menginisialisasi objek Video baru.
        self.__title = title  # Enkapsulasi: menyimpan judul video dengan akses terbatas (private).
        self.__description = description  # Enkapsulasi: menyimpan deskripsi video dengan akses terbatas (private).
        self.__views = 0  # Enkapsulasi: menghitung jumlah tampilan video, diinisialisasi dengan 0.
        self.__likes = 0  # Enkapsulasi: menghitung jumlah suka video, diinisialisasi dengan 0.
        self.__dislikes = 0  # Enkapsulasi: menghitung jumlah tidak suka video, diinisialisasi dengan 0.

    def play(self):
        # Metode untuk memutar video.
        self.__views += 1  # Meningkatkan jumlah tampilan video setiap kali video diputar.
        print(f"Playing video: {self.__title}")  # Menampilkan pesan saat video diputar.

    def like(self):
        # Metode untuk menyukai video.
        self.__likes += 1  # Meningkatkan jumlah suka video setiap kali video disukai.
        print(f"Liked video: {self.__title}")  # Menampilkan pesan saat video disukai.

    def dislike(self):
        # Metode untuk tidak menyukai video.
        self.__dislikes += 1  # Meningkatkan jumlah tidak suka video setiap kali video tidak disukai.
        print(f"Disliked video: {self.__title}")  # Menampilkan pesan saat video tidak disukai.

    def get_info(self):
        # Metode untuk mendapatkan informasi video dalam bentuk dictionary.
        return {
            "title": self.__title,  # Mengembalikan judul video.
            "description": self.__description,  # Mengembalikan deskripsi video.
            "views": self.__views,  # Mengembalikan jumlah tampilan video.
            "likes": self.__likes,  # Mengembalikan jumlah suka video.
            "dislikes": self.__dislikes  # Mengembalikan jumlah tidak suka video.
        }


class Channel:
    def __init__(self, name, owner):
        # Konstruktor kelas Channel, digunakan untuk menginisialisasi objek Channel baru.
        self.__name = name  # Enkapsulasi: menyimpan nama channel dengan akses terbatas (private).
        self.__owner = owner  # Enkapsulasi: menyimpan pemilik channel dengan akses terbatas (private).
        self.__videos = []  # Enkapsulasi: menyimpan daftar video yang diupload ke channel, diinisialisasi sebagai list kosong.

    def upload_video(self, video):
        # Metode untuk mengupload video ke channel.
        self.__videos.append(video)  # Menambahkan video ke dalam daftar __videos.
        self.__owner.upload_video(video)  # Memanggil metode upload_video dari pemilik channel untuk mencatat upload.

    def get_videos(self):
        # Metode untuk mendapatkan daftar informasi video yang diupload ke channel.
        return [video.get_info() for video in self.__videos]  # Mengembalikan informasi setiap video dalam bentuk list.
    
class Comment:
    def __init__(self, user, video, content):
        # Konstruktor kelas Comment, digunakan untuk menginisialisasi objek Comment baru.
        self.__user = user  # Enkapsulasi: menyimpan pengguna yang membuat komentar dengan akses terbatas (private).
        self.__video = video  # Enkapsulasi: menyimpan video yang dikomentari dengan akses terbatas (private).
        self.__content = content  # Enkapsulasi: menyimpan isi komentar dengan akses terbatas (private).
        self.__likes = 0  # Enkapsulasi: menghitung jumlah suka pada komentar, diinisialisasi dengan 0.
        self.__timestamp = self.__get_timestamp()  # Enkapsulasi: menyimpan waktu pembuatan komentar dengan akses terbatas (private).

    def __get_timestamp(self):
        # Metode private untuk mendapatkan waktu saat komentar dibuat.
        import datetime  # Mengimpor modul datetime untuk mendapatkan waktu saat ini.
        return datetime.datetime.now()  # Mengembalikan waktu saat ini.

    def like(self):
        # Metode untuk menyukai komentar.
        self.__likes += 1  # Meningkatkan jumlah suka komentar setiap kali metode like dipanggil.
        print(f"Comment liked: {self.__content}")  # Menampilkan pesan saat komentar disukai.

    def get_info(self):
        # Metode untuk mendapatkan informasi tentang komentar dalam bentuk dictionary.
        return {
            "user": self.__user,  # Mengembalikan pengguna yang membuat komentar.
            "content": self.__content,  # Mengembalikan isi komentar.
            "likes": self.__likes,  # Mengembalikan jumlah suka komentar.
            "timestamp": self.__timestamp  # Mengembalikan waktu pembuatan komentar.
        }


class Playlist:
    #konstruktor kelas playlist digunakan untuk menginisialisasi objek Playlist dengan nama playlist
    def __init__(self, name):
        self.__name = name  # Enkapsulasi: atribut private untuk menyimpan nama playlist
        self.__videos = []  # Enkapsulasi: atribut private untuk menyimpan daftar video

    def get_name(self):
        # Getter untuk mendapatkan nama playlist (akses terbatas melalui metode publik)
        return self.__name
    
    def set_name(self, new_name):
        # Setter untuk mengubah nama playlist (akses terbatas melalui metode publik)
        self.__name = new_name

    def add_video(self, video):
        # Metode untuk menambahkan video ke playlist
        self.__videos.append(video) # Enkapsulasi: menambah objek video ke daftar video (private)
        print(f"Added video: {video.get_info()['title']} to playlist: {self.__name}")

    def remove_video(self, video):
         # Metode untuk menghapus video dari playlist
        self.__videos.remove(video) # Enkapsulasi: menghapus objek video dari daftar video (private)
        print(f"Removed video: {video.get_info()['title']} from playlist: {self.__name}")

    def get_videos(self):
         # Menggunakan list comprehension untuk mengembalikan daftar informasi video (dictionary)
        return [video.get_info() for video in self.__videos]


class Video:
    # Konstruktor untuk menginisialisasi objek Video dengan judul dan deskripsi
    def __init__(self, title, description):
        self.__title = title   # Enkapsulasi: atribut private untuk judul video
        self.__description = description  # Enkapsulasi: atribut private untuk deskripsi video
        self.__views = 0  # Enkapsulasi: atribut private untuk jumlah penayangan video
        self.__likes = 0  # Enkapsulasi: atribut private untuk jumlah likes video
        self.__dislikes = 0  # Enkapsulasi: atribut private untuk jumlah dislikes video

    def play(self):
         # Metode untuk memainkan video, meningkatkan jumlah penayangan setiap kali diputar
        self.__views += 1 # Enkapsulasi: menambah jumlah penayangan (private)
        print(f"Playing video: {self.__title}")

    def like(self):
         # Metode untuk menyukai video, meningkatkan jumlah likes
        self.__likes += 1 # Enkapsulasi: menambah jumlah likes (private)
        print(f"Liked video: {self.__title}")

    def dislike(self):
        # Metode untuk tidak menyukai video, meningkatkan jumlah dislikes
        self.__dislikes += 1 # Enkapsulasi: menambah jumlah dislikes (private)
        print(f"Disliked video: {self.__title}")

    def get_info(self):
        # Metode untuk mendapatkan informasi lengkap tentang video dalam bentuk dictionary
        return {
            "title": self.__title,
            "description": self.__description,
            "views": self.__views,
            "likes": self.__likes,
            "dislikes": self.__dislikes
        }


class LiveStream(Video):  # Pewarisan dari kelas Video
    def __init__(self, title, description, stream_url):
        super().__init__(title, description)  # Memanggil konstruktor kelas induk
        self.__stream_url = stream_url  # Enkapsulasi
        self.__is_live = False  # Enkapsulasi

    def start_stream(self):
        self.__is_live = True
        print(f"Live stream started: {self.get_info()['title']} at {self.__stream_url}")

    def end_stream(self):
        self.__is_live = False
        print(f"Live stream ended: {self.get_info()['title']}")

    def play(self):
        if self.__is_live:
            print(f"Streaming live: {self.get_info()['title']}")
        else:
            print(f"Cannot play, the stream is not live.")

class ShortVideo(Video):  # Pewarisan dari kelas Video
    def __init__(self, title, description, duration):
        super().__init__(title, description)  # Memanggil konstruktor kelas induk
        self.__duration = duration  # Enkapsulasi

    def get_info(self):
        info = super().get_info()  # Mengambil info dari kelas induk
        info['duration'] = self.__duration
        return info


class TutorialVideo(Video):  # Pewarisan dari kelas Video
    def __init__(self, title, description, difficulty_level):
        super().__init__(title, description)  # Memanggil konstruktor kelas induk
        self.__difficulty_level = difficulty_level  # Enkapsulasi

    def get_info(self):
        info = super().get_info()  # Mengambil info dari kelas induk
        info['difficulty_level'] = self.__difficulty_level
        return info


class PremiumUser(User):  # Pewarisan dari kelas User
    def __init__(self, username, email, subscription_type):
        super().__init__(username, email)  # Memanggil konstruktor kelas induk
        self.__subscription_type = subscription_type  # Enkapsulasi

    def get_subscription_info(self):
        return f"{self.get_username()} has a {self.__subscription_type} subscription."


class ReplyComment(Comment):  # Pewarisan dari kelas Comment
    def __init__(self, user, video, content, parent_comment):
        super().__init__(user, video, content)  # Memanggil konstruktor kelas induk
        self.__parent_comment = parent_comment  # Enkapsulasi

    def get_info(self):
        info = super().get_info()  # Mengambil info dari kelas induk
        info['parent_comment'] = self.__parent_comment.get_info()  # Menyertakan info komentar induk
        return info

class Reaction(Comment):  # Pewarisan dari kelas Comment
    def __init__(self, user, video, reaction_type):
        super().__init__(user, video, "")  # Memanggil konstruktor kelas induk
        self.__reaction_type = reaction_type  # Enkapsulasi

    def get_info(self):
        info = super().get_info()  # Mengambil info dari kelas induk
        info['reaction_type'] = self.__reaction_type
        return info


class Vlog(Video):  # Pewarisan dari kelas Video
    def __init__(self, title, description, location, vlog_date):
        super().__init__(title, description)  # Memanggil konstruktor kelas induk
        self.__location = location  # Enkapsulasi
        self.__vlog_date = vlog_date  # Enkapsulasi

    def get_info(self):
        info = super().get_info()  # Mengambil info dari kelas induk
        info['location'] = self.__location
        info['vlog_date'] = self.__vlog_date
        return info


class ChannelSubscription(Playlist):  # Pewarisan dari kelas Playlist
    def __init__(self, name, subscription_date):
        super().__init__(name)  # Memanggil konstruktor kelas induk
        self.__subscription_date = subscription_date  # Enkapsulasi

    def get_info(self):
        info = super().get_videos()  # Mengambil info dari kelas induk
        return {
            "playlist_name": self.get_name(),
            "subscription_date": self.__subscription_date,
            "videos": info
        }


class AdminUser(User):  # Pewarisan dari kelas User
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)  # Memanggil konstruktor kelas induk
        self.__admin_level = admin_level  # Enkapsulasi

    def get_admin_info(self):
        return f"{self.get_username()} is an admin with level {self.__admin_level}."



admin_user = AdminUser ("admin_jane", "admin_jane@example.com", "Super Admin")
print(admin_user.get_admin_info())

vlog = Vlog("My Travel Vlog", "Exploring the beautiful mountains.", "Mount Everest", "2023-10-01")
vlog.play()
print(vlog.get_info())

reaction1 = Reaction("john_doe", vlog.get_info()['title'], "love")
print(reaction1.get_info())

channel_subscription = ChannelSubscription("My Favorite Channels", "2023-10-01")
channel_subscription.add_video(vlog)
print(channel_subscription.get_info())


premium_user = PremiumUser ("jane_doe", "jane@example.com", "Gold")
print(premium_user.get_subscription_info())

short_video = ShortVideo("Short Clip", "A quick short video.", "1:30")
short_video.play()
print(short_video.get_info())

tutorial_video = TutorialVideo("Python Tutorial", "Learn Python programming.", "Beginner")
tutorial_video.play()
print(tutorial_video.get_info())

# Contoh komentar dan balasan
comment1 = Comment("john_doe", short_video.get_info()['title'], "Nice short video!")
reply_comment = ReplyComment("jane_doe", short_video.get_info()['title'], "I agree!", comment1)
print(reply_comment.get_info())


user1 = User("john_doe", "john@example.com")
channel1 = Channel("John's Channel", user1)

video1 = Video("My First Video", "This is my first video on YouTube.")
channel1.upload_video(video1)

comment1 = Comment(user1.get_username(), video1.get_info()['title'], "Great video!")
comment1.like()
print(comment1.get_info())



user1 = User("john_doe", "john@example.com")
channel1 = Channel("John's Channel", user1)

video1 = Video("My First Video", "This is my first video on YouTube.")
channel1.upload_video(video1)

video1.play()
video1.like()
video_info = video1.get_info()
print(video_info)

user1.subscribe(channel1)