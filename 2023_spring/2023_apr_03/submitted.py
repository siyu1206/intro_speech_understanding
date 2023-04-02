import numpy as np

def generate_pure_tone(frequency, sample_rate, duration):
    '''
    Generate a pure tone at the specified frequency, sampling rate, and duration.
    @parameter:
    frequency (scalar) - the frequency of the pure tone, in Hertz
    sample_rate (scalar) - how many samples per second?
    duration (scalar) - the duration of the pure tone, in seconds
    '''
    t = np.linspace(0,duration,sample_rate)
    x = np.sine(2*np.pi*frequency*t)
    return(x)

