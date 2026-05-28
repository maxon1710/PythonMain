

class Lead:
    def __init__(self, name):
        self.name = name

def change_name(lead_obj: Lead, new_name):
    lead_obj.name = new_name


lead = Lead("max")
print(f"Был лид - {lead.name}")

change_name(lead, "Dima")
print(f"Стал лид - {lead.name}")

