from Functions.generate_character import random_npc, random_char
from Classes.inventory import weapons, staffs, potions, elixirs
from Classes.magic import heal, firebolt

# Village people

blacksmith = random_npc(prof="shop")
innkeeper = random_npc(prof="inn")
mayor = random_npc(prof="mayor")
npc_town1 = random_npc()
npc_town2 = random_npc()
npc_town3 = random_npc()
npc_town4 = random_npc()
npc_town5 = random_npc()

town_pop = [mayor, blacksmith, innkeeper, npc_town1, npc_town2, npc_town3, npc_town4, npc_town5]


# Enemies


m_lst = [firebolt, heal]
bandit_items = {"weapon": weapons[0]}
guard_items = {"weapon": weapons[2]}
leader_items = {"weapon": weapons[3],"potions": potions[0]}
troll_items = {"weapon": weapons[4], "potions": potions[0]}
wizard_items = {"weapon": staffs[1], "potions": potions[0], "elixirs": elixirs[0]}

bandit1 = random_char(0, [], bandit_items, x="bandit")
bandit2 = random_char(0, [], bandit_items, x="bandit")
bandit3 = random_char(0, [], bandit_items, x="bandit")
bandit4 = random_char(0, [], bandit_items, x="bandit")
bandit5 = random_char(0, [], bandit_items, x="bandit")

sentry = random_char(100,  [], guard_items, a=5, x="leader")
bodyguard = random_char(100,  [], guard_items, a=5, x="leader")

bandit_leader = random_char(200,  [], leader_items, a=5, x="leader")
fake_mayor = random_char(500, [], leader_items, a=5, x="leader")
new_leader = random_char(100, [], leader_items, a=5, x="leader")

troll = random_char(500,  [], troll_items, a=5, x="bandit")

wizard = random_char(1000,  m_lst, wizard_items, a=1, x="wizard")
wizard_apprentice = random_char(1000,  m_lst, wizard_items, a=5, x="wizard")

bandits = [bandit1, bandit2, bandit3, bandit4, bandit5]
guards = [sentry, bodyguard]
leaders = [bandit_leader, fake_mayor, new_leader]
trolls = [troll]
wizards = [wizard, wizard_apprentice]
