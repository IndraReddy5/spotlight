import requests as req
import random

Admin_User = {"username": "admin", "password": "light123"}

New_Users = [
    {"username": "chris", "email": "chris@spotlight.in", "password": "light123"},
    {"username": "rogers", "email": "rogers@spotlight.in", "password": "light123"},
    {"username": "kanha", "email": "kanha@spotlight.in", "password": "light123"},
    {"username": "dodge", "email": "dodge@spotlight.in", "password": "light123"},
    {"username": "muffin", "email": "muffin@spotlight.in", "password": "light123"},
    {"username": "rick", "email": "rick@spotlight.in", "password": "light123"},
    {"username": "root", "email": "root@spotlight.in", "password": "light123"},
    {"username": "monk", "email": "monk@spotlight.in", "password": "light123"},
    {"username": "shiv", "email": "shiv@spotlight.in", "password": "light123"},
    {"username": "panda", "email": "panda@spotlight.in", "password": "light123"},
    {"username": "sherlock", "email": "sherlock@spotlight.in", "password": "light123"},
    {"username": "john", "email": "john@spotlight.in", "password": "light123"},
    {"username": "samay", "email": "samay@spotlight.in", "password": "light123"},
    {"username": "murad", "email": "murad@spotlight.in", "password": "light123"},
    {"username": "sher", "email": "sher@spotlight.in", "password": "light123"},
    {"username": "crux", "email": "crux@spotlight.in", "password": "light123"},
]

Albums = [
    {
        "user": New_Users[11],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/everything-1586954477-cCET17ui2u.jpg",
        "album_name": "Everything",
        "artists_names": "Diamond Eyes",
        "file_name": "everything.jpg",
    },
    {
        "user": New_Users[11],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/1696583182_QUThTOGvco_Final.jpg",
        "album_name": "Waves",
        "artists_names": "Comma Dee, AC13",
        "file_name": "final.jpg",
    },
    {
        "user": New_Users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/1698141643_Ei0ENTsgvb_DONT-UNDERSTAND---SKETCHEZ---FINAL.png",
        "album_name": "Don't Understand",
        "artists_names": "Sketchez",
        "file_name": "dont_understand.jpg",
    },
    {
        "user": New_Users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/closer-1691625650-ZMrhyher8R.jpg",
        "album_name": "Roy Knox",
        "artists_names": "ROY KNOX",
        "file_name": "closer.jpg",
    },
    {
        "user": New_Users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/cricket-we-nice-1697673648-TXcEQeUxy3.jpg",
        "album_name": "Cricket (We Nice)",
        "artists_names": "ORGAN",
        "file_name": "cricket.jpg",
    },
    {
        "user": New_Users[13],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/fly-away-1586946686-8NxFljjQBy.jpg",
        "album_name": "fly away",
        "artists_names": "Krys Talk",
        "file_name": "fly_away.jpg",
    },
    {
        "user": New_Users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/getaway-1697155249-ZKilSbNXEi.jpg",
        "album_name": "Getaway",
        "artists_names": "Daniel Levi",
        "file_name": "getaway.jpg",
    },
    {
        "user": New_Users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/if-i-disappear-1651831235-G4FMMkdnmR.png",
        "album_name": "if I disappear",
        "artists_names": "Tom Mårtensson, Tobu",
        "file_name": "album_2.jpg",
    },
    {
        "user": New_Users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/running-away-1649325635-ZD22SgM4sM.jpg",
        "album_name": "Running Away",
        "artists_names": "Perk Pietrek, Abstrakt, Shiah Maisel",
        "file_name": "running_away.jpg",
    },
    {
        "user": New_Users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/pressure-fectro-remix-1692835292-QzsG0VBZs7.jpg",
        "album_name": "Grove Pressure (Fectro Remix)",
        "artists_names": "Fectro, Wiguez",
        "file_name": "pressure.jpg",
    },
    {
        "user": New_Users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/slow-down-1641294039-Imxo6qzcGg.jpg",
        "album_name": "Slow Down",
        "artists_names": "JShiah Maisel, Jim Yosef",
        "file_name": "slow_down.jpg",
    },
    {
        "user": New_Users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/take-our-time-1645534832-FSOxrdKCfV.jpg",
        "album_name": "take our time",
        "artists_names": "Tollef",
        "file_name": "take_our_time.jpg",
    },
]

