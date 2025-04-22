
import random
import logging

logger = logging.getLogger(__name__)

class GhostAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.status = "inactive"

    def activate(self):
        self.status = "active"
        logger.info(f"[Ghost] Agentul {self.agent_id} este acum activ și invizibil.")

    def deactivate(self):
        self.status = "inactive"
        logger.info(f"[Ghost] Agentul {self.agent_id} este acum inactiv.")

    def teleport(self, destination):
        logger.info(f"[Ghost] Agentul {self.agent_id} se teleportează la {destination}.")

    def replicate(self):
        new_id = f"{self.agent_id}_clone_{random.randint(1000, 9999)}"
        logger.info(f"[Ghost] Replicare: {new_id}")
        return GhostAgent(new_id)
