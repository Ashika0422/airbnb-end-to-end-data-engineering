import logging
import os

from config import LOGS

os.makedirs(LOGS, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOGS, "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)