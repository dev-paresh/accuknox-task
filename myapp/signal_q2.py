
# Here what i have implement:
# -----------------------------------------------------------------------------

# I created a custom Django signal because I wanted to check whether Django signals run in the same thread as the caller.
# I used threading.get_ident() to get the thread ID because it uniquely identifies the current thread, allowing me to compare the sender and receiver threads.
# I printed the thread ID before sending the signal and inside the receiver because this would help confirm if both were running in the same thread.
# When I ran the script, I saw that the sender and receiver had the same thread ID, proving that Django signals execute in the same thread as the caller by default.

import threading
from django.dispatch import Signal, receiver

from django.conf import settings
settings.configure()

thread_signal = Signal()

@receiver(thread_signal)
def thread_receiver(sender, **kwargs):
    print(f"Receiver thread ID: {threading.get_ident()}")

print(f"Sender thread ID: {threading.get_ident()}")
thread_signal.send(sender="test_sender")



# sample out put
# ----------------------------------------------------

# Sender thread ID: 140084689793472
# Receiver thread ID: 140084689793472