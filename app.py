import clashroyale
import logging
from pprint import pprint

TOKEN=open("token", "r").read().strip()
clan_tag = '9Q0RL8Q8'

kind_mapper = {
    'casual2v2': 'other',
    'casual1v1': 'other',
    'PvP': 'other',
    'friendly': 'other',
    'challenge': 'other',
    'riverRacePvP': 'clan',
    'riverRaceDuel': 'clan',
    'boatBattle': 'boat' # I think this battles are attacks to our boat
}

def get_battle_summary(player):
    battles = client.get_player_battles(player)
    summary = {'clan': 0, 'other': 0, 'boat': 0}
    for battle in battles:
        kind = kind_mapper[battle.type]
        summary[kind] += 1
    return summary

logging.basicConfig(level=logging.INFO)

client = clashroyale.official_api.Client(token=TOKEN, cache_fp='clash.db')

members = client.get_clan_members(clan_tag)

for member in members:
    battle_summary = get_battle_summary(member.tag)
    print(f"[{member.name}] "
        f"Donation rating {member.donations - member.donationsReceived} "
        f"Clan battles {battle_summary['clan']} "
        f"Other battles {battle_summary['other']} ")
