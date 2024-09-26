import nacl.utils
from nacl.public import PrivateKey
from nacl.signing import SigningKey
import hashlib

class PseudoVRF:
  def __init__(self):
      # Generate a signing key pair
      self.signing_key = SigningKey.generate()
      self.verify_key = self.signing_key.verify_key

  def prove(self, input_data):
      # Sign the input data
      signature = self.signing_key.sign(input_data)
      
      # Use the signature to generate a pseudo-random output
      output = hashlib.sha256(signature).digest()
      
      return output, signature

  def verify(self, input_data, output, signature):
      # Verify the signature
      try:
          self.verify_key.verify(signature)
      except nacl.exceptions.BadSignatureError:
          return False
      
      # Regenerate the output and compare
      regenerated_output = hashlib.sha256(signature).digest()
      return output == regenerated_output

# Usage example
vrf = PseudoVRF()

# Generate a proof
input_data = b"Some input data"
output, proof = vrf.prove(input_data)

print(f"Output: {output.hex()}")
print(f"Proof: {proof.hex()}")

# Verify the proof
is_valid = vrf.verify(input_data, output, proof)
print(f"Is valid: {is_valid}")