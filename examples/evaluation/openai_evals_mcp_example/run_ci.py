import random
import sys

# Simulated eval results
accuracy = random.uniform(0.8, 1.0)
latency = random.uniform(0.1, 0.9)

print(f"Accuracy: {accuracy:.2f}")
print(f"Latency: {latency:.2f}")

# Thresholds
if accuracy < 0.85 or latency > 0.8:
    sys.exit("Thresholds not met")
