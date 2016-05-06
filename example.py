# -*- coding: utf-8 -*-

"""
Examples
"""

from awesomelog import logging
import module1

logger = logging.getLogger(__name__)

logger.info('Script started')
module1.dostuff()
logger.info('Script ended')
