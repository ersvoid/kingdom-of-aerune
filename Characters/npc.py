from Functions.generate_character import random_npc, random_char
from Classes.inventory import weapons, staffs, potions, elixirs, armors
from Classes.magic import heal, firebolt

# Village people

blacksmith = random_npc(prof="shop")
innkeeper = random_npc(prof="inn")
mayor = random_npc(prof="mayor")
armorsmith = random_npc(prof="arm")
npc_town1 = random_npc()
npc_town2 = random_npc()
npc_town3 = random_npc()
npc_town4 = random_npc()
npc_town5 = random_npc()

town_pop = [mayor, blacksmith, innkeeper, armorsmith, npc_town1, npc_town2, npc_town3, npc_town4, npc_town5]


# Enemies


m_lst = [firebolt, heal]
bandit_items = {"weapon": weapons[1], "armor":armors[0], "items": "Nothing here"}
guard_items = {"weapon": weapons[2], "armor":armors[3], "items": "Nothing here"}
leader_items = {"weapon": weapons[3],"potions": potions[0], "armor":armors[2], "items": "Nothing here" }
troll_items = {"weapon": weapons[4], "potions": potions[0], "armor":armors[5], "items": "Nothing here"}
wizard_items = {"weapon": staffs[1], "potions": potions[0], "elixirs": elixirs[0], "armor":armors[0], "items": "Nothing here"}

bandit1 = random_char(20, 10, [], bandit_items, a=2, x="bandit")
bandit2 = random_char(50, 10, [], bandit_items, a=5, x="bandit")
bandit3 = random_char(10, 10, [], bandit_items, x="bandit")
bandit4 = random_char(10, 10, [], bandit_items, x="bandit")
bandit5 = random_char(10, 10, [], bandit_items, x="bandit")

sentry = random_char(150, 100,  [], guard_items, a=15, x="leader")
bodyguard = random_char(250, 100,  [], guard_items, a=25, x="leader")

bandit_leader = random_char(100, 200,  [], leader_items, a=10, x="leader")
fake_mayor = random_char(150, 500, [], leader_items, a=15, x="leader")
new_leader = random_char(200, 100, [], leader_items, a=20, x="leader")

troll = random_char(1000, 500,  [], troll_items, a=10, x="bandit")

wizard = random_char(2500, 1000,  m_lst, wizard_items, a=25, x="wizard")
wizard_apprentice = random_char(1000, 1000,  m_lst, wizard_items, a=10, x="wizard")

bandits = [bandit1, bandit2, bandit3, bandit4, bandit5]
guards = [sentry, bodyguard]
leaders = [bandit_leader, fake_mayor, new_leader]
trolls = [troll]
wizards = [wizard_apprentice, wizard]
