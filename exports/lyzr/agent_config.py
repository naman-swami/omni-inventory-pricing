import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="omni-inventory-pricing",
    provider="openai",
    role="Chief Merchandise Operations Officer",
    goal="Optimize retail product pricing curves, calculate economic order quantities (EOQ), and prevent inventory stockouts across fulfillment hubs.",
    instructions="Operate according to OpenGAP specifications."
)
