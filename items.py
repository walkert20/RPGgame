#items.py

#class Item():
#	def __init__(self, name, value, output):
#		self.name = name
#		self.value = value
#		self.output = output

def store(Item):
	# Update the value at the Key that matches the Item's name.
	storage[Item] +=1

def use(Item):
	# The item is used in the battle system and removed from the storage
	if (storage[Item] != 0):
		storage[Item] -=1
		return (Item, description[Item], value[Item])
	else:
		print("You don't have any " + Item +".")
		return 0


# Item descriptions (By Silvia "Silvy" Boy):
# NOTE: As the game progresses, append items to the storage.
water = "(Heals a single player a small amount): It's water. Probably not clean, but will still hydrate you."
grenade = "(Deals damage to the whole enemy team): Chuck one of these and everyone clears the f#ck out, haha!"
large_water = "(Heals the whole team a small amount): Hey, save some for the rest of us!"
large_grenade = "(Deals massive damage to the whole enemy team): Whoa, where were you keeping that?"
rocket_launcher = "(Deals massive damage to a single enemy): Real nice of someone to leave this lying around."
burn_relief = "(Removes 'Burned' status from a single player): Stop your whining, it's not that bad." 
antidote = "(Removes 'Poisoned' status from a single player): Blegh! It tastes like medicine. Wait, it is medicine!"
clean_water = "(Heals a single player a large amount): I kind of miss the metallic taste."
bread = "(Heals a single player a moderate amount and raises their strength by 10): Eat up. No telling when we might get another piece."
shock_grenade = "(Deals electric damage to a single enemy. Extra damage to machines): Shocking, isn't it?"
pocket_watch = "(Call on aid from another time. Damage is randomized): Shiny. Seems like it belongs to a 'CB', whoever that is."

def check_inventory(storage):
	pass
	# Print storage (key,value) 

storage = {"water":0, "grenade":0}

description = {"water":"heal", "grenade":"harm"}

value = {"water":20, "grenade":20}

