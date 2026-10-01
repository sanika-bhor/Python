

def validate_claim(data):

    print("Validating claim:", data.ClaimId)

    if data.Amount <= 0:
        print("Invalid claim amount")
        return

    print("Claim validation completed")


def notify_customer(data):

    print("Sending claim acknowledgement to:",
          data.CustomerEmail)


def notify_claims_officer(data):

    print("Notifying claims officer about:",
          data.ClaimId)


def update_audit_log(data):

    print("Recording claim submission in audit log")

