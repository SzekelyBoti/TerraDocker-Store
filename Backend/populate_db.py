from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from models import Game, create_db_engine
def populate_database():
  engine = create_db_engine()
  Session = sessionmaker(bind=engine)
  session = Session()
  data = [
    {
           "id": 1,
           "name": "Palworld",
           "genre": "Action RPG",
           "price": "29.99",
           "quantity": 278,
           "release_date": "2024-01-19",
           "description": "Palworld is a captivating action-adventure game set in a vibrant open world, where players befriend and raise mystical creatures known as Pals while navigating challenges and uncovering the game's rich narrative.",
           "developer": "Pocketpair",
           "image": "https://images.squarespace-cdn.com/content/v1/5ec3dc7fac9fc01d0a86c2cc/1705664219919-2IFVW9HB6JBL1Q42SMIH/palworld-tag-page-cover-art.jpg",
           "release": "2024-01-19"
    },
    {
           "id": 2,
           "name": "Cyberpunk 2077",
           "genre": "Action RPG",
           "price": "59.99",
           "quantity": 197,
           "release_date": "2020-12-10",
           "description": "Step into the dystopian future of Night City in Cyberpunk 2077, an action-packed RPG that immerses players in a narrative-driven, visually stunning world filled with choices and consequences.",
           "developer": "CD Projekt",
           "image": "https://i.redd.it/w44jvkcns8461.png",
           "release": "2020-12-10"
    },
    {
           "id": 3,
           "name": "Assassin's Creed Valhalla",
           "genre": "Action RPG",
           "price": "59.99",
           "quantity": 145,
           "release_date": "2020-11-10",
           "description": "Embark on a Viking adventure in Assassin's Creed Valhalla, where players take on the role of Eivor, a fierce warrior, and lead their clan to conquer new lands in a captivating open-world setting.",
           "developer": "Ubisoft Montreal",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202011/0302/8jomNsyMYDoJnzFkBrr9Rit2.jpg",
           "release": "2020-11-10"
    },
    {
           "id": 4,
           "name": "Call of Duty: Black Ops Cold War - Ultimate Edition",
           "genre": "First-Person Shooter",
           "price": "99.99",
           "quantity": 134,
           "release_date": "2020-11-13",
           "description": "Experience the intense and gripping Cold War-era narrative in Call of Duty: Black Ops Cold War, where players engage in thrilling FPS action and make critical decisions that shape the outcome of the Cold War.",
           "developer": "Treyarch",
           "image": "https://store-images.s-microsoft.com/image/apps.43853.13655629581078567.571ec8ca-5412-4d72-8ac1-e201c6d3c602.891e30cb-5f6b-44f2-b962-1bffde3d148d?w=400&h=600",
           "release": "2020-11-13"
    },
    {
           "id": 5,
           "name": "Spider-Man: Miles Morales",
           "genre": "Action-Adventure",
           "price": "49.99",
           "quantity": "196",
           "release_date": "2020-11-12",
           "description": "Swing through the streets of New York as the iconic superhero Miles Morales in this action-packed adventure. Unleash new powers, face formidable foes, and become the next Spider-Man.",
           "developer": "Insomniac Games",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202008/1020/PRfYtTZQsuj3ALrBXGL8MjAH.jpg"
    },
    {
           "id": 6,
           "name": "Demon's Souls",
           "genre": "Action RPG",
           "price": "69.99",
           "quantity": 163,
           "release_date": "2020-11-12",
           "description": "Immerse yourself in the challenging and atmospheric world of Demon's Souls, a remake of the classic action RPG. Face deadly foes, uncover mysteries, and explore the haunting landscapes of Boletaria.",
           "developer": "Bluepoint Games",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202011/1717/GemRaOZaCMhGxQ9dRhnQQyT5.png"
    },
    {
           "id": 7,
           "name": "FIFA 21",
           "genre": "Sports",
           "price": "59.99",
           "quantity": 238,
           "release_date": "2020-10-09",
           "description": "Experience the excitement of football at its best in FIFA 21. With enhanced gameplay, realistic graphics, and new features, FIFA 21 delivers an immersive football simulation for fans around the world.",
           "developer": "EA Vancouver",
           "image": "https://metro.co.uk/wp-content/uploads/2020/07/FIFA21ps42DPFTfront_en_RGB-f627.jpg?quality=90&strip=all",
           "release": "2020-10-09"
    },
    {
           "id": 8,
           "name": "Watch Dogs: Legion",
           "genre": "Action-Adventure",
           "price": "54.99",
           "quantity": 120,
           "release_date": "2020-10-29",
           "description": "In Watch Dogs: Legion, hack your way through a dystopian London as you recruit and play as any character in the city. Uncover a gripping narrative and use hacking skills to liberate the city.",
           "developer": "Ubisoft Toronto",
           "image": "https://s3.amazonaws.com/prod-media.gameinformer.com/2020/08/03/151c457b/328-cover-front-1024.jpg"
    },
    {
           "id": 9,
           "name": "Star Wars: Squadrons",
           "genre": "Space Simulation",
           "price": "39.99",
           "quantity": "234",
           "release_date": "2020-10-02",
           "description": "Take control of iconic starfighters in Star Wars: Squadrons, an immersive space simulation game. Engage in thrilling dogfights, participate in fleet battles, and experience the galaxy far, far away.",
           "developer": "Motive Studios",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202009/2410/aaIGMZl7LGnfbmQNOrHOrL6c.png"
    },
    {
           "id": 10,
           "name": "Madden NFL 21",
           "genre": "Sports",
           "price": "49.99",
           "quantity": "124",
           "release_date": "2020-08-28",
           "description": "Get ready for gridiron greatness in Madden NFL 21. Experience the excitement of American football with improved gameplay, realistic graphics, and new features that bring the NFL to life.",
           "developer": "EA Tiburon",
           "image": "https://m.media-amazon.com/images/I/81TZ7BKHMjL.jpg"
    },
    {
           "id": 11,
           "name": "Ghost of Tsushima - Director's cut",
           "genre": "Action-Adventure",
           "price": "59.99",
           "quantity": "123",
           "release_date": "2020-07-17",
           "description": "Journey back to feudal Japan in Ghost of Tsushima, an action-packed open-world adventure. Become the Ghost and embark on a quest for vengeance against the Mongol invaders.",
           "developer": "Sucker Punch Productions",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202106/2322/v53I7qHvpWSQsL2oLxrM46NV.png"
    },
    {
           "id": 12,
           "name": "The Last of Us Part II",
           "genre": "Action-Adventure",
           "price": "69.99",
           "quantity": "431",
           "release_date": "2020-06-19",
           "description": "Experience an emotionally charged journey in The Last of Us Part II. Navigate a post-apocalyptic world, face intense challenges, and make difficult choices that shape the fate of Ellie.",
           "developer": "Naughty Dog",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202010/2618/Y02ljdBodKFBiziorYgqftLE.png"
    },
    {
           "id": 13,
           "name": "Far Cry 6",
           "genre": "First-Person Shooter",
           "price": "59.99",
           "quantity": "123",
           "release_date": "2021-10-07",
           "description": "Embark on a revolution in Far Cry 6. Set in the tropical paradise of Yara, players join the guerrilla movement to liberate the nation from the oppressive rule of Anton Castillo.",
           "developer": "Ubisoft Toronto",
           "image": "https://buycheapplaycheap.com/wp-content/uploads/2021/09/Far-Cry-6.jpg"
    },
    {
           "id": 14,
           "name": "Deathloop",
           "genre": "Action",
           "price": "49.99",
           "quantity": "213",
           "release_date": "2021-09-14",
           "description": "Break the time loop in Deathloop, an immersive action game. Play as Colt, trapped on the mysterious island of Blackreef, and unravel the secrets behind the repeating cycle of death and mayhem.",
           "developer": "Arkane Studios",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202007/1617/PgGbOmz7wrheZhlYrNQQ87Ib.jpg"
    },
    {
           "id": 15,
           "name": "Ratchet & Clank: Rift Apart",
           "genre": "Action-Adventure",
           "price": "69.99",
           "quantity": "321",
           "release_date": "2021-06-11",
           "description": "Join Ratchet and his robotic companion Clank in an interdimensional adventure. Explore stunning worlds, defeat nefarious foes, and witness the power of the PlayStation 5 in Rift Apart.",
           "developer": "Insomniac Games",
           "image": "https://cdna.artstation.com/p/assets/covers/images/039/370/448/large/anna-roan-anna-roan-artstation-thumbnail-cover.jpg?1625698821"
    },
    {
           "id": 16,
           "name": "Resident Evil Village",
           "genre": "Action-Horror",
           "price": "59.99",
           "quantity": "132",
           "release_date": "2021-05-07",
           "description": "Experience the terror in Resident Evil Village. As Ethan Winters, navigate a mysterious village, face grotesque creatures, and uncover a chilling story in this survival horror masterpiece.",
           "developer": "Capcom",
           "image": "https://img.redbull.com/images/c_crop,x_351,y_0,h_630,w_473/c_fill,w_450,h_600/q_auto:low,f_auto/redbullcom/2021/1/15/i4htflrfw8viwtzgfyni/resident-evil-village-cover"
    },
    {
           "id": 17,
           "name": "Returnal",
           "genre": "Third-Person Shooter",
           "price": "69.99",
           "quantity": "234",
           "release_date": "2021-04-30",
           "description": "Embark on a surreal sci-fi journey in Returnal. Play as Selene, trapped on an alien planet, and battle nightmarish creatures in a constantly changing environment with each death resetting the cycle.",
           "developer": "Housemarque",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202011/1621/4ItSbqJE88H019Ua3WBQKLF8.png"
    },
    {
           "id": 18,
           "name": "Outriders",
           "genre": "Cooperative Shooter",
           "price": "49.99",
           "quantity": "134",
           "release_date": "2021-04-01",
           "description": "Join the Outriders on Enoch, a mysterious and hostile planet. Engage in intense cooperative shooter gameplay, explore a dark sci-fi world, and unravel the secrets of the Anomaly.",
           "developer": "People Can Fly",
           "image": "https://cdn11.bigcommerce.com/s-6rs11v9w2d/images/stencil/1280x1280/products/1108/3174/b9a4df7dba8e640025ac72bac27c43a5__35763.1675458016.jpg?c=1"
    },
    {
           "id": 19,
           "name": "It Takes Two",
           "genre": "Action-Adventure",
           "price": "39.99",
           "quantity": "314",
           "release_date": "2021-03-26",
           "description": "Embark on a whimsical and heartwarming journey in It Takes Two. Play as two tiny characters, Cody and May, navigating through a fantastical world to mend the broken bond of a married couple.",
           "developer": "Hazelight Studios",
           "image": "https://cdn-products.eneba.com/resized-products/5JzUnzfcLd7T0_XHcaam5ry7LSjd4NamuBdAARtpLiA_350x200_1x-0.jpeg"
    },
    {
           "id": 20,
           "name": "Hitman 3",
           "genre": "Stealth",
           "price": "59.99",
           "quantity": "63",
           "release_date": "2021-01-20",
           "description": "Become the ultimate assassin in Hitman 3. Agent 47 returns for the dramatic conclusion to the World of Assassination trilogy, taking players on a globetrotting adventure full of intrigue and espionage.",
           "developer": "IO Interactive",
           "image": "https://i.redd.it/m9kuc4as7vd61.png"
    },
    {
           "id": 21,
           "name": "Cyber Shadow",
           "genre": "Platformer",
           "price": "19.99",
           "quantity": "234",
           "release_date": "2021-01-26",
           "description": "Unleash your ninja skills in Cyber Shadow, a retro-inspired platformer. As the lone warrior, Shadow, battle through a cybernetic world filled with challenging enemies and epic boss fights.",
           "developer": "Mechanical Head Studios",
           "image": "https://e.snmc.io/lk/l/x/35b23db33f22f80c7efd513669ca1ff1/9317261"
    },
    {
           "id": 22,
           "name": "Immortals Fenyx Rising",
           "genre": "Action-Adventure",
           "price": "49.99",
           "quantity": "123",
           "release_date": "2020-12-03",
           "description": "Embark on a mythological adventure in Immortals Fenyx Rising. Play as Fenyx, a winged demigod, and face legendary creatures, solve puzzles, and explore a vibrant open-world inspired by Greek mythology.",
           "developer": "Ubisoft Quebec",
           "image": "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/31fc2b104379919.5f61db116314d.jpg"
    },
    {
           "id": 23,
           "name": "Call of Duty: Modern Warfare 3 (2023)",
           "genre": "First-Person Shooter",
           "price": "69.99",
           "quantity": "232",
           "release_date": "2023-11-10",
           "description": "Join Captain Price and Task Force 141 as they face off against the ultimate threat, ultranationalist Vladimir Makarov. Open Combat Missions: New Open Combat Missions redefine the traditional Campaign level.",
           "developer": "Infinity Ward",
           "image": "https://i.imgur.com/hZhDm7Kl.png"
    },
    {
           "id": 24,
           "name": "Doom Eternal",
           "genre": "First-Person Shooter",
           "price": "59.99",
           "quantity": "231",
           "release_date": "2020-03-20",
           "description": "Unleash hell in Doom Eternal, the action-packed FPS. As the Doom Slayer, face hordes of demons in epic battles, explore new dimensions, and experience the ultimate power fantasy.",
           "developer": "id Software",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202010/0114/b4Q1XWYaTdJLUvRuALuqr0wP.png"
    },
    {
           "id": 25,
           "name": "Animal Crossing: New Horizons",
           "genre": "Life Simulation",
           "price": 49.99,
           "quantity": 120,
           "release_date": "2020-03-20",
           "description": "Create your own paradise in Animal Crossing: New Horizons. Build, customize, and explore your island home, interact with charming anthropomorphic villagers, and enjoy the relaxing life simulation experience.",
           "developer": "Nintendo",
           "image": "https://i.ebayimg.com/images/g/aNgAAOSwVChgEZxF/s-l1200.webp"
    },
    {
           "id": 26,
           "name": "Final Fantasy VII Remake",
           "genre": "Action RPG",
           "price": 69.99,
           "quantity": 90,
           "release_date": "2020-04-10",
           "description": "Relive the epic journey of Cloud Strife in Final Fantasy VII Remake. Experience a reimagined classic with stunning visuals, engaging combat, and a captivating story set in the iconic city of Midgar.",
           "developer": "Square Enix",
           "image": "https://assets1.ignimgs.com/2020/04/06/final-fantasy-vii-remake---button-fin-1586205679705.jpg"
    },
    {
           "id": 27,
           "name": "Genshin Impact",
           "genre": "Action RPG",
           "price": 0,
           "quantity": 200,
           "release_date": "2020-09-28",
           "description": "Embark on a breathtaking open-world adventure in Genshin Impact. Explore the fantasy realm of Teyvat, assemble a diverse party of characters, and unleash elemental powers in this free-to-play action RPG.",
           "developer": "miHoYo",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202104/2507/Xdncb153Sz5UZMaF0X944NP5.png"
    },
    {
           "id": 28,
           "name": "Marvel's Avengers",
           "genre": "Action-Adventure",
           "price": 59.99,
           "quantity": 80,
           "release_date": "2020-09-04",
           "description": "Join Earth's Mightiest Heroes in Marvel's Avengers. Play as iconic superheroes, assemble a team, and take on epic missions to save the world in this action-packed adventure.",
           "developer": "Crystal Dynamics",
           "image": "https://cdn.mobygames.com/covers/9530912-marvel-avengers-xbox-one-front-cover.jpg"
    },
    {
           "id": 29,
           "name": "Crash Bandicoot 4: It's About Time",
           "genre": "Platformer",
           "price": 59.99,
           "quantity": 70,
           "release_date": "2020-10-02",
           "description": "Time-travel with Crash and Coco in Crash Bandicoot 4: It's About Time. Face challenging platforming levels, defeat classic villains, and experience the beloved marsupial's latest adventure.",
           "developer": "Toys for Bob",
           "image": "https://e.snmc.io/lk/l/x/62cc282a1b3c8ddc296a76eafd6cd20f/9388991"
    },
    {
           "id": 30,
           "name": "Assassin's Creed Odyssey",
           "genre": "Action-Adventure",
           "price": 39.99,
           "quantity": 85,
           "release_date": "2018-10-05",
           "description": "Embark on a legendary odyssey in Assassin's Creed Odyssey. Set in ancient Greece, choose your path as a mercenary, explore a vast open world, and shape the course of history.",
           "developer": "Ubisoft Quebec",
           "image": "https://cdn.mobygames.com/covers/7474732-assassins-creed-odyssey-playstation-4-inside-cover.jpg"
    },
    {
           "id": 31,
           "name": "Red Dead Redemption 2",
           "genre": "Action-Adventure",
           "price": 59.99,
           "quantity": 75,
           "release_date": "2018-10-26",
           "description": "Immerse yourself in the expansive and immersive world of Red Dead Redemption 2. Ride through the wild west, experience a gripping narrative, and make choices that shape the destiny of Arthur Morgan.",
           "developer": "Rockstar Games",
           "image": "https://assets.vg247.com/current//2018/05/red_dead_redemption_2_cover_art_1.jpg"
    },
    {
           "id": 32,
           "name": "God of War",
           "genre": "Action-Adventure",
           "price": 49.99,
           "quantity": 90,
           "release_date": "2018-04-20",
           "description": "Embark on a mythological journey with Kratos and Atreus in God of War. Navigate the realms of Norse mythology, face powerful foes, and witness the evolving bond between father and son.",
           "developer": "Santa Monica Studio",
           "image": "https://cdn.mobygames.com/covers/6194621-god-of-war-playstation-4-front-cover.jpg"
    },
    {
           "id": 33,
           "name": "Monster Hunter: World Deluxe Edition",
           "genre": "Action RPG",
           "price": 39.99,
           "quantity": 100,
           "release_date": "2018-01-26",
           "description": "Join the hunt in Monster Hunter: World. Explore diverse ecosystems, track colossal monsters, and craft powerful gear in this action-packed RPG that brings the thrill of the hunt to life.",
           "developer": "Capcom",
           "image": "https://cdn-products.eneba.com/resized-products/D3b5kr9_350x200_3x-0.jpg"
    },
    {
           "id": 34,
           "name": "Fortnite - 2800 V-Bucks",
           "genre": "Battle Royale",
           "price": 22.99,
           "quantity": 150,
           "release_date": "2017-07-25",
           "description": "Jump into the ever-evolving world of Fortnite, a free-to-play battle royale game. Build, battle, and outlast your opponents in fast-paced multiplayer matches with unique building mechanics.",
           "developer": "Epic Games",
           "image": "https://i.ebayimg.com/images/g/rKYAAOSwqY5fhrmq/s-l1600.jpg"
    },
    {
           "id": 35,
           "name": "The Legend of Zelda: Breath of the Wild",
           "genre": "Action-Adventure",
           "price": 59.99,
           "quantity": 110,
           "release_date": "2017-03-03",
           "description": "Embark on an epic adventure in The Legend of Zelda: Breath of the Wild. Explore the vast kingdom of Hyrule, solve puzzles, battle ancient guardians, and uncover the secrets of the wild.",
           "developer": "Nintendo",
           "image": "https://cdn02.plentymarkets.com/qozbgypaugq8/item/images/1613/full/PSTR-ZELDA005.jpg"
    },
    {
           "id": 36,
           "name": "Overwatch 2",
           "genre": "First-Person Shooter",
           "price": 39.99,
           "quantity": 120,
           "release_date": "2022-10-04",
           "description": "Join the ranks of heroes in Overwatch, a team-based first-person shooter. Assemble your team, choose from diverse heroes, and engage in fast-paced multiplayer battles to save the world.",
           "developer": "Blizzard Entertainment",
           "image": "https://sahsponyexpress.com/wp-content/uploads/2022/10/overwatch-2-button-fin-1656022954568-900x900.jpg"
    },
    {
           "id": 37,
           "name": "Dark Souls III",
           "genre": "Action RPG",
           "price": 49.99,
           "quantity": 60,
           "release_date": "2016-04-12",
           "description": "Prepare to die in Dark Souls III, the challenging action RPG. Explore dark and atmospheric landscapes, face deadly foes, and master the intricate combat system in a world on the brink of collapse.",
           "developer": "FromSoftware",
           "image": "https://image.api.playstation.com/cdn/EP0700/CUSA03365_00/OFMeAw2KhrdaEZAjW1f3tCIXbogkLpTC.png"
    },
    {
           "id": 38,
           "name": "Uncharted 4: A Thief's End",
           "genre": "Action-Adventure",
           "price": 49.99,
           "quantity": 80,
           "release_date": "2016-05-10",
           "description": "Embark on Nathan Drake's final adventure in Uncharted 4: A Thief's End. Follow the charismatic treasure hunter as he seeks fortune and faces dangerous adversaries in a quest for legendary treasure.",
           "developer": "Naughty Dog",
           "image": "https://m.media-amazon.com/images/M/MV5BMTYzYzIxMjktMDM4NS00MTM5LWJlMDgtNDRhMDNhOGRmY2EwXkEyXkFqcGdeQXVyMTk2OTAzNTI@._V1_.jpg"
    },
    {
           "id": 39,
           "name": "The Witcher 3: Wild Hunt",
           "genre": "Action RPG",
           "price": 29.99,
           "quantity": 95,
           "release_date": "2015-05-19",
           "description": "Immerse yourself in the epic world of The Witcher 3: Wild Hunt. Follow Geralt of Rivia on a quest to find his adopted daughter, Ciri, and navigate a rich, morally ambiguous fantasy world.",
           "developer": "CD Projekt",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202211/0711/kh4MUIuMmHlktOHar3lVl6rY.png"
    },
    {
           "id": 40,
           "name": "Bloodborne",
           "genre": "Action RPG",
           "price": 39.99,
           "quantity": 70,
           "release_date": "2015-03-24",
           "description": "Face the nightmarish creatures of Yharnam in Bloodborne, an action RPG with intense combat. Explore Gothic environments, uncover dark secrets, and battle grotesque beasts in this challenging journey.",
           "developer": "FromSoftware",
           "image": "https://image.api.playstation.com/vulcan/img/rnd/202010/2614/Sy5e8DmeKIJVjlAGraPAJYkT.png"
    },
    {
           "id": 41,
           "name": "Metal Gear Solid V: The Phantom Pain",
           "genre": "Action-Adventure",
           "price": 49.99,
           "quantity": 85,
           "release_date": "2015-09-01",
           "description": "Experience the final chapter of the legendary Metal Gear Solid series in The Phantom Pain. Play as the iconic Snake, explore an open world, and engage in tactical espionage operations.",
           "developer": "Kojima Productions",
           "image": "https://static.posters.cz/image/750/plakatok/metal-gear-solid-v-the-phantom-pain-cover-i26603.jpg"
    },
    {
           "id": 42,
           "name": "Fallout 4",
           "genre": "Action RPG",
           "price": 29.99,
           "quantity": 100,
           "release_date": "2015-11-10",
           "description": "Survive and thrive in the post-apocalyptic wasteland of Fallout 4. Build settlements, encounter diverse factions, and shape the future of the Commonwealth in this open-world action RPG.",
           "developer": "Bethesda Game Studios",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202009/2500/D59jxQR99Jg545NKa4Nu1FmP.png"
    },
    {
           "id": 43,
           "name": "Batman: Arkham Knight",
           "genre": "Action-Adventure",
           "price": 39.99,
           "quantity": 75,
           "release_date": "2015-06-23",
           "description": "Become the Dark Knight in Batman: Arkham Knight. Face iconic villains, explore Gotham City, and experience the epic conclusion to the Arkham series with the Batmobile at your disposal.",
           "developer": "Rocksteady Studios",
           "image": "https://static.posters.cz/image/750/plakatok/batman-arkham-knight-cover-i24451.jpg"
    },
    {
           "id": 44,
           "name": "The Elder Scrolls V: Skyrim",
           "genre": "Action RPG",
           "price": 19.99,
           "quantity": 110,
           "release_date": "2011-11-11",
           "description": "Embark on an epic journey in The Elder Scrolls V: Skyrim. Explore a vast open world, slay dragons, master shouts, and shape the destiny of Tamriel in this legendary action RPG.",
           "developer": "Bethesda Game Studios",
           "image": "https://preview.redd.it/i-learned-that-the-skyrim-anniversary-edition-cover-art-v0-5fj9bk8lw7891.jpg?auto=webp&s=8d94ff0d8acc4b101187989464962f94a7f54438"
    },
    {
           "id": 45,
           "name": "Portal 2",
           "genre": "Puzzle",
           "price": 29.99,
           "quantity": 60,
           "release_date": "2011-04-18",
           "description": "Immerse yourself in the mind-bending puzzles of Portal 2. Navigate through Aperture Science, solve intricate challenges, and experience the humor and creativity of this acclaimed puzzle game.",
           "developer": "Valve",
           "image": "https://www.gamespot.com/a/uploads/scale_medium/1197/11970954/2426687-2219887-box_portal2.png"
    },
    {
           "id": 46,
           "name": "Mass Effect 3",
           "genre": "Action RPG",
           "price": 39.99,
           "quantity": 80,
           "release_date": "2012-03-06",
           "description": "Commander Shepard returns for the final battle in Mass Effect 3. Lead the fight against the Reapers, make crucial decisions, and experience the epic conclusion to the groundbreaking Mass Effect trilogy.",
           "developer": "BioWare",
           "image": "https://m.media-amazon.com/images/I/71j1rt6O60L.jpg"
    },
    {
           "id": 47,
           "name": "The Legend of Zelda: Skyward Sword",
           "genre": "Action-Adventure",
           "price": 49.99,
           "quantity": 90,
           "release_date": "2011-11-18",
           "description": "Soar through the skies in The Legend of Zelda: Skyward Sword. Join Link on a quest to rescue Princess Zelda, unravel the mysteries of the floating island of Skyloft, and engage in motion-based swordplay.",
           "developer": "Nintendo",
           "image": "https://www.nintendo.com/ph/switch/az89/img/hero_sp.jpg"
    },
    {
           "id": 48,
           "name": "Skyrim VR",
           "genre": "Action RPG",
           "price": 39.99,
           "quantity": 50,
           "release_date": "2017-11-17",
           "description": "Experience The Elder Scrolls V: Skyrim in virtual reality. Immerse yourself in the breathtaking world of Tamriel, wield your weapons in VR, and embark on an epic adventure like never before.",
           "developer": "Bethesda Game Studios",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202009/2820/UKBGQA7E5vUK9gEzKdfkeaYI.png"
    },
    {
           "id": 49,
           "name": "Dead Island 2",
           "genre": "Survival Horror",
           "price": 59.99,
           "quantity": 100,
           "release_date": "2023-04-21",
           "description": "Dead Island 2 is back! A unique formula of horror, dark humor and over the top zombie-slaying.",
           "developer": "Deep Silver Dambuster Studios",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202208/1012/SyX3pwXDmPfzSY6KsdCU6dfk.jpg"
    },
    {
           "id": 50,
           "name": "One Piece Odyssey",
           "genre": "Action-Adventure",
           "price": 59.99,
           "quantity": 90,
           "release_date": "2023-01-10",
           "description": "A brand new RPG set in the world of the popular anime, ONE PIECE! Play as members of the Straw Hat Crew in a fantastic adventure set in the ONE PIECE world!",
           "developer": "ILCA",
           "image": "https://image.api.playstation.com/vulcan/ap/rnd/202208/3012/gJVbYvFrKRIL5OhgmeCd2lOf.png"
    },
    {
           "name": "Cat Game",
           "genre": "Action",
           "price": "99.99",
           "quantity": "158",
           "release_date": "2024-02-07",
           "description": "A game about a very aggressive cat",
           "developer": "G2A Killers",
           "image": "https://img.freepik.com/premium-photo/picture-cat-with-gun-his-face_281348-56.jpg",
           "id": 51
    },
    {
           "name": "Another Game About Cats",
           "genre": "Horror",
           "price": "59.99",
           "quantity": "12",
           "release_date": "2024-01-23",
           "description": "oooo oooo very scary",
           "developer": "G2A Killers",
           "image": "https://img.freepik.com/premium-photo/horror-cat_839844-8.jpg",
           "id": 52
    },
    {
           "name": "Sniper Elite 5",
           "genre": "Action-Adventure",
           "price": "49.99",
           "quantity": "70",
           "release_date": "2022-05-26",
           "description": "The award-winning series returns as Karl Fairburne fights to uncover Project Kraken in 1944 France. The genre-defining authentic sniping, with enhanced kill cam, has never looked or felt better as you fight across immersive maps to stop the Nazi war machine in its tracks. ",
           "developer": "Rebellion",
           "image": "https://gamefaqs.gamespot.com/a/box/3/5/6/860356_front.jpg",
           "id": 53
    }
  ]
  for game in data:
    new_game = Game(
    id=game['id'],
    name=game['name'],
    genre=game['genre'],
    price=float(game['price']),
    quantity=game['quantity'],
    release_date=datetime.strptime(game['release_date'], "%Y-%m-%d").date(), 
    description=game['description'],
    developer=game['developer'],
    image=game['image']
  )
  session.add(new_game)
  session.commit()
  session.close()
  print("Data populated successfully!")

if __name__ == '__main__':
  populate_database() 