Songs = [
    {
        "user": New_Users[11],
        "album_id": 1,
        "song_name": "Everything",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Diamond Eyes - Everything [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "everything.mp3",
        "lyrics_file_name": "everything.txt",
    },
    {
        "user": New_Users[11],
        "album_id": 1,
        "song_name": "Chime",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Chime - Phototropic [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "chime.mp3",
        "lyrics_file_name": "chime.txt",
    },
    {
        "user": New_Users[11],
        "album_id": 2,
        "song_name": "waves",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/AC13 - Waves Ft. Comma Dee [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "waves.mp3",
        "lyrics_file_name": "waves.txt",
        "song_cover_file_name": "waves.jpg",
        "cover_image_file": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/old-monk_-_alwin.jpeg",
    },
    {
        "user": New_Users[12],
        "album_id": 3,
        "song_name": "don't understand",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Sketchez - Don't Understand [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "dont_understand.mp3",
        "lyrics_file_name": "dont_understand.txt",
    },
    {
        "user": New_Users[12],
        "album_id": 4,
        "song_name": "closer",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/ROY KNOX - Closer [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "closer.mp3",
        "lyrics_file_name": "closer.txt",
    },
    {
        "user": New_Users[12],
        "album_id": 5,
        "song_name": "cricket (we nice)",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/ORGAN - Cricket (we nice) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "cricket.mp3",
        "lyrics_file_name": "cricket.txt",
    },
    {
        "user": New_Users[13],
        "album_id": 6,
        "song_name": "fly away",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Krys Talk - Fly Away [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "fly_away.mp3",
        "lyrics_file_name": "fly_away.txt",
    },
    {
        "user": New_Users[14],
        "album_id": 7,
        "song_name": "river",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Daniel Levi - River [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "river.mp3",
        "lyrics_file_name": "river.txt",
    },
    {
        "user": New_Users[14],
        "album_id": 7,
        "song_name": "that's what make it right",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Daniel Levi - That's What Makes It Right [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "make_it_right.mp3",
        "lyrics_file_name": "make_it_right.txt",
    },
    {
        "user": New_Users[14],
        "album_id": 8,
        "song_name": "if I disappear",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Tobu - If I Disappear (ft. Tom Mårtensson) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "disappear.mp3",
        "lyrics_file_name": "disappear.txt",
    },
    {
        "user": New_Users[14],
        "album_id": 9,
        "song_name": "running away",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Shiah Maisel, Abstrakt, Perk Pietrek - Running Away [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "running_away.mp3",
        "lyrics_file_name": "running_away.txt",
    },
    {
        "user": New_Users[15],
        "album_id": 10,
        "song_name": "gone",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Wiguez - Gone (Feat. Rico 56) (Thorne Remix) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "gone.mp3",
        "lyrics_file_name": "gone.txt",
    },
    {
        "user": New_Users[15],
        "album_id": 10,
        "song_name": "pressure",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Wiguez - Pressure (Fectro Remix) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "pressure.mp3",
        "lyrics_file_name": "pressure.txt",
    },
    {
        "user": New_Users[15],
        "album_id": 11,
        "song_name": "slow down",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Jim Yosef & Shiah Maisel - Slow Down [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "slow_down.mp3",
        "lyrics_file_name": "slow_down.txt",
    },
    {
        "user": New_Users[15],
        "album_id": 12,
        "song_name": "take our time",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Tollef - Take Our Time [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "take_our_time.mp3",
        "lyrics_file_name": "take_our_time.txt",
    },
]

Genres = [
    {"user": New_Users[11], "genre": "indie"},
    {"user": New_Users[11], "genre": "pop"},
    {"user": New_Users[11], "genre": "electronic"},
    {"user": New_Users[11], "genre": "Melodic DubStep"},
    {"user": New_Users[12], "genre": "Future House"},
    {"user": New_Users[12], "genre": "Drum & Bass"},
    {"user": New_Users[13], "genre": "House"},
    {"user": New_Users[14], "genre": "Trap"},
    {"user": New_Users[14], "genre": "Melodic House"},
    {"user": New_Users[15], "genre": "Future Bass"},
    {"user": New_Users[15], "genre": "DubStep"},
    {"user": New_Users[15], "genre": "Progressive House"},
]

Song_Genre = [
    {"user": New_Users[11], "song_id": 1, "genre_id": random.randint(1, 12)},
    {"user": New_Users[11], "song_id": 2, "genre_id": random.randint(1, 12)},
    {"user": New_Users[11], "song_id": 3, "genre_id": random.randint(1, 12)},
    {"user": New_Users[12], "song_id": 4, "genre_id": random.randint(1, 12)},
    {"user": New_Users[12], "song_id": 5, "genre_id": random.randint(1, 12)},
    {"user": New_Users[12], "song_id": 6, "genre_id": random.randint(1, 12)},
    {"user": New_Users[13], "song_id": 7, "genre_id": random.randint(1, 12)},
    {"user": New_Users[14], "song_id": 8, "genre_id": random.randint(1, 12)},
    {"user": New_Users[14], "song_id": 9, "genre_id": random.randint(1, 12)},
    {"user": New_Users[14], "song_id": 10, "genre_id": random.randint(1, 12)},
    {"user": New_Users[14], "song_id": 11, "genre_id": random.randint(1, 12)},
    {"user": New_Users[15], "song_id": 12, "genre_id": random.randint(1, 12)},
    {"user": New_Users[15], "song_id": 13, "genre_id": random.randint(1, 12)},
    {"user": New_Users[15], "song_id": 14, "genre_id": random.randint(1, 12)},
    {"user": New_Users[15], "song_id": 15, "genre_id": random.randint(1, 12)},
]

Playlists = [
    {"user": New_Users[0], "playlist_name": "bot_play"},
    {"user": New_Users[0], "playlist_name": "lofi"},
    {"user": New_Users[1], "playlist_name": "chill"},
    {"user": New_Users[1], "playlist_name": "rock"},
    {"user": New_Users[2], "playlist_name": "pop"},
    {"user": New_Users[2], "playlist_name": "edm"},
    {"user": New_Users[3], "playlist_name": "hiphop"},
    {"user": New_Users[3], "playlist_name": "rap"},
    {"user": New_Users[4], "playlist_name": "jazz"},
    {"user": New_Users[4], "playlist_name": "country"},
    {"user": New_Users[5], "playlist_name": "metal"},
    {"user": New_Users[5], "playlist_name": "classical"},
    {"user": New_Users[6], "playlist_name": "soul"},
    {"user": New_Users[6], "playlist_name": "rnb"},
    {"user": New_Users[7], "playlist_name": "Electronic"},
    {"user": New_Users[7], "playlist_name": "Dance"},
    {"user": New_Users[8], "playlist_name": "Folk"},
    {"user": New_Users[8], "playlist_name": "DubStep"},
    {"user": New_Users[9], "playlist_name": "Blues"},
    {"user": New_Users[9], "playlist_name": "Funk"},
    {"user": New_Users[10], "playlist_name": "Disco"},
    {"user": New_Users[10], "playlist_name": "Techno"},
]

Playlist_Songs = [
    {"user": New_Users[0], "playlist_id": 1, "song_id": random.randint(1, 15)},
    {"user": New_Users[0], "playlist_id": 1, "song_id": random.randint(1, 15)},
    {"user": New_Users[0], "playlist_id": 1, "song_id": random.randint(1, 15)},
    {"user": New_Users[0], "playlist_id": 2, "song_id": random.randint(1, 15)},
    {"user": New_Users[0], "playlist_id": 2, "song_id": random.randint(1, 15)},
    {"user": New_Users[0], "playlist_id": 2, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 3, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 3, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 3, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 4, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 4, "song_id": random.randint(1, 15)},
    {"user": New_Users[1], "playlist_id": 4, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 5, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 5, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 5, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 6, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 6, "song_id": random.randint(1, 15)},
    {"user": New_Users[2], "playlist_id": 6, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 7, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 7, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 7, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 8, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 8, "song_id": random.randint(1, 15)},
    {"user": New_Users[3], "playlist_id": 8, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 9, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 9, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 9, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 10, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 10, "song_id": random.randint(1, 15)},
    {"user": New_Users[4], "playlist_id": 10, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 11, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 11, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 11, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 12, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 12, "song_id": random.randint(1, 15)},
    {"user": New_Users[5], "playlist_id": 12, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 13, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 13, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 13, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 14, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 14, "song_id": random.randint(1, 15)},
    {"user": New_Users[6], "playlist_id": 14, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 15, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 15, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 15, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 16, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 16, "song_id": random.randint(1, 15)},
    {"user": New_Users[7], "playlist_id": 16, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 17, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 17, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 17, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 18, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 18, "song_id": random.randint(1, 15)},
    {"user": New_Users[8], "playlist_id": 18, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 19, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 19, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 19, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 20, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 20, "song_id": random.randint(1, 15)},
    {"user": New_Users[9], "playlist_id": 20, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 21, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 21, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 21, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 22, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 22, "song_id": random.randint(1, 15)},
    {"user": New_Users[10], "playlist_id": 22, "song_id": random.randint(1, 15)},
]

Reviews = [
    {
        "user": New_Users[0],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[0],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[1],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[1],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[2],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[2],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[3],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[3],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[4],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[4],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[5],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[5],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[6],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[6],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[7],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[7],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[8],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[8],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[9],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[9],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[10],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
    {
        "user": New_Users[10],
        "song_id": random.randint(1, 15),
        "rating": random.randint(1, 5),
    },
]

Album_Flags = [
    {
        "user": New_Users[random.randint(1, 10)],
        "album_id": random.randint(1, 12),
        "reason": "Inappropriate",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "album_id": random.randint(1, 12),
        "reason": "Not Suitable for this platform",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "album_id": random.randint(1, 12),
        "reason": "Copyright Infringement",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "album_id": random.randint(1, 12),
        "reason": "Song is not in English",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "album_id": random.randint(1, 12),
        "reason": "Song isn't worthy of this platform",
    },
]

Song_Flags = [
    {
        "user": New_Users[random.randint(1, 10)],
        "song_id": random.randint(1, 15),
        "reason": "Inappropriate",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "song_id": random.randint(1, 15),
        "reason": "Not Suitable for this platform",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "song_id": random.randint(1, 15),
        "reason": "Copyright Infringement",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "song_id": random.randint(1, 15),
        "reason": "Song is not in English",
    },
    {
        "user": New_Users[random.randint(1, 10)],
        "song_id": random.randint(1, 15),
        "reason": "Song isn't worthy of this platform",
    },
]


# Helper Function for login
def get_auth_token(user):
    auth_token = req.post(
        "http://localhost:8000/api/login?include_auth_token", json=user
    ).json()["response"]["user"]["authentication_token"]
    return auth_token


# Helper Function for to make json headers with login token
def make_header(user):
    headers = {"Content-Type": "application/json", "Auth-Token": get_auth_token(user)}
    return headers


# Helper Function for creating a new album
def create_album(user, album_cover_path, album_name, artists_names, file_name):
    headers = make_header(user)
    form_data = {
        "album_name": album_name,
        "artists_names": artists_names,
    }
    files = {
        "cover_image": (file_name, open(album_cover_path, "rb"), "image/png"),
    }
    call = req.post(
        "http://localhost:8000/api/creator/album/new",
        data=form_data,
        files=files,
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(f"{album_name} album has been created")
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for adding a new song
def add_song(
    user,
    album_id,
    song_name,
    audio_file_path,
    lyrics_file_path,
    song_file_name,
    lyrics_file_name,
    song_cover_file_name=None,
    cover_image_file=None,
):
    headers = make_header(user)
    form_data = {
        "album_id": album_id,
        "song_name": song_name,
    }
    files = {
        "audio_file": (song_file_name, open(audio_file_path, "rb"), "image/png"),
        "lyrics_file": (lyrics_file_name, open(lyrics_file_path, "rb"), "image/png"),
    }
    if song_cover_file_name and cover_image_file:
        files["cover_image"] = (
            song_cover_file_name,
            open(cover_image_file, "rb"),
            "image/png",
        )
    call = req.post(
        "http://localhost:8000/api/creator/song/new",
        data=form_data,
        files=files,
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(
            f"{song_name} song has been added to {Albums[album_id-1]['album_name']} album"
        )
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for adding a new genre
def add_genre(user, genre):
    headers = make_header(user)
    call = req.post(
        "http://localhost:8000/api/creator/genre/new",
        json={"genre": genre},
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(f"{genre} genre has been added to database")
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for adding songs genre
def add_song_genre(user, song_id, genre_id):
    headers = make_header(user)
    try:
        call = req.post(
            f"http://localhost:8000/api/creator/song/{song_id}/add/genre/{genre_id}",
            headers={"Auth-Token": headers["Auth-Token"]},
        )
        call.raise_for_status()
        if call.status_code == 200:
            print(
                f"{Genres[genre_id-1]['genre']} genre has been added to {Songs[song_id-1]['song_name']} song"
            )
    except req.exceptions.HTTPError as err:
        print(err.args[0])
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for creating a new playlist
def add_playlist(user, playlist_name):
    headers = make_header(user)
    call = req.post(
        "http://localhost:8000/api/playlist/new",
        json={"playlist_name": playlist_name},
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(f"{playlist_name} playlist has been created")
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for adding songs to playlist
def add_song_playlist(user, playlist_id, song_id):
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/playlist/{playlist_id}/add/{song_id}",
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(
            f"{Songs[song_id-1]['song_name']} song has been added to {Playlists[playlist_id-1]['playlist_name']} playlist"
        )
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for adding user rating to songs
def add_rating(user, song_id, rating):
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/song/{song_id}/rating",
        json={"rating": rating},
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(
            f"{Songs[song_id-1]['song_name']} song has been rated {rating} by {user['username']}"
        )
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for flagging a Album
def flag_album(user, album_id, reason):
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/flag/album/{album_id}",
        json={"reason": reason},
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(
            f"{Albums[album_id-1]['album_name']} album has been flagged by {user['username']}"
        )
    req.post("http://localhost:8000/api/logout", headers=headers)


# Helper Function for flagging a Song
def flag_song(user, song_id, reason):
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/flag/song/{song_id}",
        json={"reason": reason},
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    if call.status_code == 200:
        print(
            f"{Songs[song_id-1]['song_name']} album has been flagged by {user['username']}"
        )
    req.post("http://localhost:8000/api/logout", headers=headers)


## adding New Users
for user in New_Users:
    call = req.post(
        "http://localhost:8000/api/signup",
        json=user,
        headers={"Content-Type": "application/json"},
    )
    if call.status_code == 200:
        print(f"{user['username']} has been added")

## Making John, Samay, crux, Sher, Murad as Creators
for user in New_Users[11:]:
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/creator/signup/{user['username']}", headers=headers
    )
    if call.status_code == 200:
        print(f"{user['username']} is creator now")
    req.post("http://localhost:8000/api/logout", headers=headers)

## Making Root, Monk, Shiv, Panda, Sherlock as patrons
for user in New_Users[6:11]:
    headers = make_header(user)
    call = req.post(
        f"http://localhost:8000/api/patron/{user['username']}/subscribe",
        headers=headers,
    )
    if call.status_code == 200:
        print(f"{user['username']} is patron now")
    req.post("http://localhost:8000/api/logout", headers=headers)


## Creating new albums
for album in Albums:
    create_album(**album)

## Creating new songs and adding them to albums
for song in Songs:
    add_song(**song)

## Making Genres
for genre in Genres:
    add_genre(**genre)

## Approving song genres by admin
for num in range(1, len(Genres), 2):
    headers = make_header(Admin_User)
    call = req.post(
        f"http://localhost:8000/api/admin/genre",
        json={"genre_id": num, "admin_approval": "Yes"},
        headers=headers,
    )
    if call.status_code == 200:
        print(f"{Genres[num]['genre']} genre has been approved by admin")
    req.post("http://localhost:8000/api/logout", headers=headers)

## Adding song genres
for song_genre in Song_Genre:
    add_song_genre(**song_genre)

## creating playlists
for playlist in Playlists:
    add_playlist(**playlist)

## Adding songs to playlists
for playlist_song in Playlist_Songs:
    add_song_playlist(**playlist_song)

## Adding user ratings on songs
for review in Reviews:
    add_rating(**review)

## Flagging some songs
for song_flag in Song_Flags:
    flag_song(**song_flag)

## Marking some song flags as read by Admin
for num in range(1, len(Song_Flags), 2):
    headers = make_header(Admin_User)
    call = req.post(
        f"http://localhost:8000/api/admin/flags",
        json={"flag_type": "song", "flag_id": num},
        headers=headers,
    )
    if call.status_code == 200:
        print(f"{num} song flag has been read by Admin")
    req.post("http://localhost:8000/api/logout", headers=headers)

## Flagging some albums
for album_flag in Album_Flags:
    flag_album(**album_flag)

## Marking some album flags as read by Admin
for num in range(1, len(Album_Flags), 2):
    headers = make_header(Admin_User)
    call = req.post(
        f"http://localhost:8000/api/admin/flags",
        json={"flag_type": "album", "flag_id": num},
        headers=headers,
    )
    if call.status_code == 200:
        print(f"{num} album flag has been read by Admin")
    req.post("http://localhost:8000/api/logout", headers=headers)