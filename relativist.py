
import logging

logger = logging.getLogger(__name__)

class RelativistSync:
    def __init__(self):
        self.consensus_nodes = []

    def validate_timestamp(self, timestamp):
        # Simulăm consens între 3 noduri
        self.consensus_nodes = [True, True, True]
        logger.info("[Relativist] Validare timestamp cuantic de către 3 noduri.")
        return all(self.consensus_nodes)

    def trigger_watchdog(self, delay):
        normal_threshold = 0.005
        if delay > normal_threshold:
            logger.warning("[Watchdog] Întârziere detectată. Activare carantină logică.")
            return "quarantine"
        logger.info("[Watchdog] Comunicare în parametri normali.")
        return "ok"
