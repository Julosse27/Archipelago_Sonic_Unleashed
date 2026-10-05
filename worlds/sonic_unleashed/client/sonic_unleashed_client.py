from CommonClient import CommonContext, ClientStatus, NetworkItem
import asyncio
import os
import json

def jeu_lance():
    return False

class SonicUnleashedContext(CommonContext):
    game = "Sonic Unleashed"
    items_handling = 0b111
    want_slot_data = True
    item_id_to_name: dict[int, str]
    item_index: int
    chemin_compteur_ap = os.path.join(os.path.dirname(os.getenv("appdata", "")), "Local", "Sonic Unleashed Recompiled AP", "compteur.json")

    async def server_auth(self, password_requested=False):
        if password_requested and not self.password:
            await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            # Il faudra setup le jeu en fonction de ce qu'il y aurra la dedans
            self.item_id_to_name = args["slot_info"]["item_id_to_name"]
            self.seed_name = args["slot_info"]["seed_name"]
            self.total_medals = args["slot_info"]["total_medals"]

    async def on_check(self, location_ids: set):
        await self.check_locations(location_ids)

    async def on_goal_complete(self):
        await self.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])

    def get_item_index(self) -> int:
        if not os.path.exists(os.path.dirname(self.chemin_compteur_ap)):
            os.mkdir(os.path.dirname(self.chemin_compteur_ap))
        if self.item_index == None:
            with open(self.chemin_compteur_ap, "r") as file:
                try:
                    compteur = json.load(file)
                except:
                    compteur = None
            if compteur == None or not (compteur["seed_name"] == self.seed_name and compteur["slot"] == self.slot):
                rep = 0

                with open(self.chemin_compteur_ap, "w") as file:
                    json.dump({"seed_name": self.seed_name, "slot": self.slot, "compteur": 0}, file)
            else:
                rep: int = compteur["compteur"]
        else:
            rep = self.item_index

        return rep

    def get_checks(self) -> list[int]:
        """
        Retourne tout les nouvelles locations
        """

        return []

    def boss_level_complete(self):
        return False

    def give_item(self, item: NetworkItem):
        if self.item_id_to_name[item.item].split(" - ")[0] == "Collectible: moon medal":
            self.moon_medals += 1
        elif self.item_id_to_name[item.item].split(" - ")[0] == "Collectible: sun medal":
            self.sun_medals += 1

    def is_enought_medals(self):
        if self.sun_medals > self.total_medals[0] and self.moon_medals > self.total_medals[1]:
            return True
        else:
            return False

    def increment_item_index(self):
        self.item_index += 1

        temp = self.chemin_compteur_ap + ".tmp"
        with open(temp, "w") as file:
            json.dump({"seed_name": self.seed_name, "slot": self.slot, "compteur": self.item_index}, file)

        os.replace(temp, self.chemin_compteur_ap)

    async def game_watcher(self):
        while not self.exit_event.is_set():
            await asyncio.sleep(0.5)

            if self.slot is None:
                continue
            if not jeu_lance():
                continue

            checks = self.get_checks()
            if checks != []:
                await self.check_locations(checks)

            while self.get_item_index() < len(self.items_received):
                self.give_item(self.items_received[self.get_item_index()])
                self.increment_item_index()

            if self.boss_level_complete() and self.is_enought_medals():
                pass