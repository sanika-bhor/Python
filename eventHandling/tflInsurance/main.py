from Dispatcher import EventDispatcher
from Model import Claim
from Handlers import ClaimHandler

dispatcher = EventDispatcher()
dispatcher.subscribe("ClaimSubmitted", ClaimHandler.validate_claim)
dispatcher.subscribe("ClaimSubmitted", ClaimHandler.notify_customer)
dispatcher.subscribe("ClaimSubmitted", ClaimHandler.notify_claims_officer)
dispatcher.subscribe("ClaimSubmitted", ClaimHandler.update_audit_log)


# claim = {
#     "claim_id": "CLM1001",
#     "customer_name": "Rahul",
#     "customer_email": "rahul@example.com",
#     "amount": 50000
# }

claim=Claim("CLM1001", "Rahul","rahul@example.com", 50000)

dispatcher.publish("ClaimSubmitted", claim)