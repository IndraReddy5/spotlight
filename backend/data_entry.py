import requests as req

admin_user = {"username": "admin", "password": "light123"}

new_users = [
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


def get_auth_token(user):
    auth_token = req.post(
        "http://localhost:8000/api/login?include_auth_token", json=user
    ).json()["response"]["user"]["authentication_token"]
    return auth_token


def make_header(user):
    headers = {"Content-Type": "application/json", "Auth-Token": get_auth_token(user)}
    return headers


for user in new_users:
    req.post(
        "http://localhost:8000/api/signup",
        json=user,
        headers={"Content-Type": "application/json"},
    )

# Making John, Samay, crux, Sher, Murad as Creators
for user in new_users[11:]:
    headers = make_header(user)
    print(f"{user['username']} is creator now")
    req.post(
        f"http://localhost:8000/api/creator/signup/{user['username']}", headers=headers
    )
    req.post("http://localhost:8000/api/logout", headers=headers)

## Making Root, Monk, Shiv, Panda, Sherlock as patrons
for user in new_users[6:11]:
    headers = make_header(user)
    print(f"{user['username']} is patron now")
    req.post(
        f"http://localhost:8000/api/patron/{user['username']}/subscribe",
        headers=headers,
    )
    req.post("http://localhost:8000/api/logout", headers=headers)


## Making Genres


## Creating new albums
def create_album(user, album_cover_path, album_name, artists_names, file_name):
    headers = make_header(user)
    form_data = {
        "album_name": album_name,
        "artists_names": artists_names,
    }
    files = {
        "cover_image": (file_name, open(album_cover_path, "rb"), "image/png"),
    }
    req.post(
        "http://localhost:8000/api/creator/album/new",
        data=form_data,
        files=files,
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    req.post("http://localhost:8000/api/logout", headers=headers)


Albums = [
    {
        "user": new_users[11],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/everything-1586954477-cCET17ui2u.jpg",
        "album_name": "Everything",
        "artists_names": "Diamond Eyes",
        "file_name": "everything.jpg",
    },
    {
        "user": new_users[11],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/1696583182_QUThTOGvco_Final.jpg",
        "album_name": "Waves",
        "artists_names": "Comma Dee, AC13",
        "file_name": "final.jpg",
    },
    {
        "user": new_users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/1698141643_Ei0ENTsgvb_DONT-UNDERSTAND---SKETCHEZ---FINAL.png",
        "album_name": "Don't Understand",
        "artists_names": "Sketchez",
        "file_name": "dont_understand.jpg",
    },
    {
        "user": new_users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/closer-1691625650-ZMrhyher8R.jpg",
        "album_name": "Roy Knox",
        "artists_names": "ROY KNOX",
        "file_name": "closer.jpg",
    },
    {
        "user": new_users[12],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/cricket-we-nice-1697673648-TXcEQeUxy3.jpg",
        "album_name": "Cricket (We Nice)",
        "artists_names": "ORGAN",
        "file_name": "cricket.jpg",
    },
    {
        "user": new_users[13],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/fly-away-1586946686-8NxFljjQBy.jpg",
        "album_name": "fly away",
        "artists_names": "Krys Talk",
        "file_name": "fly_away.jpg",
    },
    {
        "user": new_users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/getaway-1697155249-ZKilSbNXEi.jpg",
        "album_name": "Getaway",
        "artists_names": "Daniel Levi",
        "file_name": "getaway.jpg",
    },
    {
        "user": new_users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/if-i-disappear-1651831235-G4FMMkdnmR.png",
        "album_name": "if I disappear",
        "artists_names": "Tom Mårtensson, Tobu",
        "file_name": "album_2.jpg",
    },
    {
        "user": new_users[14],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/running-away-1649325635-ZD22SgM4sM.jpg",
        "album_name": "Running Away",
        "artists_names": "Perk Pietrek, Abstrakt, Shiah Maisel",
        "file_name": "running_away.jpg",
    },
    {
        "user": new_users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Cover_Images/pressure-fectro-remix-1692835292-QzsG0VBZs7.jpg",
        "album_name": "Grove Pressure (Fectro Remix)",
        "artists_names": "Fectro, Wiguez",
        "file_name": "pressure.jpg",
    },
    {
        "user": new_users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/slow-down-1641294039-Imxo6qzcGg.jpg",
        "album_name": "Slow Down",
        "artists_names": "JShiah Maisel, Jim Yosef",
        "file_name": "slow_down.jpg",
    },
    {
        "user": new_users[15],
        "album_cover_path": "/home/monk/spotlight/backend/static/Test_Album_Song_Cover_Images/take-our-time-1645534832-FSOxrdKCfV.jpg",
        "album_name": "take our time",
        "artists_names": "Tollef",
        "file_name": "take_our_time.jpg",
    },
]

for album in Albums:
    create_album(**album)
    print(f"{album['album_name']} created")


## Creating new songs and adding them to albums


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
    req.post(
        "http://localhost:8000/api/creator/song/new",
        data=form_data,
        files=files,
        headers={"Auth-Token": headers["Auth-Token"]},
    )
    req.post("http://localhost:8000/api/logout", headers=headers)


songs = [
    {
        "user": new_users[11],
        "album_id": 1,
        "song_name": "Everything",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Diamond Eyes - Everything [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "everything.mp3",
        "lyrics_file_name": "everything.txt",
    },
    {
        "user": new_users[11],
        "album_id": 1,
        "song_name": "Chime",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Chime - Phototropic [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "chime.mp3",
        "lyrics_file_name": "chime.txt",
    },
    {
        "user": new_users[11],
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
        "user": new_users[12],
        "album_id": 3,
        "song_name": "don't understand",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Sketchez - Don't Understand [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "dont_understand.mp3",
        "lyrics_file_name": "dont_understand.txt",
    },
    {
        "user": new_users[12],
        "album_id": 4,
        "song_name": "closer",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/ROY KNOX - Closer [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics1.txt",
        "song_file_name": "closer.mp3",
        "lyrics_file_name": "closer.txt",
    },
    {
        "user": new_users[12],
        "album_id": 5,
        "song_name": "cricket (we nice)",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/ORGAN - Cricket (we nice) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "cricket.mp3",
        "lyrics_file_name": "cricket.txt",
    },
    {
        "user": new_users[13],
        "album_id": 6,
        "song_name": "fly away",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Krys Talk - Fly Away [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "fly_away.mp3",
        "lyrics_file_name": "fly_away.txt",
    },
    {
        "user": new_users[14],
        "album_id": 7,
        "song_name": "river",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Daniel Levi - River [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "river.mp3",
        "lyrics_file_name": "river.txt",
    },
    {
        "user": new_users[14],
        "album_id": 7,
        "song_name": "that's what make it right",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Daniel Levi - That's What Makes It Right [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "make_it_right.mp3",
        "lyrics_file_name": "make_it_right.txt",
    },
    {
        "user": new_users[14],
        "album_id": 8,
        "song_name": "if I disappear",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Tobu - If I Disappear (ft. Tom Mårtensson) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics2.txt",
        "song_file_name": "disappear.mp3",
        "lyrics_file_name": "disappear.txt",
    },
    {
        "user": new_users[14],
        "album_id": 9,
        "song_name": "running away",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Shiah Maisel, Abstrakt, Perk Pietrek - Running Away [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "running_away.mp3",
        "lyrics_file_name": "running_away.txt",
    },
    {
        "user": new_users[15],
        "album_id": 10,
        "song_name": "gone",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Wiguez - Gone (Feat. Rico 56) (Thorne Remix) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "gone.mp3",
        "lyrics_file_name": "gone.txt",
    },
    {
        "user": new_users[15],
        "album_id": 10,
        "song_name": "pressure",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Wiguez - Pressure (Fectro Remix) [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "pressure.mp3",
        "lyrics_file_name": "pressure.txt",
    },
    {
        "user": new_users[15],
        "album_id": 11,
        "song_name": "slow down",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Jim Yosef & Shiah Maisel - Slow Down [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "slow_down.mp3",
        "lyrics_file_name": "slow_down.txt",
    },
    {
        "user": new_users[15],
        "album_id": 12,
        "song_name": "take our time",
        "audio_file_path": "/home/monk/spotlight/backend/static/Test_Songs/Tollef - Take Our Time [NCS Release].mp3",
        "lyrics_file_path": "/home/monk/spotlight/backend/static/Test_Lyrics/lyrics3.txt",
        "song_file_name": "take_our_time.mp3",
        "lyrics_file_name": "take_our_time.txt",
    },
]

for song in songs:
    add_song(**song)
    print(f"{song['song_name']} song added")


## creating playlists


## Adding songs to playlists


## Adding user reviews on songs


## Flagging some songs


## Flagging some albums
