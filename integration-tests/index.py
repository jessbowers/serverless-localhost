import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, ctx):
  logger.info("Handling as %s", ctx.function_name)
  logger.info("env %s", os.environ)
  return {
    "statusCode": 200,
    "body": "hello python"
  }